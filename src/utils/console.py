from cmd2 import Cmd
import numpy as np
from src.utils.logger import get_logger
from src.dal.experiment_config import ExperimentConfigDAL
from src.dal.problem_statement_dal import ProblemStatementDAL
from src.experiements.experiment_builder import ExperimentBuilder


logger = get_logger(__name__)

# TODO: Переработать команду help
# TODO: Сделать красивый вывод у команды status
class Command(Cmd):
    """
    Interactive command-line interface for the quantum optimizer application.

    This class extends the standard Python cmd.Cmd framework and provides
    a REPL-style console for interacting with the optimization system.
    Users can execute commands for loading configuration files, running
    experiments, and controlling the application lifecycle.

    Attributes:
        prompt (str): Console prompt displayed to the user.
        tensor: Loaded optimization tensor.
        config: Loaded experiment configuration.
    """

    prompt = 'quant-optimizer> '

    def __init__(self):
        super().__init__()
        self.prompt = 'quant-optimizer> '
        self.tensor = None
        self.config = None
        self.experiment_history = None
        self.parameters = None

    def do_config(self, arg: str):
        """
        Load experiment configuration from a file.

        The command expects a path to a configuration file as an argument.

        Example:
            quant-optimizer> config experiment.json

        Args:
            arg (str): Command arguments containing the configuration file path.
        """
        try:
            logger.info(f'quant-optimizer> config {arg}')
            args = arg.split()
            filename = args[0]
            self.config = ExperimentConfigDAL.read(filename)
            self.poutput('Configuration has been successfully initialized.\n')
            logger.info('Configuration has been successfully initialized.')
        except Exception as e:
            self.poutput(str(e) + '\n')
            logger.exception(e)
            pass

    def do_input(self, arg: str):
        """
        Load optimization problem from a file.

        The command expects a path to a file containing optimization problem.
        The loaded matrix is stored in the command interface state and can
        be used in subsequent optimization operations.

        Example:
            quant-optimizer> input problem.json

        Args:
            arg (str): Command arguments containing the path to the optimization problem file.
        """
        try:
            logger.info(f'quant-optimizer> input {arg}')
            args = arg.split()
            filename = args[0]
            self.tensor = ProblemStatementDAL.read(filename)
            self.poutput('Optimization problem has been successfully initialized.\n')
            logger.info('Optimization problem has been successfully initialized.')
        except Exception as e:
            self.poutput(str(e) + '\n')
            logger.exception(e)
            pass

    def do_status(self, arg: str):
        """
        Display the current state of the optimization problem.

        Shows information about the loaded QUBO matrix and experiment
        configuration. If a required component has not been initialized,
        an appropriate message is displayed.

        Example:
            quant-optimizer> status
        """
        try:
            logger.info(f'quant-optimizer> status')
            if self.tensor is None:
                self.poutput('Optimization problem has not been initialized.\n')
            else:
                self.poutput(str(self.tensor) + '\n')
            if self.config is None:
                self.poutput('Configuration has not been initialized.\n')
            else:
                self.poutput(str(self.config) + '\n')
                self.poutput(str(self.parameters) + '\n')
        except Exception as e:
            self.poutput(str(e) + '\n')
            logger.exception(e)
            pass

    def do_run(self, arg: str):
        """
        Runs a variational quantum algorithm experiment for the given problem.

        The experiment includes construction and execution of the corresponding
        parameterized quantum circuit, optimization of its variational parameters,
        and final measurement of the resulting quantum state.

        Example:
            quant-optimizer> run
        """
        try:
            logger.info(f'quant-optimizer> run {arg}')
            experiment = ExperimentBuilder().build(self.config)
            self.parameters = self.experiment_history.optimization_history[-1].optimal_parameters
            result = experiment.run(self.tensor, self.parameters)
            top = result.get_solution(5)
            answer = ''
            min_energy = 1e10
            for x in top:
                arr = np.array(list(map(int, list(x))))
                energy = self.tensor.energy(arr)
                if energy < min_energy:
                    answer = x
                    min_energy = energy
            logger.info(f'The solution of the optimization problem: {answer} with energy {min_energy}.')
            self.poutput(f'The solution of the optimization problem: {answer} with energy {min_energy}.\n')
        except Exception as e:
            self.poutput(str(e) + '\n')
            logger.exception(e)
            pass

    def do_optimize(self, arg: str):
        """
        Execute the quantum optimization experiment.

        Builds a VQA experiment using the loaded configuration, runs the
        optimization process on the initialized optimization problem, and selects
        the best solution from the obtained results. The optimal binary
        solution and its corresponding energy value are written to the log.

        The command requires that both the optimization problem statement and experiment
        configuration have been initialized beforehand.

        Example:
            quant-optimizer> optimize
        """
        try:
            logger.info(f'quant-optimizer> optimize {arg}')
            experiment = ExperimentBuilder().build(self.config)
            layers = self.config['experiment']['layers']
            self.experiment_history = experiment.optimize(self.tensor, layers)
            logger.info(f'The values of the variation parameters have been successfully determined.')
            self.poutput(f'The values of the variation parameters have been successfully determined.\n')
        except Exception as e:
            self.poutput(str(e) + '\n')
            logger.exception(e)
            pass

    # noinspection PyMethodMayBeStatic
    def do_exit(self, arg):
        """
        Exit the interactive console.

        Example:
            quant-optimizer> exit
        """
        logger.info(f'quant-optimizer> exit')
        return True
