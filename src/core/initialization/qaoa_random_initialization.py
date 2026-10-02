from src.core.input.problem_statement import ProblemStatement
from src.core.initialization.initializer import Initializer
from src.core.optimization.variational_parameters import VariationalParameters
import numpy as np


class QAOARandomInitializer(Initializer):
    """
    Random initialization of gamma_i and beta_i parameter values for the QAOA algorithm.

    Attributes
    ----------
    seed:
        An integer that affects the generation of parameter values.
    """

    def __init__(self, config: dict):
        super().__init__(config)
        seed = config['initializer']['seed']
        if not isinstance(seed, int):
            raise TypeError("The seed should be an integer.")
        self.seed = seed

    def initialize(self, config: dict, tensor: ProblemStatement) -> VariationalParameters:
        """
        Generates random initial values for the variational parameters.

        Args:
            config: Experiment configuration.
            tensor: The tensor in which the optimization problem is encoded.

        Returns:
            A ``VariationalParameters`` object containing randomly generated
            initial values.
        """
        p = config['experiment']['layers']
        gamma = np.random.uniform(low=0.0, high=2*np.pi, size=p)
        beta = np.random.uniform(low=0.0, high=np.pi, size=p)
        params = np.concatenate((gamma, beta))
        return VariationalParameters(params)

