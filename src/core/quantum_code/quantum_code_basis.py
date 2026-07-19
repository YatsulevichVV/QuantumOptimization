from enum import Enum, auto


class QuantumCodeBasis(Enum):
    """
    Enumeration of the bases in which the quantum code will be assembled.
    The name of the basis corresponds to the operators used.
    """

    RZ_RZZ = auto()
    RZ_CNOT = auto()
    U3_CZ = auto()
