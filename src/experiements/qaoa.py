from src.experiements.experiment import Experiment
from src.experiements.experiment_result import ExperimentResult

from src.core.initialization.initializer import Initializer
from src.core.quantum_code.objective_evaluator import ObjectiveEvaluator
from src.core.quantum_code.quantum_code_basis import QuantumCodeBasis
from src.core.quantum_code.quantum_code_compression import QuantumCodeCompression
from src.core.quantum_code.quantum_code_builder import QuantumCodeBuilder
from src.core.engine.quantum_code_executor import QuantumCodeExecutor

from src.core.optimization.optimizer_factory import OptimizerFactory
from src.core.optimization.variational_parameters_builder import VariationalParameterBuilder
from src.core.optimization.optimizers_list import Optimizers
from src.core.optimization.optimizer import Optimizer

from src.core.input.qubo import QUBO


# TODO: Оптимизировать реализацию класса QAOA. Сейчас реализация очень громоздкая.
class QAOA(Experiment):
    """
    Implementation of the original QAOA algorithm.

    Attributes
    ----------
    engine : QuantumCodeExecutor
        The quantum execution backend used to run quantum circuits and obtain
        measurement results.
    basis : QuantumCodeBasis
        The quantum code basis defining the gate set and circuit structure used
        to construct QAOA circuits.
    compressor : QuantumCodeCompression
        The module responsible for optimizing the generated quantum circuits by
        reducing their depth and gate count.
    initializer : Initializer
        The module responsible for generating the initial values of the
        variational parameters.
    parameters_builder : VariationalParameterBuilder
        The module that converts the optimizer parameter vector into
        ``VariationalParameters`` used by the QAOA circuit.
    objective_evaluator : ObjectiveEvaluator
        The target function to be optimized.
    optimizer : Optimizers
        The title of the optimizer.
    optimizer_engine: Optimizer
        The module responsible for optimizing the variational parameters.
    max_iterations : int
        The maximum number of optimization iterations.
    epsilon : float
        The convergence tolerance used as the stopping criterion for the
        optimization algorithm.
    """

    # TODO: добавить реализацию сжатия.
    def __init__(
            self,
            engine: QuantumCodeExecutor,
            basis: QuantumCodeBasis,
            code_builder: QuantumCodeBuilder,
            compressor: object,
            initializer: Initializer,
            parameters_builder: VariationalParameterBuilder,
            optimizer: Optimizers,
            max_iterations: int,
            epsilon: float
    ):
        if not isinstance(engine, QuantumCodeExecutor):
            raise TypeError("Engine must be an instance of QuantumCodeExecutor.")
        if not isinstance(basis, QuantumCodeBasis):
            raise TypeError("Basis must be an instance of QuantumCodeBasis.")
        if not isinstance(code_builder, QuantumCodeBuilder):
            raise TypeError("Code builder must be an instance of QuantumCodeBuilder.")
        # if not isinstance(compressor, QuantumCodeCompression):
        #     raise TypeError("Compressor must be an instance of QuantumCodeCompression.")
        if not isinstance(initializer, Initializer):
            raise TypeError("Initializer must be an instance of Initializer.")
        if not isinstance(parameters_builder, VariationalParameterBuilder):
            raise TypeError("Parameters builder must be an instance of VariationalParameterBuilder.")
        if not isinstance(max_iterations, int):
            raise TypeError("Maximum number of iterations must be an integer.")
        if not isinstance(epsilon, float):
            raise TypeError("Epsilon must be an float.")
        self.engine = engine
        self.basis = basis
        self.code_builder = code_builder
        self.compressor = compressor
        self.initializer = initializer
        self.parameters_builder = parameters_builder
        self.max_iterations = max_iterations
        self.epsilon = epsilon
        self.objective_evaluator = ObjectiveEvaluator(engine, basis, code_builder, compressor)
        self.optimizer = optimizer
        self.optimizer_engine = OptimizerFactory.create(
            optimizer,
            self.objective_evaluator,
            initializer,
            parameters_builder,
            max_iterations,
            epsilon
        )

    def run(self, qubo: QUBO, p: int) -> ExperimentResult:
        """
        Runs the QAOA experiment for the specified optimization problem.

        The method initializes the variational parameters, constructs and
        optimizes the QAOA circuit, repeatedly evaluates the objective function,
        and returns the complete results of the optimization process.

        Args:
            qubo: The QUBO optimization problem to be solved.
            p: The number of QAOA layers.

        Returns:
            An ``ExperimentResult`` object containing the optimization history,
            the optimal variational parameters, and the final objective
            evaluation.
        """
        optimizer_result = self.optimizer_engine.optimize(qubo, p)
        parameters = optimizer_result.optimal_parameters
        code = self.code_builder.build(self.basis, parameters, qubo)
        result = self.engine.execute(code)
        exp_result = ExperimentResult(
            optimization_history=[optimizer_result],
            final_measurement=result,
            final_energy=result.get_energy(qubo)
        )
        return exp_result
