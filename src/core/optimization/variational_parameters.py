import numpy as np


class VariationalParameters:
    """
    Variational parameters of the quantum iterative algorithm

    Attributes
    ----------
    parameters: np.ndarray
        The array of variational parameters
    size: int
        The count of the variational parameters
    """

    def __init__(self, parameters: np.ndarray):
        ...
