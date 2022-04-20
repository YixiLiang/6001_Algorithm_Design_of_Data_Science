# Implementation
def fun_21(m, n):
    """
    Find the number of ways to reach the exit of a maze (represented by a m * n matrix)

    Parameters
    ----------
    matrix : a matrix of integers
    m : the number of rows in the matrix
    n : the number of columns in the matrix

    Returns
    ----------
    The number of ways : an integer
    """

    # Implement me (25 marks)

# Test
import numpy as np
np.random.seed(0)

for i in range(10):
    m, n = np.random.randint(low=0, high=6, size=2)
    print('Input  ' + str(i + 1) + ':', 'm = ' + str(m), 'n = ' + str(n))
    print('Output ' + str(i + 1) + ':', fun_21(m, n), end='\n\n')