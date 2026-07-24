from abc import ABC, abstractmethod
from src.core.quantum_code.quantum_code_basis import QuantumCodeBasis
from src.core.optimization.variational_parameters import VariationalParameters
from src.core.input.problem_statement import ProblemStatement
from src.core.quantum_code.quantum_code import QuantumCode


class QuantumCodeBuilder(ABC):
    """
    A module that collects a quantum code based on the input data,
    i.e., the value of the variational parameters and the initial optimization problem,
    depending on the established basis.

    Attributes
    ----------
    code_template:
        A quantum circuit template that will be used for compilation to avoid multiple code builds.
    """
    code_template: object

    # TODO: проработать систему компиляции
    def __init__(self):
        pass

    @abstractmethod
    def build(
            self,
            basis: QuantumCodeBasis,
            parameters: VariationalParameters,
            objective: ProblemStatement
    ) -> QuantumCode:
        """
        Builds a quantum circuit from the specified basis, variational parameters,
        and optimization problem.

        Args:
            basis: The quantum code basis defining the gate set and circuit structure.
            parameters: The variational parameters to be embedded into the circuit.
            objective: The optimization problem to be encoded in the quantum circuit.

        Returns:
            A ``QuantumCode`` object representing the constructed quantum circuit.
        """
        pass