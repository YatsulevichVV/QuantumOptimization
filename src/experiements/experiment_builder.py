import numpy as np
import random

from src.core.engine.quantum_code_executor import QuantumCodeExecutor
from src.core.initialization.initializer import Initializer
from src.core.optimization.cobyla_opimizer import COBYLAOptimizer
from src.core.optimization.optimizer import Optimizer
from src.core.optimization.qaoa_standart_builder import QAOAStandardBuilder
from src.core.optimization.variational_parameters_builder import VariationalParameterBuilder
from src.core.quantum_code.quantum_code_basis import QuantumCodeBasis
from src.core.quantum_code.qaoa_ansatz_builder import QAOAAnsatzBuilder
from src.core.quantum_code.quantum_code import QuantumCode
from src.core.quantum_code.quantum_code_builder import QuantumCodeBuilder
from src.experiements.experiment import Experiment
from src.utils.logger import get_logger
from src.core.input.qubo import QUBO
from src.core.engine.cirq_emulator import CirqEmulator
from src.core.initialization.qaoa_random_initialization import QAOARandomInitializer
from src.core.quantum_code.objective_evaluator import ObjectiveEvaluator
from src.core.optimization.variational_parameters import VariationalParameters
from src.core.optimization.one_plus_one_optimizer import OnePlusOneOptimizer
from src.core.optimization.optimizers_list import Optimizers
from src.experiements.qaoa import QAOA

class ExperimentBuilder:
    """
    Factory for constructing experiment instances from a configuration.

    The builder maps string identifiers specified in the configuration to
    concrete implementations of experiment components, such as quantum
    execution engines, ansatz builders, optimizers, parameter initializers,
    and quantum code bases. This allows experiment configurations to be
    defined externally (e.g., in JSON files) without modifying the source
    code.
    """

    experiment_map: dict[str, type[Experiment]] = {
        "qaoa": QAOA,
    }
    engine_map: dict[str, type[QuantumCodeExecutor]] = {
        "cirq": CirqEmulator,
    }
    optimizer_map: dict[str, type[Optimizers]] = {
        "one_plus_one": Optimizers.OnePlusOne,
        "cobyla": Optimizers.COBYLA,
    }
    initializer_map: dict[str, type[Initializer]] = {
        "random_initialization_qaoa": QAOARandomInitializer,
    }
    code_builder_map: dict[str, type[QuantumCodeBuilder]] = {
        "standard_qaoa": QAOAAnsatzBuilder,
    }
    parameter_builder_map: dict[str, type[VariationalParameterBuilder]] = {
        "identety_variational_parameters": QAOAStandardBuilder,
    }
    compressor_map: dict[str, type[QuantumCodeExecutor]] = {}
    basis_map: dict[str, QuantumCodeBasis] = {
        "rz_cnot": QuantumCodeBasis.RZ_CNOT,
    }

    def build(self, config: dict[str, str]) -> Experiment:
        """
        Builds and configures an experiment from the provided configuration.

        The method parses the configuration, instantiates all required
        experiment components, and assembles them into a ready-to-run
        `Experiment` object.

        Parameters
        ----------
        config : dict[str, str]
            Dictionary containing the experiment configuration. The values
            specify the implementations and parameters of the experiment
            components.

        Returns
        -------
        Experiment
            A fully configured experiment instance.
        """
        # TODO: доработать систему аргументов
        if not isinstance(config, dict):
            raise TypeError('Configuration must be a dictionary.')
        engine = self.engine_map[config['engine']['type']](config['engine']['number_shots'])
        basis = self.basis_map[config['basis']]
        code_builder = self.code_builder_map[config['code_builder']]()
        compressor = None
        initializer = self.initializer_map[config['initializer']['type']](config['initializer']['seed'])
        parameters_builder = self.parameter_builder_map[config['parameters_builder']]()
        optimizer = self.optimizer_map[config['optimizer']]
        max_iterations = int(config['max_iteration'])
        epsilon = float(config['epsilon'])
        return self.experiment_map[config['experiment']](
            engine,
            basis,
            code_builder,
            compressor,
            initializer,
            parameters_builder,
            optimizer,
            max_iterations,
            epsilon,
        )
