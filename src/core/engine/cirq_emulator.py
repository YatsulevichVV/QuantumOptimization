from src.core.engine.quantum_code_executor import QuantumCodeExecutor
from src.core.quantum_code.quantum_code import QuantumCode
from src.core.output.objective_evaluation_result import ObjectiveEvaluationResult


class CirqEmulator(QuantumCodeExecutor):
    """
    The Cirq quantum computing emulator from Google.

    Attributes
    ----------
    samples:
        The number of repeated runs of the quantum code to collect statistics.
    """

    def __init__(self, samples: int):
        super().__init__(samples)

    def execute(self, code: QuantumCode) -> ObjectiveEvaluationResult:
        ...