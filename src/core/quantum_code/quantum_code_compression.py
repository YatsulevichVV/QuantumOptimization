from abc import ABC, abstractmethod
from src.core.quantum_code.quantum_code import QuantumCode


class QuantumCodeCompression(ABC):
    """
    The module responsible for compressing the quantum code, that is,
    for reducing the number of gates and the depth of the quantum circuit
    without changing or slightly changing the resulting state.
    """

    @abstractmethod
    def compress(self, code: QuantumCode) -> QuantumCode:
        ...
