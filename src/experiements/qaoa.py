from experiment import Experiment
from src.core.optimization.optimizer import Optimizer
from src.experiements.experiment_result import ExperimentResult


class QAOA(Experiment):
    """
    Implementation of the original QAOA algorithm.

    Attributes
    ----------
    optimizer : Optimizer
        An optimization algorithm for selecting the values of the variation parameters of the QAOA algorithm.
    """

    def __init__(self, optimizer: Optimizer):
        ...

    def run(self) -> ExperimentResult:
        ...
