from abc import ABC, abstractmethod
from src.core.optimization.variational_parameters import VariationalParameters
import numpy as np


class VariationalParameterBuilder(ABC):
    """
    The module responsible for constructing the values of variational parameters based on some parameterization.
    Parameterization can be different. This can be a standard identical assembly,
    a construction based on the physical principle of quantum annealing or on the Fourier transform.
    """

    @abstractmethod
    def build(self, parametrization: np.ndarray) -> VariationalParameters:
        """
        Constructs a complete set of variational parameters from the given parameterization.

        Args:
            parametrization: A NumPy array ``np.ndarray`` containing the values of the optimization variables
                according to the selected parameterization.

        Returns:
            A ``VariationalParameters`` object containing the variational parameters
            ready to be used for quantum circuit construction.
        """
        pass