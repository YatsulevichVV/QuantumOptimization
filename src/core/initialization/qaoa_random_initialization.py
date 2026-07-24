from src.core.initialization.initializer import Initializer
from src.core.optimization.variational_parameters import VariationalParameters
import numpy as np


class QAOARandomInitializer(Initializer):
    """
    Random initialization of gamma_i and beta_i parameter values for the QAOA algorithm.

    Attributes
    ----------
    seed:
        An integer that affects the generation of parameter values.
    """

    def __init__(self, seed: int):
        if not isinstance(seed, int):
            raise TypeError("The seed should be an integer.")
        self.seed = seed

    def initialize(self, p: int) -> VariationalParameters:
        """
        Generates random initial values for the variational parameters.

        Args:
            p: The number of iterations in the QAOA algorithm

        Returns:
            A ``VariationalParameters`` object containing randomly generated
            initial values.
        """
        gamma = np.random.uniform(low=0.0, high=2*np.pi, size=p)
        beta = np.random.uniform(low=0.0, high=np.pi, size=p)
        params = np.concatenate((gamma, beta))
        return VariationalParameters(params)

