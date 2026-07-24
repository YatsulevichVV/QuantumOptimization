import numpy as np
from src.core.optimization.variational_parameters import VariationalParameters
from src.core.optimization.variational_parameters_builder import VariationalParameterBuilder


class QAOAStandardBuilder(VariationalParameterBuilder):
    """
    A standard collector of variational parameters designed for the ordinary QAOA algorithm.
    It just generates a VariationalParameters object.
    """

    def build(self, parametrization: np.ndarray) -> VariationalParameters:
        """
        Constructs a complete set of variational parameters from the given parameterization.
        For standard parameterization, it represents a call to the constructor of the ``VariationalParameters`` object.

        Args:
            parametrization: A NumPy array ``np.ndarray`` containing the values of the optimization variables
                according to the selected parameterization.

        Returns:
            A ``VariationalParameters`` object containing the variational parameters
            ready to be used for quantum circuit construction.
        """
        return VariationalParameters(parametrization)