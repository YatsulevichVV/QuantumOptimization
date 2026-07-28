from src.core.initialization.initializer import Initializer
from src.core.quantum_code.objective_evaluator import ObjectiveEvaluator
from src.core.optimization.variational_parameters_builder import VariationalParameterBuilder
from src.core.optimization.optimizers_list import Optimizers
from src.core.optimization.optimizer import Optimizer
from src.core.optimization.one_plus_one_optimizer import OnePlusOneOptimizer
from src.core.optimization.cobyla_opimizer import COBYLAOptimizer


class OptimizerFactory:
    """
    Factory responsible for creating optimizer instances.
    """

    @staticmethod
    def create(
            optimizer: Optimizers,
            objective: ObjectiveEvaluator,
            initializer: Initializer,
            parameters_builder: VariationalParameterBuilder,
            max_iterations: int,
            epsilon: float
    ) -> Optimizer:
        """
        Creates an optimizer instance based on the specified optimization algorithm.

        The method acts as a factory for creating concrete implementations of the
        ``Optimizer`` interface. It selects the corresponding optimizer class based
        on the provided ``Optimizers`` enumeration value and initializes it with
        the required optimization components.

        Args:
            optimizer: The type of optimization algorithm to be created.
            objective: The objective evaluator used to calculate the optimization
                function value.
            initializer: The module responsible for generating initial variational
                parameters.
            parameters_builder: The module responsible for converting optimizer
                parameters into variational parameters.
            max_iterations: The maximum number of optimization iterations.
            epsilon: The convergence tolerance used as a stopping criterion.

        Returns:
            An instance of the selected optimizer implementation.
        """
        if optimizer == Optimizers.OnePlusOne:
            return OnePlusOneOptimizer(
                objective,
                initializer,
                parameters_builder,
                max_iterations,
                epsilon
            )
        if optimizer == Optimizers.COBYLA:
            return COBYLAOptimizer(
                objective,
                initializer,
                parameters_builder,
                max_iterations,
                epsilon
            )
        raise ValueError(f"Unsupported optimizer: {optimizer}")
