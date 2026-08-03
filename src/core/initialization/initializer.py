from abc import ABC, abstractmethod
from src.core.optimization.variational_parameters import VariationalParameters


class Initializer(ABC):
    """
    The module that is responsible for initializing the values of the variational parameters.
    """

    def __init__(self, *args):
        pass

    @abstractmethod
    def initialize(self, size: int) -> VariationalParameters:
        """
        Initializes the variational parameters.

        Args:
            size: The count of the variational parameters.

        Returns:
            A ``VariationalParameters`` object containing the initial values
            of the variational parameters.
        """
        pass