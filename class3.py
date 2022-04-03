# Implementation
def fun_36(arr):
    """
    Find the largest sum across all the contiguous (non-empty) subarrays of the input array
    You may assume the input array is not empty

    Parameters
    ----------
    arr : a list of integers

    Returns
    ----------
    The largest sum : an interger
    """

    # Implement me
    max_sum = None
    for i in range(len(arr)):
        sum_ = 0
        for j in range(i, len(arr)):
            sum_ += arr[j]
            if max_sum is None or max_sum < sum_:
                max_sum = sum_
    return max_sum

# Test
arr_1 = [2]
arr_2 = [-2, 3]
arr_3 = [-2, 3, -2, 4, -1, -2]

print(fun_36(arr_1))
print(fun_36(arr_2))
print(fun_36(arr_3))


def fun_38(arr):
    """
    Find the largest sum across all the contiguous (non-empty) subarrays of the input array
    You may assume the input array is not empty
    这个算法的核心是统计之前所有的和，只要之前的和大于1就进行运算下来。否者小于1就重新计算
    Parameters
    ----------
    arr : a list of integers

    Returns
    ----------
    The largest sum : an interger
    """

    sum_arr = [0] * len(arr)
    # Corner case
    sum_arr[0] = arr[0]

    for i in range(1, len(arr)):
        if sum_arr[i-1] > 0:
            sum_arr[i] = sum_arr[i-1] + arr[i]
        else:
            sum_arr[i] = arr[i]
    return max(sum_arr)

# Test
arr_1 = [2]
arr_2 = [-2, 3]
arr_3 = [-2, 3, -2, 4, -1, -2]

print(fun_38(arr_1))
print(fun_38(arr_2))
print(fun_38(arr_3))


def fun_310(arr):
    """
    Find the largest sum across all the contiguous (non-empty) subarrays of the input array
    You may assume the input array is not empty
    节省空间意味着只用变量
    Parameters
    ----------
    arr : a list of integers

    Returns
    ----------
    The largest sum : an interger
    """

    # Implement me

    # Corner case
    sum_last = arr[0]
    sum_max = arr[0]

    for i in range(1, len(arr)):
        if sum_last > 0:
            sum_last = sum_last + arr[i]
        else:
            sum_last = arr[i]
        if sum_last > sum_max:
            sum_max = sum_last
    return sum_max

# Test
arr_1 = [2]
arr_2 = [-2, 3]
arr_3 = [-2, 3, -2, 4, -1, -2]

print(fun_310(arr_1))
print(fun_310(arr_2))
print(fun_310(arr_3))


def fun_312(arr):
    """
    Find the largest sum across all the contiguous (non-empty) subarrays of the input array
    You may assume the input array is not empty
    You may also assume there is exactly one subarray (that has the largest sum)

    Parameters
    ----------
    arr : a list of integers

    Returns
    ----------
    [the largest sum,
    the index of the first element in the subarray,
    the index of the last element in the subarray]
    : a list
    """

    # Implement me
    max_sum = None
    # For each possible start of the subarray
    for i in range(len(arr)):
        # For each possible end of the subarray
        for j in range(i, len(arr)):
            # The sum of the subarray (starting with i and ending with j)
            sum_ = 0
            for k in range(i, j + 1):
                sum_ += arr[k]

            if max_sum is None or max_sum < sum_:
                # Update max_sum
                max_sum = sum_
                start_index = i
                end_index = j

    return [max_sum, start_index, end_index]

# Test
arr_1 = [2]
arr_2 = [-2, 3]
arr_3 = [-2, 3, -2, 4, -1, -2]

print(fun_312(arr_1))
print(fun_312(arr_2))
print(fun_312(arr_3))


def fun_313(arr):
    """
    Find the largest sum across all the contiguous (non-empty) subarrays of the input array
    You may assume the input array is not empty
    You may also assume there is exactly one subarray (that has the largest sum)

    Parameters
    ----------
    arr : a list of integers

    Returns
    ----------
    [the largest sum,
    the index of the first element in the subarray,
    the index of the last element in the subarray]
    : a list
    """

    # Implement me
    max_sum = None
    start_index, end_index = 0,0
    # For each possible start of the subarray
    for i in range(len(arr)):
        sum_ = 0
        for j in range(i, len(arr)):
            # The sum of the subarray (starting with i and ending with j)
            sum_ += arr[j]
            if max_sum is None or max_sum < sum_:
                # Update max_sum
                max_sum = sum_
                start_index = i
                end_index = j

    return [max_sum, start_index, end_index]

# Test
arr_1 = [2]
arr_2 = [-2, 3]
arr_3 = [-2, 3, -2, 4, -1, -2]

print(fun_313(arr_1))
print(fun_313(arr_2))
print(fun_313(arr_3))


def fun_314(arr):
    """
    Find the largest sum across all the contiguous (non-empty) subarrays of the input array
    You may assume the input array is not empty
    You may also assume there is exactly one subarray (that has the largest sum)

    Parameters
    ----------
    arr : a list of integers

    Returns
    ----------
    [the largest sum,
    the index of the first element in the subarray,
    the index of the last element in the subarray]
    : a list
    """

    # Implement me
    sum_arr = [0] * len(arr)
    # Corner case
    sum_arr[0] = arr[0]

    for i in range(1, len(arr)):
        if sum_arr[i - 1] > 0:
            sum_arr[i] = sum_arr[i - 1] + arr[i]
        else:
            sum_arr[i] = arr[i]

    # The largest sum and the index of the last element
    max_sum, last_idx = None, 0

    for i in range(len(arr)):
        if max_sum is None or max_sum < sum_arr[i]:
            # Update max_sum and last_idx
            max_sum, last_idx = sum_arr[i], i

    if max_sum == arr[last_idx]:
        return [max_sum, last_idx, last_idx]

    sum_ = max_sum
    # The index of the first element
    first_idx = last_idx + 1

    while (sum_ != 0):
        first_idx -= 1
        sum_ -= arr[first_idx]
    return [max_sum, first_idx, last_idx]
# Test
arr_1 = [2]
arr_2 = [-2, 3]
arr_3 = [-2, 3, -2, 4, -1, -2]

print(fun_313(arr_1))
print(fun_313(arr_2))
print(fun_313(arr_3))


def fun_315(arr):
    """
    Find the largest sum across all the contiguous (non-empty) subarrays of the input array
    You may assume the input array is not empty
    You may also assume there is exactly one subarray (that has the largest sum)

    Parameters
    ----------
    arr : an array

    Returns
    ----------
    [the largest sum,
    the index of the first element in the subarray,
    the index of the last element in the subarray]
    : a list

    """

    # Implement me
    global_max, local_max = arr[0], arr[0]
    first_idx, last_idx, first_idx_temp = 0, 0, 0

    for i in range(1, len(arr)):
        if local_max > 0:
            local_max += arr[i]
        else:
            local_max, first_idx_temp = arr[i], i
        if global_max < local_max:
            global_max, first_idx, last_idx = local_max, first_idx_temp, i

    return [global_max, first_idx, last_idx]

# Test
arr_1 = [2]
arr_2 = [-2, 3]
arr_3 = [-2, 3, -2, 4, -1, -2]

print(fun_315(arr_1))
print(fun_315(arr_2))
print(fun_315(arr_3))