from problem_statement import ProblemStatement
import numpy as np

class QUBO(ProblemStatement):
    """
    Quantum Unconstrained Binary Optimization (QUBO) matrix.

    Attributes
    ----------
    tensor : np.ndarray
        QUBO matrix.
    size: int
        Size of the QUBO matrix.
    """

    def __init__(self, tensor: np.ndarray):
        super().__init__(tensor)
        ...

    def grid_search_max(self) -> float:
        ...

    def grid_search_min(self) -> float:
        ...

    def energy(self, x: np.ndarray) -> float:
        ...

