from src.core.engine.quantum_code_executor import QuantumCodeExecutor
from src.core.quantum_code.quantum_code import QuantumCode
from src.core.output.objective_evaluation_result import ObjectiveEvaluationResult
from cirq.contrib.qasm_import import circuit_from_qasm
from cirq import Simulator
from collections import Counter


class CirqEmulator(QuantumCodeExecutor):
    """
    The Cirq quantum computing emulator from Google.

    Attributes
    ----------
    simulator:
        The simulator used to execute the quantum code.
    repetitions:
        The number of repeated runs of the quantum code to collect statistics.
    """

    def __init__(self, repetitions: int):
        if not (isinstance(repetitions, int) and repetitions > 0):
            raise TypeError("The number of repetitions must be an positive integer.")
        self.repetitions = repetitions
        self.simulator = Simulator()

    def execute(self, quantum_code: QuantumCode) -> ObjectiveEvaluationResult:
        """
        Execute quantum code and return the evaluation result.

        The method submits and run the provided quantum code to the Cirq emulator.

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
        circuit = circuit_from_qasm(quantum_code.code)
        result = self.simulator.run(circuit, repetitions=self.repetitions)
        hist = result.multi_measurement_histogram(keys=result.measurements.keys())
        counts = {"".join(map(str, bits)): count for bits, count in hist.items()}
        objective = ObjectiveEvaluationResult(counts)
        return objective