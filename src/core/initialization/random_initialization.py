from src.core.initialization.initializer import Initializer
from src.core.optimization.variational_parameters import VariationalParameters


class RandomInitializerQAOA(Initializer):
    """
    Random initialization of gamma_i and beta_i parameter values for the QAOA algorithm.

    Attributes
    ----------
    seed:
        An integer that affects the generation of parameter values.
    """

    def __init__(self, seed: int):
        ...

    def initialize(self) -> VariationalParameters:
        ...

