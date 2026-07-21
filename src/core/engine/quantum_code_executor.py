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
        """
        Execute quantum code and return the evaluation result.

        The method submits the provided quantum code to the execution
        backend (physical quantum processor or simulator), performs the
        required measurements, and converts the obtained results into an
        objective evaluation.

        Parameters
        ----------
        code : QuantumCode
            Quantum program represented in QASM format together with its
            execution context and metadata.

        Returns
        -------
        ObjectiveEvaluationResult
            Result of the quantum execution containing measurement outcomes.
        """
        pass

