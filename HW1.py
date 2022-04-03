# Implementation
def fun_21(arr):
    """
    Find the first and second largest element in the array
    You may assume the array has at least two unique elements

    Parameters
    ----------
    arr : a list of integers

    Returns
    ----------
    [the first largest element, the second largest element] : a list of two integers
    """

    # Implement me (45 marks)
    # distribute first two numbers in arr to firstLarge and secondLarge by order
    if arr[0] >= arr[1]:
        firstLarge = arr[0]
        secondLarge = arr[1]
    else:
        firstLarge = arr[1]
        secondLarge = arr[0]

    # compare the rest of the numbers in arr and change firstLarge and secondLarge value in specific situation
    for i in range(2, len(arr)):
        if arr[i] > firstLarge:
            secondLarge = firstLarge
            firstLarge = arr[i]
        elif arr[i] > secondLarge:
            secondLarge = arr[i]
    return [firstLarge, secondLarge]


# Test
arr_1 = [2, 3]
arr_2 = [3, 2, 3]
arr_3 = [2, 3, 5, -4]
arr_4 = [2, 3, 5, -4, 9, 10, 20, 11]

print(fun_21(arr_1))
print(fun_21(arr_2))
print(fun_21(arr_3))
print(fun_21(arr_4))


# Implementation
def fun_22(arr):
    """
    Find the largest sum across all the contiguous (non-empty) subarrays of the input array
    You may assume the input array is not empty
    You may not assume there is exactly one subarray (that has the largest sum)

    Parameters
    ----------
    arr : a list of integers

    Returns
    ----------
    [the largest sum,
    the list of all the possible [index of the first element, index of the last element]]
    : a list of two items, where the first item is an integer and the second item is a list of list
    """

    # Implement me (45 marks)
    # The largest sum, list of the index
    max_sum = None
    max_list = []

    for i in range(len(arr)):
        # The sum of the subarray (starting with i)
        sum_ = 0
        for j in range(i, len(arr)):
            # The sum of the subarray (ending with j)
            sum_ += arr[j]
            if max_sum is None or max_sum <= sum_:
                if max_sum == sum_:
                    # if list has the same max sum add the index into the list
                    max_list.append([i, j])
                else:
                    # Update list
                    max_list = [[i, j]]
                # Update max_sum
                max_sum = sum_
    return [max_sum, max_list]


# Test
arr_1 = [2]
arr_2 = [-2, 3]
arr_3 = [-2, 3, -2, 4, -1, -2]
arr_4 = [-2, 3, -2, 4, -1, -2, -10, 5]

print(fun_22(arr_1))
print(fun_22(arr_2))
print(fun_22(arr_3))
print(fun_22(arr_4))
