def fun_31(arr, target):
    """
    Find a target in an array
    You can assume the items in the array are unique

    Parameters
    ----------
    arr : a list of integers
    target : an integer

    Returns
    ----------
    The index of the target, if the target is in the array
    None, otherwise
    """

    # Initialize idx with None (which should be returned if the target is not in the array)
    idx = None
    for i in range(len(arr)):
        if target == arr[i]:
            idx = i
    return idx


# Test
arr_1 = [2]
arr_2 = [3]
arr_3 = [2, 3]

print(fun_31(arr_1, 3))
print(fun_31(arr_2, 3))
print(fun_31(arr_3, 3))
print("#" * 50)


# Implementation
def fun_33(arr, target):
    """
    Find a target in an array
    You can assume the items in the array are unique

    Parameters
    ----------
    arr : a list of integers
    target : an integer

    Returns
    ----------
    The index of the target, if the target is in the array
    None, otherwise
    """

    # Implemet me
    idx = None
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return idx


# Test
arr_1 = [2]
arr_2 = [3]
arr_3 = [2, 3]

print(fun_33(arr_1, 3))
print(fun_33(arr_2, 3))
print(fun_33(arr_3, 3))
print("#" * 50)


# Implementation
def fun_33(arr, target):
    """
    Find a target in an array
    You can assume the items in the array are unique

    Parameters
    ----------
    arr : a list of integers
    target : an integer

    Returns
    ----------
    The index of the target, if the target is in the array
    None, otherwise
    """

    # Implemet me
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = start + (start - end) // 2
        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1


# Test
arr_1 = [2]
arr_2 = [3]
arr_3 = [2, 3]

print(fun_33(arr_1, 3))
print(fun_33(arr_2, 3))
print(fun_33(arr_3, 3))
print("#" * 50)


# Implementation
def fun_36(arr, target):
    """
    Find a target in an array
    You can assume the items in the array are unique

    Parameters
    ----------
    arr : a list of integers
    target : an integer

    Returns
    ----------
    The index of the target, if the target is in the array
    The index where the target should be inserted (so that the array is still sorted in ascending order), otherwise
    """

    # Implement me
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if target == arr[mid]:
            return mid
        if arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return left


# Test
arr_1 = [2]
arr_2 = [4]
arr_3 = [2, 3, 4]

print(fun_36(arr_1, 3))
print(fun_36(arr_2, 3))
print(fun_36(arr_3, 3))
print("#" * 50)

