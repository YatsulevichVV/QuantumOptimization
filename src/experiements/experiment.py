from abc import ABC, abstractmethod
from src.experiements.experiment_result import ExperimentResult


class Experiment(ABC):
    """
    The experiment is a full-fledged launch of a variational quantum algorithm. These include any VQA algorithms,
    the standard QAOA algorithm, the recursive QAOA algorithm, and others.
    """

    @abstractmethod
    def run(self) -> ExperimentResult:
        ...
