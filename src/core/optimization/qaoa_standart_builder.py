import numpy as np

from src.core.optimization.variational_parameters import VariationalParameters
from variational_parameters_builder import VariationalParameterBuilder


class QAOAStandardBuilder(VariationalParameterBuilder):
    """
    A standard collector of variational parameters designed for the ordinary QAOA algorithm.
    It just generates a VariationalParameters object.
    """

    def build(self, parametrization: np.ndarray) -> VariationalParameters:
        ...