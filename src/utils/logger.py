import logging


def get_logger(name: str) -> logging.Logger:
    """
    Create and configure a logger instance.
    The logger outputs messages to both the console and a log file.

    Args:
        name (str): Logger name, usually provided as __name__.

    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger(name)                                    # Settings for logging
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(
        '%(asctime)s | %(name)s | %(levelname)s | %(message)s',
    )
    console = logging.StreamHandler()                                   # Handler for console-output messages
    console.setFormatter(formatter)
    file = logging.FileHandler(filename="application.log", mode='w')    # Handler for file-output messages
    file.setFormatter(formatter)
    logger.addHandler(console)                                          # Building logger
    logger.addHandler(file)
    return logger
