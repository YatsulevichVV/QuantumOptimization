from src.core.input.problem_statement import ProblemStatement
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
        if tensor.ndim != 2:
            raise TypeError("The tensor is not a matrix")
        if tensor.shape[0] != tensor.shape[1]:
            raise ValueError("The matrix must be square")
        if not np.issubdtype(tensor.dtype, np.number):
            raise TypeError("The matrix must be numeric")
        self.tensor = (tensor + tensor.T) / 2
        self.size = tensor.shape[0]


    def grid_search_max(self) -> float:
        pass

    def grid_search_min(self) -> float:
        pass

    def energy(self, x: np.ndarray) -> float:
        """
        Evaluate the QUBO objective function.

        The objective function is:
            f(x) = x^T Q x
        where x is a binary vector.

        Args:
            x: Binary vector.

        Returns:
            float: Objective function value.
        """
        if not isinstance(x, np.ndarray):
            raise TypeError(f"Binary vector must be numpy.ndarray, got {type(x).__name__}")
        if x.ndim != 1:
            raise TypeError("The binary vector is not a vector")
        if not np.issubdtype(x.dtype, np.number):
            raise TypeError("The binary vector must be numeric")
        if self.size != len(x):
            raise ValueError("The size of the binary vector must be equal to size of the QUBO matrix")
        return float(x.T @ self.tensor @ x)
