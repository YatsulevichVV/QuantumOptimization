from objective_evaluation_result import ObjectiveEvaluationResult
from src.core.optimization.variational_parameters import VariationalParameters


class OptimizationResult:
    """
    The result of an iterative optimization algorithm

    Attributes
    ----------
    measurements: list[ObjectiveEvaluationResult]
        The list of the results of the runs at each iteration of the optimization algorithm.
    iteration_count: int
        The number of iterations of the optimization algorithm.
    optimal_parameters: VariationalParameters
        Optimal values of the VQA variational parameters.
    problem_solution: list[int]
        The solution of the optimization problem.
    """

    def __init__(
            self,
            measurements: list[ObjectiveEvaluationResult],
            iteration_count: int,
            optimal_parameters: VariationalParameters,
            problem_solution: list[int]
    ): ...
