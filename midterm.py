# Implementation
def fun_31(arr):
    """
    Find the first and second smallest element in the array
    You may assume the array has at least two unique elements

    Parameters
    ----------
    arr : a list of integers

    Returns
    ----------
    [the first smallest element, the second smallest element] : a list of two integers
    """

    # Implement me (20 marks)
    # create two variables to store the first two elements in array
    if arr[0] > arr[1]:
        smallFirst = arr[1]
        smallSceond = arr[0]
    else:
        smallFirst = arr[0]
        smallSceond = arr[1]
    # start from 2, compare with first and second small variable.
    for i in range(2, len(arr)):
        if arr[i] < smallFirst:
            smallSceond = smallFirst
            smallFirst = arr[i]
        elif arr[i] < smallSceond:
            smallSceond = arr[i]

    return [smallFirst, smallSceond]

# Test
arr_1 = [2, 3]
arr_2 = [3, 2]
arr_3 = [2, 3, 5, -4]
arr_4 = [2, 3, 5, -4, 9, 10, 20, 11]

print(fun_31(arr_1))
print(fun_31(arr_2))
print(fun_31(arr_3))
print(fun_31(arr_4))
print(50*'#')


def fun_41(s):
    """
    Find the minimum number of parentheses that should be added to make the input string valid
    The parentheses are valid if they are always in pairs and in correct order
    You may assume the string only includes '(' and ')'

    Parameters
    ----------
    s : a string

    Returns
    ----------
    the minimum number of parentheses that should be added : an integer
    """

    # Implement me (20 marks)
    parentheses = {')':'('}
    stack = []
    for c in s:
        # judge if right parentheses
        if c in parentheses.keys() and len(stack) != 0:
            # compare with lastOne, if lastOne is '(', then remove from stack,
            # else lastOne = ')' add current and lastOne into stack
            lastOne = stack.pop()
            if parentheses.get(c) == lastOne:
                continue
            else:
                stack.append(lastOne)
                stack.append(c)
        else:
            stack.append(c)
    return len(stack)


# Test
s_1 = "()"
s_2 = "("
s_3 = ")"
s_4 = ")("
s_5 = "()()"
s_6 = "))(("

print(fun_41(s_1))
print(fun_41(s_2))
print(fun_41(s_3))
print(fun_41(s_4))
print(fun_41(s_5))
print(fun_41(s_6))
print(50*'#')


def fun_42(s):
    """
    Find the minimum number of parentheses that should be added to make the input string valid
    The parentheses are valid if they are always in pairs and in correct order
    You may assume the string only includes '(' and ')'

    Parameters
    ----------
    s : a string

    Returns
    ----------
    the minimum number of parentheses that should be added : an integer
    """

    # Implement me (20 marks)
    parentheses = {')': '('}
    # countLeftPar count left parentheses
    countLeftPar = 0
    # countInvalidPar count right parentheses that are not match with left parentheses,
    # and left parentheses that are not match with right parentheses
    countInvalidPar = 0
    for c in s:
        # judge if right parentheses
        if c in parentheses.keys():
            if countLeftPar > 0:
                # if there is any left parentheses - 1
                countLeftPar -= 1
            else:
                # means there is not any left parentheses, so it must invalid
                countInvalidPar += 1
        else:
            # left parentheses + 1
            countLeftPar += 1
    return countLeftPar + countInvalidPar

# Test
s_1 = "()"
s_2 = "("
s_3 = ")"
s_4 = ")("
s_5 = "()()"
s_6 = "))(("

print(fun_42(s_1))
print(fun_42(s_2))
print(fun_42(s_3))
print(fun_42(s_4))
print(fun_42(s_5))
print(fun_42(s_6))
