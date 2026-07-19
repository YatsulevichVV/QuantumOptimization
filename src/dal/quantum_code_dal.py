from dal import DataAccessLayer
from src.core.quantum_code.quantum_code import QuantumCode


class QuantumCodeDAL(DataAccessLayer):
    """
    Reading and recording of quantum code in QASM format.
    """

    def read(self, filename: str) -> QuantumCode:
        ...

    def write(self, filename: str, data: QuantumCode):
        ...
