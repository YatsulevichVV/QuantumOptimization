from dal import DataAccessLayer
from src.core.quantum_code.quantum_code import QuantumCode
from pathlib import Path


class QuantumCodeDAL(DataAccessLayer):
    """
    Reading and recording of quantum code in QASM format.
    """

    def read(self, filename: str) -> QuantumCode:
        """
        Reads quantum code in QASM format from the specified file.

        Types are supported ``.txt``, ``.qasm``.

        Args:
            filename: Path to the file containing the quantum code.

        Returns:
            A ``QuantumCode`` object constructed from the QASM code loaded
            from the file.
        """
        path = Path(filename)
        extension = path.suffix
        if extension in ['.txt', 'qasm']:
            with open(path, "r") as file:
                data = file.read()
        else:
            raise ValueError(f"Unsupported file extension: {extension}")
        return QuantumCode(data)

    def write(self, filename: str, data: QuantumCode):
        """
        Writes quantum code in QASM format to the specified file.

        Types are supported ``.txt``, ``.qasm``.

        Args:
            filename: Path to the destination file.
            data: The ``QuantumCode`` object containing the QASM code to be
                written.
        """
        path = Path(filename)
        extension = path.suffix
        if extension in ['.txt', 'qasm']:
            with open(path, "w") as file:
                file.write(data.code)
        else:
            raise ValueError(f"Unsupported file extension: {extension}")
