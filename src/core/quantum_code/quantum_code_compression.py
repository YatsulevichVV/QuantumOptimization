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
        """
        Compresses the specified quantum code.

        Applies one or more circuit optimization techniques to reduce the number
        of quantum gates and/or the circuit depth while preserving, as closely as
        possible, the behavior of the original quantum circuit.

        Args:
            code: The quantum code to be compressed.

        Returns:
            A ``QuantumCode`` object representing the compressed quantum circuit.
        """
        pass
