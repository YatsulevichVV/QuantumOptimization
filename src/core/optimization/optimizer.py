from abc import ABC, abstractmethod
from src.core.initialization.initializer import Initializer
from src.core.output.optimization_result import OptimizationResult
from variational_parameters_builder import VariationalParameterBuilder
from src.core.initialization.initializer import Initializer
from src.core.quantum_code.objective_evaluator import ObjectiveEvaluator


class Optimizer(ABC):
    """
    An optimizer is an algorithm that starts an iterative process of selecting variational parameters.

    Attributes
    ----------
    objective: ObjectiveEvaluator
        The object that contains the objective function that needs to be optimized.
    initializer: Initializer
        Initializer of initial values of variational parameters.
    parameters_builder: VariationalParameterBuilder
        An algorithm for constructing variational parameters at each step of the iterative process.
    max_iterations: int
        Maximum number of iterations of the algorithm.
    epsilon: float
        Epsilon-area stop criterion.
    """

    def __init__(
            self,
            objective: ObjectiveEvaluator,
            initializer: Initializer,
            parameters_builder: VariationalParameterBuilder,
            max_iterations: int,
            epsilon: float
    ): ...

    @abstractmethod
    def optimize(self) -> OptimizationResult:
        ...
