from abc import ABC, abstractmethod
from src.core.quantum_code.quantum_code import QuantumCode
from src.core.output.objective_evaluation_result import ObjectiveEvaluationResult


class QuantumCodeExecutor(ABC):
    """
    The engine that will run the quantum code in the QASM language.
    It can be either a physical quantum computer or an emulator.
    """

    @abstractmethod
    def execute(self, code: QuantumCode) -> ObjectiveEvaluationResult:
        ...

