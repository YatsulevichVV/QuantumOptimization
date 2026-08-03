import json
from src.dal.dal import DataAccessLayer
from src.core.quantum_code.quantum_code import QuantumCode
from pathlib import Path


class ExperimentConfigDAL(DataAccessLayer):
    """
    Reading and recording of experimental configurations.
    """

    @staticmethod
    def read(filename: str) -> dict[str, str]:
        """
        Reads an experiment configuration from a file.

        The configuration is returned as a dictionary containing
        parameter names and their corresponding values.

        Args:
            filename: Path to the configuration file.

        Returns:
            A dictionary mapping configuration parameter names to
            their string values.
        """
        path = Path(filename)
        extension = path.suffix
        configuration = {}
        if extension in ['.json']:
            with open(path, "r") as file:
                data = json.load(file)
            configuration = data
        else:
            raise ValueError(f"Unsupported file extension: {extension}")
        return configuration

    @staticmethod
    def write(filename: str, configuration: dict[str, str]):
        """
        Writes an experiment configuration to a file.

        The provided dictionary is serialized and stored in the specified
        configuration file.

        Args:
            filename: Path to the output configuration file.
            configuration: Dictionary containing configuration parameter names
                and their string values.
        """
        path = Path(filename)
        extension = path.suffix
        if extension in ['.json']:
            with open(path, "w") as file:
                json.dump(configuration, file)
        else:
            raise ValueError(f"Unsupported file extension: {extension}")