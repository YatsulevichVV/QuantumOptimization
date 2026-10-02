from core.input.problem_statement import ProblemStatement
from src.core.input.qubo import QUBO
from src.core.initialization.initializer import Initializer
from src.core.optimization.variational_parameters import VariationalParameters
import numpy as np
import torch
import torch.nn as nn
from pathlib import Path

PATH = Path(__file__).resolve().parents[3]
WEIGHTS = PATH / "models" / "model_p3.pt"

P = 3
MAX_V = 8
INPUT_DIM = MAX_V * (MAX_V + 1) // 2

class NNSimplePerceptronQAOA(Initializer):
    def __init__(self, config: dict):
        super().__init__(config)
        seed = config['initializer']['seed']
        if not isinstance(seed, int):
            raise TypeError("The seed should be an integer.")
        self.seed = seed

    @staticmethod
    def create_model(p=P, input_dim=INPUT_DIM):
        return nn.Sequential(
            nn.Flatten(),
            nn.Linear(input_dim, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 2 * p),
        )

    @staticmethod
    def split_params(params, p):
        return params[:, :p], params[:, p:]

    @staticmethod
    def to_input(qubo):
        """Network input: Q in the top-left corner of a zero MAX_V x MAX_V matrix,
        upper triangle with the diagonal (36 numbers for any V)"""
        V = qubo.shape[0]  # number of vertices
        if V > MAX_V:
            raise ValueError(f"The model accepts V <= {MAX_V}, got V = {V}")

        padded = np.zeros((MAX_V, MAX_V), dtype=np.float32)  # zero matrix
        padded[:V, :V] = qubo
        return torch.tensor(padded[np.triu_indices(MAX_V)]).unsqueeze(0)  # upper triangle

    def predict(self, qubo: ProblemStatement):
        """
        Predict QAOA parameters.

        Args:
            qubo: upper triangular QUBO matrix V x V

        Returns:
             (gamma, beta) as numpy arrays of length p
        """

        qubo = qubo.tensor
        model = self.create_model()
        model.load_state_dict(torch.load(WEIGHTS, map_location="cpu"))
        model.eval()
        with torch.no_grad():
            params = model(self.to_input(qubo))  # predict
        beta, gamma = self.split_params(params, P)
        return gamma[0].numpy(), beta[0].numpy()

    def initialize(self, config: dict, tensor: ProblemStatement) -> VariationalParameters:
        p = config['experiment']['layers']
        gamma, beta = self.predict(tensor)

        params = np.concatenate((gamma, beta))
        return VariationalParameters(params)