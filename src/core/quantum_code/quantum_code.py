class QuantumCode:
    """
    An object that stores directly executable quantum code as a string,
    as well as additional characteristics such as the number of qubits,
    the number of instructions, and the depth of the quantum circuit.

    Attributes
    ----------
    code: str
        A quantum code in the QASM language, stored in string format.
    depth: int
        The depth of the quantum circuit.
    gate_count: int
        The number of gates in the quantum circuit.
    qubits_number: int
        The number of qubits in the quantum circuit.
    """

    def __init__(
            self,
            code: str,
            depth: int,
            gate_count: int,
            qubits_number: int
    ): ...