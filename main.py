import numpy as np
import logging
from src.core.input.qubo import QUBO


def print_hi(name):
    print(f'Hi, {name}')


if __name__ == '__main__':

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        filename='py_log.log',
        filemode='w'
    )
    logger = logging.getLogger(__file__)

    try:
        logger.info('Starting the program')
        matrix = np.array([[1, 2], [3, 4], [5, 6]])
        qubo = QUBO(matrix)
        logger.info('Successfully initialized the program')
    except Exception as e:
        logger.exception(e)
        raise
