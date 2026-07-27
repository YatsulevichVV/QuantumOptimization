from abc import ABC, abstractmethod
from typing import Any
from pathlib import Path


class DataAccessLayer(ABC):
    """
    Data access interface. Two methods will be implemented in this interface: reading and writing.
    """

    @abstractmethod
    def read(self, filename: str) -> Any:
        """
        Reads data from the specified file.

        Args:
            filename: Path to the file containing the data.

        Returns:
            The object loaded from the file. The exact type depends on the
            implementation of the data access layer.
        """
        if not isinstance(filename, str):
            raise TypeError("The filename must be a string.")
        path = Path(filename)
        if not path.is_file():
            raise FileNotFoundError(f"File '{filename}' does not exist.")
        pass

    @abstractmethod
    def write(self, filename: str, data: Any):
        """
        Writes data to the specified file.

        Args:
            filename: Path to the destination file.
            data: The object to be written. The supported type depends on the
                implementation of the data access layer.
        """
        if not isinstance(filename, str):
            raise TypeError("The filename must be a string.")
        path = Path(filename)
        if not path.is_file():
            raise FileNotFoundError(f"File '{filename}' does not exist.")
        pass
