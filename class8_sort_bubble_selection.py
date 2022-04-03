def bubble_sort_brute_force(arr):
    """
    Bubble sort

    Parameters
    ----------
    arr : a list of number

    Returns
    ----------
    The list sorted in ascending order
    """

    # Implement me
    lenArr = len(arr)
    arr_temp = list(arr)
    for i in range(lenArr - 1):
        for j in range(lenArr - 1):
            if arr_temp[j] > arr_temp[j + 1]:
                arr_temp[j], arr_temp[j + 1] = arr_temp[j + 1], arr_temp[j]
    return arr_temp


# Test
arr_1 = []
arr_2 = [3]
arr_3 = [3, 2]
arr_4 = [3, 2, 1, 4]

print(bubble_sort_brute_force(arr_1))
print(bubble_sort_brute_force(arr_2))
print(bubble_sort_brute_force(arr_3))
print(bubble_sort_brute_force(arr_4))
print(50 * '#')


def bubble_sort_improved(arr):
    """
    Bubble sort

    Parameters
    ----------
    arr : a list of number

    Returns
    ----------
    The list sorted in ascending order
    """

    # Implement me

    lenArr = len(arr)
    arr_temp = list(arr)
    for i in range(lenArr - 1):
        for j in range(lenArr - i - 1):
            if arr_temp[j] > arr_temp[j + 1]:
                arr_temp[j], arr_temp[j + 1] = arr_temp[j + 1], arr_temp[j]
    return arr_temp


# Test
arr_1 = []
arr_2 = [3]
arr_3 = [3, 2]
arr_4 = [4, 3, 2, 1, 0]

print(bubble_sort_improved(arr_1))
print(bubble_sort_improved(arr_2))
print(bubble_sort_improved(arr_3))
print(bubble_sort_improved(arr_4))
print(50 * "#")


def bubble_sort_optimal(arr):
    """
    Bubble sort

    Parameters
    ----------
    arr : a list of number

    Returns
    ----------
    The list sorted in ascending order
    """

    # Implement me
    lenArr = len(arr)
    for i in range(lenArr):
        swapped = False
        for j in range(lenArr - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if swapped == False:
            return arr
    return arr


# Test
arr_1 = []
arr_2 = [3]
arr_3 = [3, 2]
arr_4 = [4, 3, 2, 1]

print(bubble_sort_optimal(arr_1))
print(bubble_sort_optimal(arr_2))
print(bubble_sort_optimal(arr_3))
print(bubble_sort_optimal(arr_4))
print(50 * '#')


def selection_sort_brute_force(arr):
    """
    Selection sort

    Parameters
    ----------
    arr : a list of number

    Returns
    ----------
    The list sorted in ascending order
    """

    # Implement me
    arr_temp = arr
    lenArr = len(arr)
    for i in range(lenArr):
        for j in range(lenArr - 1, 0, -1):
            if arr_temp[j] < arr_temp[j - 1]:
                arr_temp[j], arr_temp[j - 1] = arr_temp[j - 1], arr_temp[j]
    return arr_temp


# Test
arr_1 = []
arr_2 = [3]
arr_3 = [3, 2]
arr_4 = [3, 2, 1, 4]

print(selection_sort_brute_force(arr_1))
print(selection_sort_brute_force(arr_2))
print(selection_sort_brute_force(arr_3))
print(selection_sort_brute_force(arr_4))
print(50 * '#')


def selection_sort_improved(arr):
    """
    Selection sort

    Parameters
    ----------
    arr : a list of number

    Returns
    ----------
    The list sorted in ascending order
    """

    # Implement me
    arr_temp = arr
    lenArr = len(arr)
    for i in range(lenArr):
        for j in range(lenArr - 1, i, -1):
            if arr_temp[j] < arr_temp[j - 1]:
                arr_temp[j], arr_temp[j - 1] = arr_temp[j - 1], arr_temp[j]
    return arr_temp


# Test
arr_1 = []
arr_2 = [3]
arr_3 = [3, 2]
arr_4 = [3, 2, 1, 4]

print(selection_sort_improved(arr_1))
print(selection_sort_improved(arr_2))
print(selection_sort_improved(arr_3))
print(selection_sort_improved(arr_4))
print(50 * '#')


def selection_sort_optimal(arr):
    """
    Selection sort

    Parameters
    ----------
    arr : a list of number

    Returns
    ----------
    The list sorted in ascending order
    """

    # Implement me
    arr_temp = arr
    lenArr = len(arr)
    for i in range(lenArr):
        min_num, min_idx = arr_temp[lenArr - 1], lenArr - 1
        for j in range(lenArr - 2, i - 1, -1):
            if arr_temp[j] < min_num:
                min_num = arr_temp[j]
                min_idx = j
        arr_temp[i], arr_temp[min_idx] = arr_temp[min_idx], arr_temp[i]
    return arr_temp


# Test
arr_1 = []
arr_2 = [3]
arr_3 = [3, 2]
arr_4 = [3, 2, 1, 4]

print(selection_sort_optimal(arr_1))
print(selection_sort_optimal(arr_2))
print(selection_sort_optimal(arr_3))
print(selection_sort_optimal(arr_4))
