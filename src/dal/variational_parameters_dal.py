from dal import DataAccessLayer
from src.core.optimization.variational_parameters import VariationalParameters
from pathlib import Path
import numpy as np
import json


class VariationalParametersDAL(DataAccessLayer):
    """
    Reading and recording of variational parameters.
    """

    def read(self, filename: str) -> VariationalParameters:
        """
        Reads variational parameters from the specified file.

        Types are supported ``.txt``, ``.csv``, ``.json``.
        In the format the ``.json`` matrix should be written in the ``parameters`` field.

        Args:
            filename: Path to the file containing the variational parameters.

        Returns:
            A ``VariationalParameters`` object loaded from the file.
        """
        path = Path(filename)
        extension = path.suffix
        parameters = np.array([])
        if extension in ['.csv', '.txt']:
            parameters = np.loadtxt(filename, delimiter=",")
        elif extension in ['.json']:
            with open(path, "r") as file:
                data = json.load(file)
            parameters = np.array(data["parameters"])
        else:
            raise ValueError(f"Unsupported file extension: {extension}")
        return VariationalParameters(parameters)

    def write(self, filename: str, data: VariationalParameters):
        """
        Writes variational parameters to the specified file.

        Types are supported ``.txt``, ``.csv``, ``.json``.
        In the format the ``.json`` matrix should be written in the ``parameters`` field.

        Args:
            filename: Path to the destination file.
            data: The ``VariationalParameters`` object to be written.
        """
        path = Path(filename)
        extension = path.suffix
        parameters = data.parameters
        if extension in ['.csv', '.txt']:
            np.savetxt(filename, parameters, delimiter=",")
        elif extension in ['.json']:
            content = {
                "parameters": parameters.tolist(),
            }
            with open(path, "w") as file:
                json.dump(content, file)
        else:
            raise ValueError(f"Unsupported file extension: {extension}")
