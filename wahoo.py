import logging
import numpy.matlib 
import numpy as np

def wahoovian(matrix):

    logging.info('INFO: Entering wahoovian function')

    if (matrix.shape[0] == matrix.shape[1] and matrix.shape[0] != 0):
        matrix = np.transpose(matrix)
        matrix *= -1
    else:
        logging.info('WARNING: Input matrix is not square')
        
    logging.info('INFO: Exiting wahoovian function')
    
    return matrix

