from abc import ABC, abstractmethod
import numpy as np


class ProblemStatement(ABC):
    """
    Description of discrete optimization problem.

    Attributes
    ----------
    tensor : np.ndarray
        A tensor in which a discrete optimization problem is encoded.
    """

    def __init__(self, tensor: np.ndarray):
        if not isinstance(tensor, np.ndarray):
            raise TypeError(f"Tensor must be numpy.ndarray, got {type(tensor).__name__}")
        if tensor.size == 0:
            raise ValueError("Tensor must not be empty")
        self.tensor = tensor

    @abstractmethod
    def grid_search_min(self) -> float:
        pass

    @abstractmethod
    def grid_search_max(self) -> float:
        pass

    @abstractmethod
    def energy(self, x: np.ndarray) -> float:
        pass
