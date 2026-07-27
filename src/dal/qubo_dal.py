from dal import DataAccessLayer
from src.core.input.qubo import QUBO
from pathlib import Path
import numpy as np
import json


class QuboDAL(DataAccessLayer):
    """
    Reading and recording of problem statement.
    """

    def read(self, filename: str) -> QUBO:
        """
        Reads an optimization problem statement from the specified file.

        Types are supported ``.txt``, ``.csv``, ``.json``.
        In the format the ``.json`` matrix should be written in the ``matrix`` field.

        Args:
            filename: Path to the file containing the problem statement.

        Returns:
            A ``QUBO`` object loaded from the file.
        """
        path = Path(filename)
        extension = path.suffix
        matrix = np.array([])
        if extension in ['.csv', '.txt']:
            matrix = np.loadtxt(filename, delimiter=",")
        elif extension in ['.json']:
            with open(path, "r") as file:
                data = json.load(file)
            matrix = np.array(data["matrix"])
        else:
            raise ValueError(f"Unsupported file extension: {extension}")
        return QUBO(matrix)

    def write(self, filename: str, data: QUBO):
        """
        Writes an optimization problem statement to the specified file.

        Types are supported ``.txt``, ``.csv``, ``.json``.
        In the format the ``.json`` matrix should be written in the ``matrix`` field.

        Args:
            filename: Path to the destination file.
            data: The ``ProblemStatement`` object to be written.
        """
        path = Path(filename)
        extension = path.suffix
        matrix = data.tensor
        if extension in ['.csv', '.txt']:
            np.savetxt(filename, matrix, delimiter=",")
        elif extension in ['.json']:
            content = {
                "matrix": matrix.tolist(),
                "n": matrix.shape[0]
            }
            with open(path, "w") as file:
                json.dump(content, file)
        else:
            raise ValueError(f"Unsupported file extension: {extension}")
