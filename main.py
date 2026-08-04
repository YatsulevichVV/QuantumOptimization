from src.utils.console import Command
from src.utils.logger import get_logger


if __name__ == '__main__':
    logger = get_logger(__name__)
    Command().cmdloop()
