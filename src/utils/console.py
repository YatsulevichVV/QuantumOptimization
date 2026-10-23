from cmd2 import Cmd
import cmd2
from rich.style import Style
from rich.text import Text
import numpy as np
import argparse

from dal.variational_parameters_dal import VariationalParametersDAL
from src.utils.logger import get_logger
from src.dal.experiment_config import ExperimentConfigDAL
from src.dal.problem_statement_dal import ProblemStatementDAL
from src.experiements.experiment_builder import ExperimentBuilder


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
        self.prompt = 'quant-optimizer> '
        self.tensor = None
        self.config = None
        self.experiment_history = None
        self.parameters = None

        self.count = 0

    def do_help(self, args: argparse.Namespace):
        """Display help information for available commands.

        If a command name is provided, delegates to the standard ``cmd2``
        help implementation to display detailed help for that command.
        Otherwise, displays a custom formatted list of available commands
        and their descriptions.

        Args:
            args: Command name for which detailed help should be displayed.
                If empty, displays the list of all available commands.

        Examples:
            quant-optimizer> help
            quant-optimizer> help config
            quant-optimizer> help optimize
        """
        if args:
            super().do_help(args)
            return
        commands = {
            "config [FILE]": "Loading the configuration file.",
            "exit": "Finish working with the program.",
            "help [COMMAND]": "Show help.",
            "initialize [-f FILE | -c]": (
                "Initialize variational parameters from a file "
                "or using the current configuration."
            ),
            "input [FILE]": "Loading the optimization problem.",
            "optimize": (
                "Launching the optimization process "
                "to select the values of the variation parameters."
            ),
            "run": (
                "Launching a quantum algorithm "
                "without an optimization process."
            ),
            "status": "Display the current state of the system.",
        }
        width = max(map(len, commands.keys()))
        for command, description in commands.items():
            self.poutput(Text(f"    {command:<{width}}", style=Style(color="yellow")), end="")
            self.poutput(Text(f"    {description}"))

    def do_config(self, arg: str):
        """
        Load experiment configuration from a file.

        The command expects a path to a configuration file as an argument.

        Example:
            quant-optimizer> config experiment.json

        Args:
            arg (str): Configuration file path.
        """
        try:
            logger.info(f'quant-optimizer> config {arg}')
            args = arg.split()
            if len(args) != 1:
                self.poutput(Text("ERROR: Incorrect command input format", Style(color="red")))
                self.poutput("Usage: config <file>")
                return
            filename = args[0]
            self.config = ExperimentConfigDAL.read(filename)
            self.poutput('Configuration has been successfully initialized.')
            logger.info('Configuration has been successfully initialized.')
        except Exception as e:
            self.poutput(Text("ERROR: ", Style(color="red")), end='')
            self.poutput(str(e))
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
            if len(args) != 1:
                self.poutput(Text("ERROR: Incorrect command input format", Style(color="red")))
                self.poutput("Usage: input <file>")
                return
            filename = args[0]
            self.tensor = ProblemStatementDAL.read(filename)
            self.poutput('Optimization problem has been successfully initialized.')
            logger.info('Optimization problem has been successfully initialized.')
        except Exception as e:
            self.poutput(Text("ERROR: ", Style(color="red")), end='')
            self.poutput(str(e))
            logger.exception(e)
            pass

    def print_config(self, config: dict):
        """
            Print the configuration in a formatted and colored representation.

            Nested dictionaries are printed hierarchically with indentation.
            Top-level keys and nested keys are displayed using different colors.
            Empty string values are represented as ``<empty>``.

            Args:
                config: Configuration dictionary to print.
        """
        self.poutput("Configuration\n")
        def print_dict(data: dict, indent: int = 0) -> None:
            color = None
            if indent == 0:
                color = "cyan"
            else:
                color = "green"
            for key, value in data.items():
                prefix = " " * indent
                if isinstance(value, dict):
                    self.poutput(Text(f"{prefix}{key}", Style(color=color)))
                    print_dict(value, indent + 2)
                elif isinstance(value, list):
                    self.poutput(f"{prefix}{key:<20} {value}")
                else:
                    value = "" if value == "" else value
                    self.poutput(Text(f"{prefix}{key:<20}", Style(color=color)), end="")
                    if value == "":
                        self.poutput(Text(f"<empty>", Style(color="bright_black")))
                    else:
                        self.poutput(f"{value}")
        print_dict(config)

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
            length = 68
            if self.tensor is None:
                self.poutput("─" * length)
                self.poutput(Text('Optimization problem has not been initialized.', Style(color="red")))
            else:
                self.poutput("─" * length)
                self.poutput("Optimization problem \n")
                if self.tensor.tensor.shape[0] <= 10:
                    self.poutput(str(self.tensor.tensor))
                else:
                    self.poutput(Text("The optimization problem has been successfully loaded."))
            if self.config is None:
                self.poutput("─" * length)
                self.poutput(Text('Configuration has not been initialized.', Style(color="red")))
                self.poutput("─" * length)
            else:
                self.poutput("─" * length)
                self.print_config(self.config)
                self.poutput("─" * length)
            if self.parameters is None:
                self.poutput(Text('The values of the variation parameters have not yet been determined.', Style(color="red")))
                self.poutput("─" * length)
            else:
                self.poutput("Variational parameters \n")
                self.poutput(str(self.parameters.parameters))
                self.poutput("─" * length)
        except Exception as e:
            self.poutput(Text("ERROR: ", Style(color="red")), end='')
            self.poutput(str(e))
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
            if self.config is None:
                self.poutput(Text("ERROR: The experiment configuration is not loaded.", Style(color="red")))
                return
            if self.tensor is None:
                self.poutput(Text("ERROR: The optimization problem is not loaded.", Style(color="red")))
                return
            experiment = ExperimentBuilder().build(self.config)
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
            # if min_energy == -6:
            #     self.count += 1
            # self.poutput(self.count)


            answer = Text(str(answer), Style(color="red"))
            min_energy = Text(str(min_energy), Style(color="green"))
            logger.info(f'The solution of the optimization problem: {answer} with energy {min_energy}.')
            self.poutput('The solution of the optimization problem: ', end='')
            self.poutput(answer, end='')
            self.poutput(' with energy ', end='')
            self.poutput(min_energy, end='.\n')

        except Exception as e:
            self.poutput(Text("ERROR: ", Style(color="red")), end='')
            self.poutput(str(e))
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
            if self.config is None:
                self.poutput(Text("ERROR: The experiment configuration is not loaded.", Style(color="red")))
                return
            if self.tensor is None:
                self.poutput(Text("ERROR: The optimization problem is not loaded.", Style(color="red")))
                return
            experiment = ExperimentBuilder().build(self.config)
            self.experiment_history = experiment.optimize(self.tensor, self.config)
            self.parameters = self.experiment_history.optimization_history[-1].optimal_parameters
            logger.info(f'The values of the variation parameters have been successfully determined.')
            # self.poutput(f'The values of the variation parameters have been successfully determined.')
        except Exception as e:
            self.poutput(Text("ERROR: ", Style(color="red")), end='')
            self.poutput(str(e))
            logger.exception(e)
            pass

    def do_initialize(self, arg: str):
        """Initialize variational parameters.

            Initializes the variational parameters either from a file or using
            the experiment configuration. The initialization method is selected
            using mutually exclusive command-line arguments.

            Args:
                arg: Command-line arguments passed to the ``initialize`` command.
                    Supported options are:
                        - ``-f, --file FILE``: Load variational parameters from
                          the specified file.
                        - ``-c, --config``: Initialize variational parameters
                          using the current experiment configuration.

            Raises:
                SystemExit: If neither ``--file`` nor ``--config`` is provided,
                    or if invalid command-line arguments are specified.

            Examples:
                quant-optimizer> initialize --file parameters.json
                quant-optimizer> initialize -f parameters.json
                quant-optimizer> initialize --config
                quant-optimizer> initialize -c
            """
        try:
            parser = cmd2.Cmd2ArgumentParser()
            group = parser.add_mutually_exclusive_group(required=True)
            group.add_argument(
                "-f",
                "--file",
                metavar="FILE",
                help="Initialize parameters from file"
            )
            group.add_argument(
                "-c",
                "--config",
                action="store_true",
                help="Initialize parameters using configuration"
            )
            args = parser.parse_args(arg.split())
            if args.file:
                logger.info(f'quant-optimizer> initialize --file {arg}')
                self.parameters = VariationalParametersDAL.read(args.file)
            elif args.config:
                experiment = ExperimentBuilder().build(self.config)
                self.parameters = experiment.initialize(self.config, self.tensor)
                logger.info(f'quant-optimizer> initialize --config')
            self.poutput('Variational parameters has been successfully initialized.')
            logger.info('Variational parameters has been successfully initialized.')
        except SystemExit:
            return
        except Exception as e:
            self.poutput(Text("ERROR: ", Style(color="red")), end='')
            self.poutput(str(e))
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

    def do_repeat(self, arg):
        self.count = 0
        for i in range(100):
            self.do_optimize(arg)
            self.poutput(i, end=' ')
            self.do_run(arg)
        print('\a')

