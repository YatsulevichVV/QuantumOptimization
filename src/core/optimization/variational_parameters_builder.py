from abc import ABC, abstractmethod
from variational_parameters import VariationalParameters
import numpy as np


class VariationalParameterBuilder(ABC):
    """
    The module responsible for constructing the values of variational parameters based on some parameterization.
    Parameterizations can be different. This can be a standard identical assembly,
    a construction based on the physical principle of quantum annealing or on the Fourier transform.
    """

    @abstractmethod
    def build(self, parametrization: np.ndarray) -> VariationalParameters:
        ...