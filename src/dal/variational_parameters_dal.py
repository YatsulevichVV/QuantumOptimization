from dal import DataAccessLayer
from src.core.optimization.variational_parameters import VariationalParameters


class VariationalParametersDAL(DataAccessLayer):
    """
    Reading and recording of variational parameters.
    """

    def read(self, filename: str) -> VariationalParameters:
        ...

    def write(self, filename: str, data: VariationalParameters):
        ...
