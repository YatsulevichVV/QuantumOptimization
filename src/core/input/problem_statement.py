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
        ...

    @abstractmethod
    def grid_search_min(self) -> float:
        pass

    @abstractmethod
    def grid_search_max(self) -> float:
        pass
