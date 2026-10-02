from abc import ABC, abstractmethod

from core.input.problem_statement import ProblemStatement
from src.core.optimization.variational_parameters import VariationalParameters


class Initializer(ABC):
    """
    The module that is responsible for initializing the values of the variational parameters.
    """

    def __init__(self, config: dict):
        pass

    @abstractmethod
    def initialize(self, config: dict, tensor: ProblemStatement) -> VariationalParameters:
        """
        Initializes the variational parameters.

        Args:
            config: Experiment configuration.
            tensor: The tensor in which the optimization problem is encoded.

        Returns:
            A ``VariationalParameters`` object containing the initial values
            of the variational parameters.
        """
        pass