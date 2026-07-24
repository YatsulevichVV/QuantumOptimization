from src.core.quantum_code.quantum_code_builder import QuantumCodeBuilder
from src.core.input.problem_statement import ProblemStatement
from src.core.input.qubo import QUBO
from src.core.optimization.variational_parameters import VariationalParameters
from src.core.quantum_code.quantum_code import QuantumCode
from src.core.quantum_code.quantum_code_basis import QuantumCodeBasis
import numpy as np


class QAOAAnsatzBuilder(QuantumCodeBuilder):
    """
    The quantum code assembly module for the original QAOA algorithm ansatz developed by Farhi in 2014.

    Attributes
    ----------
    code_template:
        A quantum circuit template that will be used for compilation to avoid multiple code builds.
    """

    def __init__(self):
        super().__init__()

    @staticmethod
    def build_cost_hamiltonian(
            basis: QuantumCodeBasis,
            gamma: float,
            matrix: QUBO,
            n: int
    ) -> str:
        """
        Builds the quantum circuit implementing the cost Hamiltonian.

        Args:
           basis: The quantum code basis defining the circuit representation.
           gamma: The value of variational parameter gamma.
           matrix: The QUBO matrix to be encoded into the cost Hamiltonian.
           n: The dimension of the optimization problem.

        Returns:
           A string containing the quantum assembly code implementing the cost
           Hamiltonian evolution.
        """
        qubo = matrix.tensor
        gate = []
        if basis == QuantumCodeBasis.RZ_CNOT:
            for j in range(n):
                for k in range(n):
                    if qubo[j][k] != 0 and gamma != 0:
                        arg = np.mod(-gamma / 2 * qubo[j][k], 2 * np.pi)
                        if j == k:
                            gate.append(f'rz({np.mod(2 * arg, 2 * np.pi)}) q[{j}];\n')
                        else:
                            gate.append(f'rz({arg}) q[{j}];\n')
                            gate.append(f'rz({arg}) q[{k}];\n')
                            gate.append(f'cx q[{j}],q[{k}];\n')
                            gate.append(f'rz({-arg}) q[{k}];\n')
                            gate.append(f'cx q[{j}],q[{k}];\n')
        # TODO: Добавить реализацию других базисов и проверить корректность реализации
        return ''.join(gate)

    @staticmethod
    def build_mixer_hamiltonian(
            basis: QuantumCodeBasis,
            beta: float,
            n: int
    ) -> str:
        """
        Builds the quantum circuit implementing the mixer Hamiltonian.

        Args:
           basis: The quantum code basis defining the circuit representation.
           beta: The value of variational parameter beta.
           n: The dimension of the optimization problem.

        Returns:
           A string containing the quantum assembly code implementing the mixer
           Hamiltonian evolution.
        """

        gate = []
        if basis == QuantumCodeBasis.RZ_CNOT or basis == QuantumCodeBasis.RZ_RZZ:
            for i in range(n):
                arg = float(np.mod(2 * beta, np.pi))
                gate.append(f'rx({arg}) q[{i}];\n')
        return ''.join(gate)

    def build(
            self,
            basis: QuantumCodeBasis,
            params: VariationalParameters,
            matrix: ProblemStatement
    ) -> QuantumCode:
        """
        Builds a quantum circuit from the specified basis, variational parameters,
        and optimization problem.

        The vector of variation parameters of the QAOA algorithm should have the form
            [gamma_1, ..., gamma_p, beta_1, ..., beta_p]

        Args:
            basis: The quantum code basis defining the gate set and circuit structure.
            params: The variational parameters to be embedded into the circuit.
            matrix: The QUBO matrix to be encoded into the cost Hamiltonian.

        Returns:
            A ``QuantumCode`` object representing the constructed quantum circuit.
        """
        if not (params.size % 2 == 0 and params.size > 0):
            raise ValueError('The count of variational parameters must be even and positive')
        n = matrix.size
        p = params.size // 2
        gamma = params.parameters[:p]
        beta = params.parameters[p:]
        program = ['OPENQASM 2.0;\ninclude \"qelib1.inc\";\n', f'qreg q[{n}];\n']   # Library and register of qubits
        for i in range(n):                                                          # Register of bits
            program.append(f'creg m{i}[1];\n')
        for i in range(n):                                                          # Hadamard gates
            program.append(f'h q[{i}];\n')
        for i in range(p):                                                          # QAOA iterations
            uc = self.build_cost_hamiltonian(basis, gamma[i], matrix, n)
            ub = self.build_mixer_hamiltonian(basis, beta[i], n)
            program.append(uc)
            program.append(ub)
        for i in range(n):                                                          # Measurement
            program.append(f'measure q[{i}] -> m{i}[0];\n')
        return QuantumCode(''.join(program))
