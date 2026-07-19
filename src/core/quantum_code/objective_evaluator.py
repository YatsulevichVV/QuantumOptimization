from src.core.engine.quantum_code_executor import QuantumCodeExecutor
from src.core.input.problem_statement import ProblemStatement
from src.core.optimization.variational_parameters import VariationalParameters
from src.core.output.objective_evaluation_result import ObjectiveEvaluationResult
from src.core.quantum_code.quantum_code_basis import QuantumCodeBasis
from src.core.quantum_code.quantum_code_builder import QuantumCodeBuilder


class ObjectiveEvaluator:
    """
    A module that runs one iteration of the variational algorithm.

    Attributes
    ----------
    engine:
        The engine on which quantum computing will be carried out.
    basis:
        The basic set of operators through which the quantum code will be constructed.
    code_builder:
        The builder of the quantum code in which the necessary ansatz is defined.
    """

    def __init__(
            self,
            engine: QuantumCodeExecutor,
            basis: QuantumCodeBasis,
            code_builder: QuantumCodeBuilder,
    ): ...

    def evaluate(
            self,
            parameters: VariationalParameters,
            objective: ProblemStatement
    ) -> ObjectiveEvaluationResult: ...
