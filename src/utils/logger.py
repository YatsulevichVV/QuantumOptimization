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
    # Settings for logging
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    formatter = logging.Formatter(
        '%(asctime)s | %(name)s | %(levelname)s | %(message)s',
    )
    # Handler for console-output messages
    console = logging.StreamHandler()
    console.setFormatter(formatter)
    # Handler for file-output messages
    file = logging.FileHandler(filename="application.log", mode='w')
    file.setFormatter(formatter)
    # Building logger
    logger.addHandler(console)
    logger.addHandler(file)
    return logger
