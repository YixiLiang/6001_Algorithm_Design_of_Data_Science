# Implementation
def fun_21(list1, list2):
    """
    Find whether two lists of integers, list1 and list2, are equal

    Parameters
    ----------
    list1 : one list of integers
    list2 : another list of integers

    Returns
    ----------
    True, if the two lists are equal
    False, otherwise
    """

    # Implement me (15 marks)
    # if len(list1) == 0 and len(list2) == 0:
    #     return True
    # # store minus number
    # stackCountMinus = []
    # # store number stay
    # stackStay = []
    # listLen = len(list1)
    # # loop whole list1
    # while listLen > 0:
    #
    #     num = list1.pop()
    #     if num > 0 and len(stackCountMinus) == 0:
    #         stackStay.append(num)
    #     elif num > 0 and len(stackCountMinus) != 0:
    #         numMiu = stackCountMinus.pop()
    #         if numMiu+1 < 0:
    #             stackCountMinus.append(numMiu+1)
    #     else:
    #         stackCountMinus.append(num)
    #     listLen -= 1
    # return True if stackStay == list2 and len(stackCountMinus) == 0 else False
    if len(list1) == 0 and len(list2) == 0:
        return True
    # store minus number
    stackCountMinus = []
    listLen = len(list1)
    # loop whole list1 from the end to the start
    while listLen > 0:
        # get the number in current location
        num = list1[listLen-1]
        if num > 0 and len(stackCountMinus) == 0:
            # skip this round
            listLen -= 1
            continue
        elif num > 0 and len(stackCountMinus) != 0:
            # pop the current num and plus the minus number
            list1.pop(listLen-1)
            numMiu = stackCountMinus.pop()
            if numMiu+1 < 0:
                stackCountMinus.append(numMiu+1)
        else:
            # pop the current num and add to stackCountMinus
            list1.pop(listLen-1)
            stackCountMinus.append(num)
        # location -1
        listLen -= 1
    return True if list1 == list2 and len(stackCountMinus) == 0 else False



# Test
print(fun_21([], []))
print(fun_21([2, 3, -1], [2]))
print(fun_21([2, 3, 4, -1, 5, -2], [2]))
print(fun_21([-1], []))
print(fun_21([1, 2, 3, 4, -2, 5, 6, -1], [2, 5]))
print(fun_21([1, -1, 1], [1]))
print(fun_21([2, 3, -100], [2]))

print(50*'#')
# Implementation
def fun_41(arr, target):
    """
    Find a target in a sortetd array (in ascending order)

    Parameters
    ----------
    arr : a list of integers
    target : an integer

    Returns
    ----------
    The index of the first item in arr that equals the target, if the target is in the array
    The index where the target should be inserted (so that the array is still sorted in ascending order), otherwise
    """

    # Implement me (5 marks)
    for i in range(len(arr)):
        if arr[i] >= target:
            return i

    return len(arr)

# Test
arr_1 = [2]
arr_2 = [4]
arr_3 = [2, 3, 4]
arr_4 = [2, 3, 3, 4]
arr_5 = [2, 2, 3, 3, 3, 4, 4]
arr_6 = [3, 3]


print(fun_41(arr_1, 3))
print(fun_41(arr_2, 3))
print(fun_41(arr_3, 3))
print(fun_41(arr_4, 3))
print(fun_41(arr_5, 3))
print(fun_41(arr_6, 3))

print(50*'#')
# Implementation
def fun_42(arr, target):
    """
    Find a target in a sortetd array (in ascending order)

    Parameters
    ----------
    arr : a list of integers
    target : an integer

    Returns
    ----------
    The index of the first item in arr that equals the target, if the target is in the array
    The index where the target should be inserted (so that the array is still sorted in ascending order), otherwise
    """

    # Implement me (35 marks)
    left = 0
    right = len(arr)-1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1
    return left

# Test
arr_1 = [2]
arr_2 = [4]
arr_3 = [2, 3, 4]
arr_4 = [2, 3, 3, 4]
arr_5 = [2, 2, 3, 3, 3, 4, 4]
arr_6 = [3, 3]


print(fun_42(arr_1, 3))
print(fun_42(arr_2, 3))
print(fun_42(arr_3, 3))
print(fun_42(arr_4, 3))
print(fun_42(arr_5, 3))
print(fun_42(arr_6, 3))