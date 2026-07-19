from abc import ABC, abstractmethod
from typing import Any


class DataAccessLayer(ABC):
    """
    Data access interface. Two methods will be implemented in this interface: reading and writing.
    """

    @abstractmethod
    def read(self, filename: str) -> Any:
        ...

    @abstractmethod
    def write(self, filename: str, data: Any):
        ...