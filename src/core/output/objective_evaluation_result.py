from src.core.input.problem_statement import ProblemStatement
import numpy as np


class ObjectiveEvaluationResult:
    """
    The result of one iteration of the variational algorithm.

    Attributes
    ----------
    result : dict[str, int]
        Statistics of a single iteration of a quantum computer or emulator,
        where the dictionary key is a bit string,
        and the value is the number of measurements of a given string.
    total_count: int
        Total number of measurements.
    """

    def __init__(self, result: dict[str, int]):
        if not isinstance(result, dict):
            raise TypeError("Result must be a dictionary")
        if not result:
            raise ValueError("Dictionary is empty")
        for state, count in result.items():
            if not isinstance(state, str): raise TypeError("All keys must be strings")
            if not isinstance(count, int): raise TypeError("All keys must be integers")
            if not set(state).issubset({"0", "1"}): raise ValueError(f"Invalid binary state: {state}")
        self.result = result
        self.total_count = sum(result.values())

    def get_energy(self, objective: ProblemStatement) -> float:
        """
        Calculate the average energy from measurement results.

        The energy is computed as the weighted average over all measured
        binary states:

            E = Σ_i n_i * E(x_i) / Σ_i n_i

        where:
            x_i is a measured binary state,

            E(x_i) is the objective function value of the state,

            n_i is the number of occurrences of the state.

        Args:
            objective: Description of a binary optimization problem in tensor form.
        Returns:
            float: Average energy of the measured states.
        """
        energy = 0
        for state, count in self.result.items():
            energy += count * objective.energy(np.array([int(bit) for bit in state]))
        return energy / self.total_count
