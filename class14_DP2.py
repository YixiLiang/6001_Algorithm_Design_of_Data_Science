import numpy as np


# # Implementation
# def fun_47(m, n):
#     """
#     Find the number of ways to reach the exit of a maze (represented by a m * n matrix)
#
#     Parameters
#     ----------
#     m : the number of rows in the matrix
#     n : the number of columns in the matrix
#
#     Returns
#     ----------
#     The number of ways : an integer
#     """
#
#     # Implement me
#     # Base
#     if m <= 0 or n <= 0:
#         return 0
#     if m == 1 or n == 1:
#         return 1
#
#     return fun_47(m - 1, n) + fun_47(m, n - 1)
#
#
# # Test
# np.random.seed(0)
#
# for i in range(10):
#     m, n = np.random.randint(low=0, high=6, size=2)
#     print('Input  ' + str(i + 1) + ':', 'm = ' + str(m), 'n = ' + str(n))
#     print('Output ' + str(i + 1) + ':', fun_47(m, n), end='\n\n')

print(50*'#')

# Implementation
def fun_48(m, n):
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

    # Implement me
    # Base
    if m <= 0 or n <= 0:
        return 0
    if m == 1 or n == 1:
        return 1

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
            matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]

    return matrix[m - 1][n - 1]


# Test
np.random.seed(0)

for i in range(10):
    m, n = np.random.randint(low=0, high=6, size=2)
    print('Input  ' + str(i + 1) + ':', 'm = ' + str(m), 'n = ' + str(n))
    print('Output ' + str(i + 1) + ':', fun_48(m, n), end='\n\n')
print(50*'#')


# Implementation
def fun_49(m, n):
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

    # Implement me
    # Base
    if m <= 0 or n <= 0:
        return 0

    row = [1 for _ in range(n)]
    # Initialize the first row
    for i in range(1,m):
        for j in range(1,n):
            # 这里通过行来计算，因为我们需要左边和上边的和，所以可以用自己和上一个计算出现在位置的结果
            row[j] += row[j-1]

    return row[n-1]


# Test
np.random.seed(0)

for i in range(10):
    m, n = np.random.randint(low=0, high=6, size=2)
    print('Input  ' + str(i + 1) + ':', 'm = ' + str(m), 'n = ' + str(n))
    print('Output ' + str(i + 1) + ':', fun_49(m, n), end='\n\n')
print(50*'#')


# Implementation
def fun_411(arr):
    """
    Get the maximum number of candies

    Parameters
    ----------
    arr : a list of integers

    Returns
    ----------
    The maximum number of candies : an integer
    """

    # Implement me
    # Base
    if len(arr) == 0:
        return 0
    if len(arr) <= 2:
        return max(arr)

    return max(arr[-1] + fun_411(arr[:-2]), fun_411(arr[:-1]))

# Test
np.random.seed(0)

for i in range(10):
    n = np.random.randint(low=2, high=11)
    arr = np.random.randint(low=2, high=11, size=n)
    print('Input  ' + str(i + 1) + ':', list(arr))
    print('Output ' + str(i + 1) + ':', fun_411(arr), end='\n\n')
print(50*'#')

# Implementation
def fun_412(arr):
    """
    Get the maximum number of candies

    Parameters
    ----------
    arr : a list of integers

    Returns
    ----------
    The maximum number of candies : an integer
    """

    # Implement me
    a,b,c = arr[0],arr[1],arr[0] + arr[2]
    if len(arr) == 0:
        return 0
    if len(arr) <= 2:
        return max(arr)
    # b是前两个的最大值，意味着保存的是当前到达最大值
    a, b = arr[0], max(arr[:2])
    # 取前两个的最大值
    for i in range(2,len(arr)):
        c = max(a + arr[i], b)
        a = b
        b = c
    return c



# Test
np.random.seed(0)

for i in range(10):
    n = np.random.randint(low=2, high=11)
    arr = np.random.randint(low=2, high=11, size=n)
    print('Input  ' + str(i + 1) + ':', list(arr))
    print('Output ' + str(i + 1) + ':', fun_412(arr), end='\n\n')
print(50*'#')


# 堆 heapq
import heapq
arr = [1,3,2,9]
heapq.heapify(arr)

heapq.nlargest(3, arr)
heapq.heappop(arr)
heapq.heappush(arr,0)
heapq



