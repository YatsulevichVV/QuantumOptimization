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
        if not isinstance(parameters, np.ndarray):
            raise TypeError("Parameters must be a numpy array")
        elif parameters.size == 0:
            raise ValueError("Parameters must not be empty")
        elif parameters.ndim != 1:
            raise ValueError("Parameters must have 1 dimension")
        elif not np.issubdtype(parameters.dtype, np.number):
            raise TypeError("The vector must be numeric")
        self.parameters = parameters
        self.size = parameters.size
