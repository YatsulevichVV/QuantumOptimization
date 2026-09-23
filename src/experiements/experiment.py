from abc import ABC, abstractmethod

from core.output.objective_evaluation_result import ObjectiveEvaluationResult
from src.experiements.experiment_result import ExperimentResult


class Experiment(ABC):
    """
    The experiment is a full-fledged launch of a variational quantum algorithm. These include any VQA algorithms,
    the standard QAOA algorithm, the recursive QAOA algorithm, and others.
    """

    def __init__(self):
        pass

    @abstractmethod
    def optimize(self, *args) -> ExperimentResult:
        """
        Executes the variational quantum algorithm experiment.

        This method performs a complete experiment, including all stages required
        by the specific algorithm implementation, such as parameter initialization,
        iterative optimization, quantum circuit evaluation, and result collection.

        Returns:
            An ``ExperimentResult`` object containing the outcomes of the
            experiment, including the optimization history and the final solution.
        """
        pass

    @abstractmethod
    def run(self, *args) -> ObjectiveEvaluationResult:
        """
        Executes the configured variational quantum algorithm and evaluates
        the objective function based on the obtained measurement results.

        Args:
            *args: Arguments required to configure and execute the algorithm.

        Returns:
            ObjectiveEvaluationResult: Result of the algorithm execution,
                including the measurement results and the evaluated objective
                value.
        """
        pass
