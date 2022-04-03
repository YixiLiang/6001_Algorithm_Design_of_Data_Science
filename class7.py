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
    n = len(arr)
    for i in range(n):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr


# Test
arr_1 = []
arr_2 = [3]
arr_3 = [3, 2]
arr_4 = [3, 2, 1, 4]

print(bubble_sort_brute_force(arr_1))
print(bubble_sort_brute_force(arr_2))
print(bubble_sort_brute_force(arr_3))
print(bubble_sort_brute_force(arr_4))
print(50*'#')


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
    n = len(arr)
    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    return arr

# Test
arr_1 = []
arr_2 = [3]
arr_3 = [3, 2]
arr_4 = [3, 2, 1, 4]

print(bubble_sort_improved(arr_1))
print(bubble_sort_improved(arr_2))
print(bubble_sort_improved(arr_3))
print(bubble_sort_improved(arr_4))
