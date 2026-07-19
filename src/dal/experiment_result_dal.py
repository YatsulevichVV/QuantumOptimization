from dal import DataAccessLayer
from src.experiements.experiment_result import ExperimentResult


class ExperimentResultDAL(DataAccessLayer):
    """
    Reading and recording of experimental results.
    """

    def read(self, filename: str) -> ExperimentResult:
        ...

    def write(self, filename: str, data: ExperimentResult):
        ...
