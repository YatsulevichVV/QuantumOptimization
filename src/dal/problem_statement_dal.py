from dal import DataAccessLayer
from src.core.input.problem_statement import ProblemStatement


class ProblemStatementDAL(DataAccessLayer):
    """
    Reading and recording of problem statement.
    """

    def read(self, filename: str) -> ProblemStatement:
        ...

    def write(self, filename: str, data: ProblemStatement):
        ...
