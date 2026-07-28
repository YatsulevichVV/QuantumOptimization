from enum import Enum, auto


class Optimizers(Enum):
    """
    Enumeration of the bases in which the quantum code will be assembled.
    The name of the basis corresponds to the operators used.
    """

    OnePlusOne = auto()
    COBYLA = auto()
