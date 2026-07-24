from src.core.engine.quantum_code_executor import QuantumCodeExecutor
from src.core.input.problem_statement import ProblemStatement
from src.core.optimization.variational_parameters import VariationalParameters
from src.core.output.objective_evaluation_result import ObjectiveEvaluationResult
from src.core.quantum_code.quantum_code_basis import QuantumCodeBasis
from src.core.quantum_code.quantum_code_builder import QuantumCodeBuilder
from src.core.quantum_code.qaoa_ansatz_builder import QAOAAnsatzBuilder


class ObjectiveEvaluator:
    """
    A module that runs one iteration of the variational algorithm.

    Attributes
    ----------
    executor:
        The engine on which quantum computing will be carried out.
    basis:
        The basic set of operators through which the quantum code will be constructed.
    code_builder:
        The builder of the quantum code in which the necessary ansatz is defined.
    """

    def __init__(
            self,
            executor: QuantumCodeExecutor,
            basis: QuantumCodeBasis,
            code_builder: QuantumCodeBuilder,
    ):
        if not isinstance(executor, QuantumCodeExecutor):
            raise TypeError('The engine must be an instance of QuantumCodeExecutor')
        if not isinstance(basis, QuantumCodeBasis):
            raise TypeError('The basis must be an instance of QuantumCodeBasis')
        if not isinstance(code_builder, QuantumCodeBuilder):
            raise TypeError('The code_builder must be an instance of QuantumCodeBuilder')
        self.executor = executor
        self.basis = basis
        self.code_builder = code_builder

    def evaluate(
            self,
            parameters: VariationalParameters,
            objective: ProblemStatement
    ) -> ObjectiveEvaluationResult:
        """
        Evaluates the objective function for the specified variational parameters.

        The method constructs a quantum circuit, executes it on the configured
        quantum engine, and computes the objective value from the measurement
        results.

        Args:
            parameters: The variational parameters used to construct the quantum
                circuit.
            objective: The optimization problem to be encoded into the quantum
                circuit.

        Returns:
            An ``ObjectiveEvaluationResult`` object containing the measurement
            results and the evaluated objective value.
        """
        quantum_code = self.code_builder.build(self.basis, parameters, objective)
        return self.executor.execute(quantum_code)
