from quantum_code_compression import QuantumCodeCompression
from src.core.quantum_code.quantum_code import QuantumCode


class QiskitCompression(QuantumCodeCompression):
    """
    An algorithm for compressing quantum code from the Qiskit library from IBM.
    The algorithm has 3 compression levels.

    Attributes
    ----------
    compression_rate:
        The level or degree of compression of the quantum code. You can select values 1, 2, or 3.
    """

    def __init__(self, compression_rate: int):
        ...

    def compress(self, code: QuantumCode) -> QuantumCode:
        ...