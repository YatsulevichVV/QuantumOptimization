from src.dal.dal import DataAccessLayer
from src.core.input.problem_statement import ProblemStatement
from src.core.input.qubo import QUBO
from pathlib import Path
import numpy as np
import json


class ProblemStatementDAL(DataAccessLayer):
    """
    Reading and recording of problem statement.
    """

    @staticmethod
    def read(filename: str) -> ProblemStatement:
        """
        Reads an optimization problem statement from the specified file.

        Types are supported ``.json``.
        In the format the ``.json`` matrix should be written in the ``tensor`` field.

        Args:
            filename: Path to the file containing the problem statement.

        Returns:
            A ``QUBO`` object loaded from the file.
        """
        path = Path(filename)
        extension = path.suffix
        # if extension in ['.csv', '.txt']:
        #     matrix = np.loadtxt(filename, delimiter=",")
        if extension in ['.json']:
            with open(path, "r") as file:
                data = json.load(file)
            tensor = np.array(data["tensor"])
            tensor_type = data["type"]
        else:
            raise ValueError(f"Unsupported file extension: {extension}")
        if tensor_type == "QUBO":
            return QUBO(tensor)
        else:
            raise ValueError(f"Unsupported type of tensor: {tensor_type}")

    @staticmethod
    def write(filename: str, data: ProblemStatement):
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
        # if extension in ['.csv', '.txt']:
        #     np.savetxt(filename, matrix, delimiter=",")
        if extension in ['.json']:
            content = {
                "tensor": matrix.tolist(),
            }
            if isinstance(data, QUBO):
                content["type"] = "QUBO"
            else:
                raise ValueError(f"Unsupported type of tensor: {data.__class__.__name__}")
            with open(path, "w") as file:
                json.dump(content, file)
        else:
            raise ValueError(f"Unsupported file extension: {extension}")
