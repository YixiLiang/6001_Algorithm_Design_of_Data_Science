import numpy as np


# Implementation
def fun_37(target):
    """
    Check whether the target is a square of another number

    Parameters
    ----------
    target : an integer

    Returns
    ----------
    True, if the target is a square of another number
    False, otherwise
    """

    # Implement me
    # Corner case
    if target == 0:
        return True

    # For each target i
    for i in range(1, target + 1):
        if i == target / i:
            return True
    # i*i may let to overflow
    # for i in range(target + 1):
    #     if i * i == target:
    #         return True

    return False


# Test
target_1 = -1
target_2 = 0
target_3 = 5
target_4 = 9
target_5 = 100

print(fun_37(target_1))
print(fun_37(target_2))
print(fun_37(target_3))
print(fun_37(target_4))
print(fun_37(target_5))

print(50 * '#')


# Implementation
def fun_38(target):
    """
    Check whether the target is a square of another number

    Parameters
    ----------
    target : an integer

    Returns
    ----------
    True, if the target is a square of another number
    False, otherwise
    """

    # Implement me
    left = 0
    right = target - 1
    if target == 1:
        return True
    if target == 0:
        return True
    if target < 0:
        return False
    while left <= right:
        mid = left + (right - left) // 2
        div = target / mid
        if mid == div:
            return True
        elif mid > target / mid:
            right = mid - 1
        else:
            left = mid + 1

    return False


# Test
target_1 = -1
target_2 = 0
target_3 = 5
target_4 = 9
target_5 = 100

print(fun_38(target_1))
print(fun_38(target_2))
print(fun_38(target_3))
print(fun_38(target_4))
print(fun_38(target_5))

print(50 * '#')


# Implementation
def fun_310(n):
    """
    Find the number I picked (between 1 and n), in no more than n attempts

    Parameters
    ----------
    n : a positive integer

    Returns
    ----------
    The target I picked (between 1 and n)
    """

    # Implement me
    for i in range(1, n + 1):
        if helper(i, n) == 1:
            return True
    return None


def helper(i, n):
    """
    Check whether the number I picked, i, is the same as the real one, n

    Parameters
    ----------
    i : a positive integer
    n : a positive integer

    Returns
    ----------
    1, if i = n
    0, otherwise
    """

    # Randomly pick a number between 1 and n
    np.random.seed(0)
    num = np.random.randint(low=1, high=n + 1)

    return 1 if i == num else 0


# Test
n_1 = 1
n_2 = 3
n_3 = 100

print(fun_310(n_1))
print(fun_310(n_2))
print(fun_310(n_3))

print(50 * "#")


# Implementation
def fun_311(n):
    """
    Find the number I picked (between 1 and n), in no more than \log(n) attempts

    Parameters
    ----------
    n : a positive integer

    Returns
    ----------
    The number I picked (between 1 and n)
    """

    # Implement me

    left, right = 1, n
    while left <= right:
        mid = left + (right - left) // 2
        num = helper(mid, n)
        if num == 0:
            return mid
        elif num == -1:
            right = mid - 1
        else:
            left = mid + 1
    return left


def helper(i, n):
    """
    Check whether the number I picked, i, is the same as the real one, n

    Parameters
    ----------
    i : a positive integer
    n : a positive integer

    Returns
    ----------
    0,  if i = n
    -1, if i > n
    1,  if i < n
    """

    # Randomly pick a number between 1 and n
    np.random.seed(1)
    num = np.random.randint(low=1, high=n + 1)

    if i == num:
        return 0
    if i > num:
        return -1
    if i < num:
        return 1


# Test
n_1 = 1
n_2 = 3
n_3 = 100

print(fun_311(n_1))
print(fun_311(n_2))
print(fun_311(n_3))

print(50 * '#')


# Implementation
def fun_312(matrix, target):
    """
    Find a target in a (m * n) matrix

    Parameters
    ----------
    matrix : list[list[int]] (i.e., a list of list of integers)
    target : an integer

    Returns
    ----------
    [i, j], if matrix[i, j] = target
    None, if the target is not in the matrix
    """

    # Implement me
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return None
    m, n = len(matrix), len(matrix[0])

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == target:
                return [i, j]


# Test
matrix_1 = []
target_1 = 2

matrix_2 = [[]]
target_2 = 2

matrix_3 = [[1], [2]]
target_3 = 2

matrix_4 = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]]
target_4 = 8

matrix_5 = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]]
target_5 = 13

print(fun_312(matrix_1, target_1))
print(fun_312(matrix_2, target_2))
print(fun_312(matrix_3, target_3))
print(fun_312(matrix_4, target_4))
print(fun_312(matrix_5, target_5))

print(50 * '#')


# Implementation
def fun_313(matrix, target):
    """
    Find a target in a (m * n) matrix
    You can assume each row in the matrix is sorted in ascending order

    Parameters
    ----------
    matrix : list[list[int]] (i.e., a list of list of integers)
    target : an integer

    Returns
    ----------
    [i, j], if matrix[i, j] = target
    None, if the target is not in the matrix
    """

    # Implement me
    # Implement me
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return None
    m, n = len(matrix), len(matrix[0])

    for i in range(m):
        left = 0
        right = n - 1
        while left <= right:
            mid = left + (right - left) // 2

            if target == matrix[i][mid]:
                return [i, mid]
            elif target > matrix[i][mid]:
                left = mid + 1
            else:
                right = mid - 1

    return None


# Test
matrix_1 = []
target_1 = 2

matrix_2 = [[]]
target_2 = 2

matrix_3 = [[1], [2]]
target_3 = 2

matrix_4 = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]]
target_4 = 8

matrix_5 = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]]
target_5 = 13

print(fun_313(matrix_1, target_1))
print(fun_313(matrix_2, target_2))
print(fun_313(matrix_3, target_3))
print(fun_313(matrix_4, target_4))
print(fun_313(matrix_5, target_5))
print(50 * '#')


# Implementation
def fun_315(matrix, target):
    """
    Find a target in a (m * n) matrix
    You can assume each row in the matrix is sorted in ascending order
    You can also assume items on row i are smaller than those on row i + 1

    Parameters
    ----------
    matrix : list[list[int]] (i.e., a list of list of integers)
    target : an integer

    Returns
    ----------
    [i, j], if matrix[i, j] = target
    None, if the target is not in the matrix
    """
    # 这个方法适用于这种情况
    #    1 3 5 7
    #    2 4 6 8
    # Implement me
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return None
    m, n = len(matrix), len(matrix[0])

    i, j = 0, n - 1
    while i >= 0 and i < m and j >= 0 and j < n:
        if matrix[i][j] == target:
            return [i,j]
        if matrix[i][j] < target:
            i += 1
        elif matrix[i][j] > target:
            j -= 1
    return None


# Test
matrix_1 = []
target_1 = 2

matrix_2 = [[]]
target_2 = 2

matrix_3 = [[1], [2]]
target_3 = 2

matrix_4 = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]]
target_4 = 8

matrix_5 = [[1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12]]
target_5 = 13

print(fun_315(matrix_1, target_1))
print(fun_315(matrix_2, target_2))
print(fun_315(matrix_3, target_3))
print(fun_315(matrix_4, target_4))
print(fun_315(matrix_5, target_5))
