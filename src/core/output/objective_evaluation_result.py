class ObjectiveEvaluationResult:
    """
    The result of one iteration of the variational algorithm.

    Attributes
    ----------
    result : dict[str, int]
        Statistics of a single iteration of a quantum computer or emulator,
        where the dictionary key is a bit string,
        and the value is the number of measurements of a given string.
    """

    def __init__(self, result: dict[str, int]):
        ...

    def get_energy(self) -> float:
        ...