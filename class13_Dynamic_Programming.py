import numpy as np


# Implementation
def fun_41(arr):
    """
    Find the maximum profit by buying and selling stock
    You can make no more than one transaction

    Parameters
    ----------
    arr : a list of integers

    Returns
    ----------
    The maximum profit : an integer
    """

    # Implement me
    n = len(arr)
    maxProfit = 0
    for i in range(n - 1):
        for j in range(i, n):
            maxProfit = max(maxProfit, arr[j] - arr[i])
    return maxProfit


# Test

# np.random.seed(0)
#
# for i in range(10):
#     n = np.random.randint(low=2, high=11)
#     arr = np.random.randint(low=2, high=11, size=n)
#     print('Input  ' + str(i + 1) + ':', list(arr))
#     print('Output ' + str(i + 1) + ':', fun_41(arr), end='\n\n')
print(50 * "#")


# Implementation
def fun_42(arr):
    """
    Find the maximum profit by buying and selling stock
    You can make no more than one transaction

    Parameters
    ----------
    arr : a list of integers

    Returns
    ----------
    The maximum profit : an integer
    """

    # Implement me
    if len(arr) == 0:
        return 0

    min_price, max_profit = arr[0], 0

    for i in range(1, len(arr)):
        max_profit = max(max_profit, arr[i] - min_price)
        min_price = min(min_price, arr[i])

    return max_profit


# Test
np.random.seed(0)


# for i in range(10):
#     n = np.random.randint(low=2, high=11)
#     arr = np.random.randint(low=2, high=11, size=n)
#     print('Input  ' + str(i + 1) + ':', list(arr))
#     print('Output ' + str(i + 1) + ':', fun_42(arr), end='\n\n')


# Implementation
def fun_44(arr):
    """
    Find the minimum cost to win a game

    Parameters
    ----------
    arr : a list of integers

    Returns
    ----------
    The minimum cost : an integer
    """

    # Implement me
    return helper(arr, len(arr))


# Implementation
def helper(arr, n):
    """
    Find the minimum cost to win a game

    Parameters
    ----------
    arr : a list of integers
    n : the number of barriers we need to pass

    Returns
    ----------
    The minimum cost : an integer
    """

    # Implement me
    if n < 2:
        return 0
    return min([helper(arr, n - 1) + arr[n - 1], helper(arr, n - 2) + arr[n - 2]])


# Test
np.random.seed(0)


# for i in range(10):
#     n = np.random.randint(low=2, high=11)
#     arr = np.random.randint(low=2, high=11, size=n)
#     print('Input  ' + str(i + 1) + ':', list(arr))
#     print('Output ' + str(i + 1) + ':', fun_44(arr), end='\n\n')


# Implementation
def fun_45(arr):
    """
    Find the minimum cost to win a game

    Parameters
    ----------
    arr : a list of integers

    Returns
    ----------
    The minimum cost : an integer
    """

    # Implement me
    a = 0
    b = 0
    c = 0

    for i in range(2, len(arr)+1):
        c = min(a + arr[i - 2], b + arr[i-1])
        a = b
        b = c
    return c


# Test
np.random.seed(0)

# for i in range(10):
#     n = np.random.randint(low=2, high=11)
#     arr = np.random.randint(low=2, high=11, size=n)
#     print('Input  ' + str(i + 1) + ':', list(arr))
#     print('Output ' + str(i + 1) + ':', fun_45(arr), end='\n\n')


# Implementation
def fun_47(m, n):
    """
    Find the number of ways to reach the exit of a maze (represented by a m * n matrix)

    Parameters
    ----------
    m : the number of rows in the matrix
    n : the number of columns in the matrix

    Returns
    ----------
    The number of ways : an integer
    """

    # Implement me
    a,b,c = 0,0,0
    if m == 0 and n == 1:
        return 1
    if n == 0 and m == 1:
        return 1

    return sum(fun_47(m-1, n), fun_47(m,n-1))


# Test
np.random.seed(0)

for i in range(10):
    m, n = np.random.randint(low=0, high=6, size=2)
    print('Input  ' + str(i + 1) + ':', 'm = ' + str(m), 'n = ' + str(n))
    print('Output ' + str(i + 1) + ':', fun_47(m, n), end='\n\n')