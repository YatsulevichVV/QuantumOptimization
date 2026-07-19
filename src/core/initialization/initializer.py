from abc import ABC, abstractmethod
from src.core.optimization.variational_parameters import VariationalParameters


class Initializer(ABC):
    """
    The module that is responsible for initializing the values of the variational parameters.
    """

    @abstractmethod
    def initialize(self) -> VariationalParameters:
        ...