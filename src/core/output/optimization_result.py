import numpy as np
from src.core.output.objective_evaluation_result import ObjectiveEvaluationResult
from src.core.optimization.variational_parameters import VariationalParameters
from src.core.input.problem_statement import ProblemStatement


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
    """

    def __init__(
            self,
            measurements: list[ObjectiveEvaluationResult],
            iteration_count: int,
            optimal_parameters: VariationalParameters,
    ):
        if not isinstance(measurements, list):
            raise TypeError("Measurements must be a list")
        if not all([isinstance(measurement, ObjectiveEvaluationResult) for measurement in measurements]):
            raise TypeError("Evert measurements must be a ObjectiveEvaluationResult")
        if not isinstance(iteration_count, int):
            raise TypeError("The attribute iteration_count must be a integer")
        if not isinstance(optimal_parameters, VariationalParameters):
            raise TypeError("The attribute optimal_parameters must be a VariationalParameters")
        self.measurements = measurements
        self.iteration_count = iteration_count
        self.optimal_parameters = optimal_parameters
