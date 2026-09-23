from src.core.engine.quantum_code_executor import QuantumCodeExecutor
from src.core.quantum_code.quantum_code import QuantumCode
from src.core.output.objective_evaluation_result import ObjectiveEvaluationResult
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


class QiskitEmulator(QuantumCodeExecutor):
    """
    The Qiskit quantum computing emulator by IBM.

    Attributes
    ----------
    simulator:
        The simulator used to execute the quantum code.
    repetitions:
        The number of repeated runs of the quantum code to collect statistics.
    """

    def __init__(self, repetitions: int):
        super().__init__()
        if not (isinstance(repetitions, int) and repetitions > 0):
            raise TypeError("The number of repetitions must be an positive integer.")
        self.repetitions = repetitions
        self.simulator = AerSimulator()

    def execute(self, quantum_code: QuantumCode) -> ObjectiveEvaluationResult:
        """
        Execute quantum code and return the evaluation result.

        The method submits and run the provided quantum code to the AerSimulator emulator.

        Parameters
        ----------
        quantum_code: QuantumCode
            Quantum program represented in QASM format together with its
            execution context and metadata.

        Returns
        -------
        ObjectiveEvaluationResult
            Result of the quantum execution containing measurement outcomes.
        """
        circuit = QuantumCircuit.from_qasm_str(quantum_code.code)
        result = self.simulator.run(circuit, shots=self.repetitions).result()
        counts = result.get_counts(circuit)
        answer = {
            bitstring.replace(" ", ""): count
            for bitstring, count in counts.items()
        }
        objective = ObjectiveEvaluationResult(answer)
        return objective
