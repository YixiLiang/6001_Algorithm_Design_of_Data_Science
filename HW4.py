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
    # Base
    # Implement me (25 marks)
    # Base
    if m <= 0 or n <= 0:
        return 0
    if m == 1 or n == 1:
        return 1

    # Create m * n matrix to store number of ways to reach the cells
    matrix = [[0 for _ in range(n)] for _ in range(m)]

    # Initialize the first row
    for j in range(n):
        matrix[0][j] = 1

    # Initialize the first column
    for i in range(m):
        matrix[i][0] = 1

    # Update the matrix
    for i in range(1, m):
        for j in range(1, n):
            # According to the question, the number of ways of the cell is the sum of the top, the left and northwest cell
            matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1] + matrix[i - 1][j - 1]
    return matrix[m - 1][n - 1]
# Test
import numpy as np

np.random.seed(0)

for i in range(10):
    m, n = np.random.randint(low=0, high=6, size=2)
    print('Input  ' + str(i + 1) + ':', 'm = ' + str(m), 'n = ' + str(n))
    print('Output ' + str(i + 1) + ':', fun_21(m, n), end='\n\n')

print(50*'#')

# Implementation
def fun_22(m, n):
    """
    Find the number of ways to reach the exit of a maze (represented by a m * n matrix)

    Parameters
    ----------
    matrix : a matrix of integers
    m : the number of rows in the matrix
    n : the number of columns in the ma

    Returns
    ----------
    The number of ways : an integer
    """

    # Implement me (65 marks)
    # Base
    if m <= 0 or n <= 0:
        return 0

    # create row to store
    arr = [1] * n

    for i in range(1, m):
        # This step can store the northwest cell
        lastTop = arr[0]
        for j in range(1, n):
            # store current cell
            current = arr[j]
            # add top cell, left cell and the stored northwest cell
            arr[j] += arr[j-1] + lastTop
            # store northwest cell
            lastTop = current

    return arr[n-1]


# Test
np.random.seed(0)

for i in range(10):
    m, n = np.random.randint(low=0, high=6, size=2)
    print('Input  ' + str(i + 1) + ':', 'm = ' + str(m), 'n = ' + str(n))
    print('Output ' + str(i + 1) + ':', fun_22(m, n), end='\n\n')