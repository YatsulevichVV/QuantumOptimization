from experiment import Experiment
from src.core.optimization.optimizer import Optimizer
from src.experiements.experiment_result import ExperimentResult


class NeuralNetworkQAOA(Experiment):
    """
    Implementation of the QAOA algorithm with initialization of
    variational parameter values using a trained neural network model.

    Attributes
    ----------
    optimizer : Optimizer
        An optimization algorithm for selecting the values of the variation parameters of the QAOA algorithm.
    """

    def __init__(self, optimizer: Optimizer):
        ...

    def run(self) -> ExperimentResult:
        ...
