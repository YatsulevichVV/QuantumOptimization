from src.core.output.optimization_result import OptimizationResult
from src.core.output.objective_evaluation_result import ObjectiveEvaluationResult

# TODO: Нужен ли этот класс?
class ExperimentResult:
    """
    Stores the results obtained during the execution of a variational quantum
    algorithm experiment.

    The object contains the complete optimization history, the final objective
    function evaluation, and the corresponding energy value obtained after the
    optimization process. It can be used to analyze the performance of different
    experiment types, such as standard QAOA, recursive QAOA, or other VQA-based
    algorithms.

    Attributes
    ----------
    optimization_history : list[OptimizationResult]
        A list containing the results of each optimization run or iteration,
        including intermediate parameter values and objective evaluations.
    final_measurement : ObjectiveEvaluationResult
        The result of the final quantum circuit evaluation performed with the
        optimal variational parameters.
    final_energy : float
        The final value of the objective function obtained after optimization.
    """

    def __init__(
            self,
            optimization_history: list[OptimizationResult],
            final_measurement: ObjectiveEvaluationResult,
            final_energy: float
    ):
        if not isinstance(optimization_history, list):
            raise TypeError("optimization_history must be a list")
        if not isinstance(final_measurement, ObjectiveEvaluationResult):
            raise TypeError("final_measurement must be a ObjectiveEvaluationResult")
        if not isinstance(final_energy, float):
            raise TypeError("final_energy must be a float")
        self.optimization_history = optimization_history
        self.final_measurement = final_measurement
        self.final_energy = final_energy

    def make_plot(self):
        ...