from cmd import Cmd
import numpy as np
from src.utils.logger import get_logger
from src.dal.experiment_config import ExperimentConfigDAL
from src.dal.qubo_dal import QuboDAL
from src.experiements.experiment_builder import ExperimentBuilder
from src.core.input.qubo import QUBO


logger = get_logger(__name__)

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
        self.tensor = None
        self.config = None

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
            self.stdout.write('Configuration has been successfully initialized.\n')
            logger.info('Configuration has been successfully initialized.')
        except Exception as e:
            self.stdout.write(str(e) + '\n')
            logger.exception(e)
            pass

    def do_input(self, arg: str):
        """
        Load optimization problem from a file.

        The command expects a path to a file containing a optimization problem.
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
            # TODO: Жёсткая привязка к матрице QUBO, такого быть не должно. Возможно нужно будет менять архитектуру DAL.
            self.tensor = QuboDAL.read(filename)
            self.stdout.write('Optimization problem has been successfully initialized.\n')
            logger.info('Optimization problem has been successfully initialized.')
        except Exception as e:
            self.stdout.write(str(e) + '\n')
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
                self.stdout.write('Optimization problem has not been initialized.\n')
            else:
                self.stdout.write(str(self.tensor) + '\n')
            if self.config is None:
                self.stdout.write('Configuration has not been initialized.\n')
            else:
                self.stdout.write(str(self.config) + '\n')
        except Exception as e:
            self.stdout.write(str(e) + '\n')
            logger.exception(e)
            pass

    def do_run(self, arg: str):
        """
        Execute the quantum optimization experiment.

        Builds a QAOA experiment using the loaded configuration, runs the
        optimization process on the initialized QUBO problem, and selects
        the best solution from the obtained results. The optimal binary
        solution and its corresponding energy value are written to the log.

        The command requires that both the QUBO matrix and experiment
        configuration have been initialized beforehand.

        Example:
            quant-optimizer> run
        """
        try:
            logger.info(f'quant-optimizer> run {arg}')
            qaoa = ExperimentBuilder().build(self.config)
            # TODO: Величина p не должна добавляться здесь
            p = self.config['experiment']['layers']
            result = qaoa.run(self.tensor, p)
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
            self.stdout.write(f'The solution of the optimization problem: {answer} with energy {min_energy}.\n')
        except Exception as e:
            self.stdout.write(str(e) + '\n')
            logger.exception(e)
            pass

    def do_exit(self, arg):
        logger.info(f'quant-optimizer> exit')
        """
        Exit the interactive console.

        Example:
            quant-optimizer> exit
        """
        return True
