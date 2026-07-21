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

    # TODO: Не очень понятно, стоит ли хранить дополнительную информацию и как лучше.
    def __init__(
            self,
            code: str,
            depth: int,
            gate_count: int,
            qubits_number: int
    ):
        if not isinstance(code, str):
            raise TypeError('The code must be a string.')
        # TODO: Возможно здесь нужен будет синтаксический анализатор
        if code == '':
            raise ValueError('The code must not be an empty string.')
        if not (isinstance(depth, int) and depth > 0):
            raise TypeError('The depth must be an positive integer.')
        if not (isinstance(gate_count, int) and gate_count > 0):
            raise TypeError('The gate_count must be an positive integer.')
        if not (isinstance(qubits_number, int) and qubits_number > 0):
            raise TypeError('The qubits_number must be an positive integer.')
        self.code = code
        self.depth = depth
        self.gate_count = gate_count
        self.qubits_number = qubits_number
