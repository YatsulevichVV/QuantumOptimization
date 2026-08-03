from dal import DataAccessLayer
from src.experiements.experiment_result import ExperimentResult


class ExperimentResultDAL(DataAccessLayer):
    """
    Reading and recording of experimental results.
    """

    # TODO: продумать смысл этого класса. Где будут рисоваться графики? Возможно здесь.
    @staticmethod
    def read(filename: str) -> ExperimentResult:
        ...

    @staticmethod
    def write(filename: str, data: ExperimentResult):
        ...
