def insertion_sort_brute_force(arr):
    """
    Insertion sort

    Parameters
    ----------
    arr : a list of number

    Returns
    ----------
    The list sorted in ascending order
    """

    # Implement me

    arr_temp = list(arr)
    n = len(arr)
    for i in range(1,n):
        temp = arr_temp[i]
        j = 0
        while j < i and arr_temp[j] < temp:
            j += 1
        for k in range(i-1, j-1, -1):
            arr_temp[k + 1] = arr_temp[k]
        # 不能正序，因为移动会覆盖后面的数
        # range 的第三位时表示step，也就是从a到b做什么操作，这里是每次减1
        # for k in range(j, i):
        #     arr_temp[k+1] = arr_temp[k]

        arr_temp[j] = temp
    return arr_temp




# Test
arr_1 = []
arr_2 = [3]
arr_3 = [3, 2]
arr_4 = [3, 2, 1, 4]

print(insertion_sort_brute_force(arr_1))
print(insertion_sort_brute_force(arr_2))
print(insertion_sort_brute_force(arr_3))
print(insertion_sort_brute_force(arr_4))


def insertion_sort_optimal(arr):
    """
    Insertion sort

    Parameters
    ----------
    arr : a list of number

    Returns
    ----------
    The list sorted in ascending order
    """
    # Implement me
    # 把比较的j放在i之前
    # 和第一个相反
    arr_temp = list(arr)
    n = len(arr)
    for i in range(1, n):
        temp = arr_temp[i]
        j = i-1
        while j >= 0 and arr_temp[j] > temp:
            arr_temp[j + 1] = arr_temp[j]
            j -= 1
        arr_temp[j+1] = temp
    return arr_temp


# Test
arr_1 = []
arr_2 = [3]
arr_3 = [3, 2]
arr_4 = [3, 2, 1, 4]

print(insertion_sort_optimal(arr_1))
print(insertion_sort_optimal(arr_2))
print(insertion_sort_optimal(arr_3))
print(insertion_sort_optimal(arr_4))
print(50*'#')


def merge_sort(arr):
    """
    Merge sort

    Parameters
    ----------
    arr : a list of number

    Returns
    ----------
    The list sorted in ascending order
    """

    # Implement me
    # A copy of the list
    arr_temp = list(arr)
    n = len(arr_temp)

    if n > 1:
        # Divide the list into two smaller ones
        # The middle of the list
        mid = n // 2
        # The left sublist
        arr_temp_left = arr_temp[:mid]
        # The right sublist
        arr_temp_right = arr_temp[mid:]

        # Recursively call merge_sort to sort the two smaller lists
        arr_temp_left = merge_sort(arr_temp_left)
        arr_temp_right = merge_sort(arr_temp_right)

        # Merge the two sorted smaller lists
        # i left pointer, j right pointer, k final pointer
        i = j = k = 0
        n_left, n_right = len(arr_temp_left), len(arr_temp_right)

        while i < n_left and j < n_right:
            if arr_temp_left[i] < arr_temp_right[j]:
                arr_temp[k] = arr_temp_left[i]
                i += 1
            else:
                arr_temp[k] = arr_temp_right[j]
                j += 1
            k += 1

        # If there are elements in arr_temp_left that have not been visited
        while i < n_left:
            arr_temp[k] = arr_temp_left[i]
            i += 1
            k += 1

        # If there are elements in arr_temp_right that have not been visited
        while j < n_right:
            arr_temp[k] = arr_temp_right[j]
            j += 1
            k += 1
    return arr_temp




# Test
arr_1 = []
arr_2 = [3]
arr_3 = [3, 2]
arr_4 = [3, 2, 1, 4]

print(merge_sort(arr_1))
print(merge_sort(arr_2))
print(merge_sort(arr_3))
print(merge_sort(arr_4))