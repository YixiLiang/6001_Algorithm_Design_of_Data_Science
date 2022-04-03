# def fun_44(s):
#     """
#     Check whether the parentheses in the input string are valid
#     The parentheses are valid if they are always in pairs and in correct order
#     You may assume the string only includes '(' and ')'
#
#     Parameters
#     ----------
#     s : a string
#
#     Returns
#     ----------
#     True or False : boolean
#     """
#
#     # Implement me
#     count = 0
#     for c in s:
#         if c == ')':
#             count -= 1
#         else:
#             count += 1
#         if count < 0:
#             return False
#     return True if count == 0 else False #如果只有（，这就是为什么count要等于0
#
# # Test
# s_1 = "()"
# s_2 = ")("
# s_3 = "()()"
# s_4 = "(())"
#
# print(fun_44(s_1))
# print(fun_44(s_2))
# print(fun_44(s_3))
# print(fun_44(s_4))


# def fun_45(s):
#     """
#     Check whether the parentheses in the input string are valid
#     The parentheses are valid if they are always in pairs and in correct order
#     You may assume the string includes not only '(' and ')', but also '[' and ']' and '{' and '}'
#
#     Parameters
#     ----------
#     s : a string
#
#     Returns
#     ----------
#     True or False : boolean
#     """
#
#     # Implement me
#     lefts, rights = ['(','[','{'],[')',']','}']
#     stack = []
#     for c in s:
#         if c in rights:
#             idx = rights.index(c)
#             if (len(stack) == 0) or (lefts[idx] != stack.pop()):
#                 return False
#
# # Test
# s_1 = "()"
# s_2 = ")("
# s_3 = "()()"
# s_4 = "([(]){})"
#
# print(fun_45(s_1))
# print(fun_45(s_2))
# print(fun_45(s_3))
# print(fun_45(s_4))


def fun_46(s):
    """
    Check whether the parentheses in the input string are valid
    The parentheses are valid if they are always in pairs and in correct order
    You may assume the string includes not only '(' and ')', but also '[' and ']' and '{' and '}'

    Parameters
    ----------
    s : a string

    Returns
    ----------
    True or False : boolean
    """

    # Implement me
    parentheses = {')': '(', ']': '[', '}': '{'}
    stack = []

    for c in s:
        if c in parentheses.keys():
            if (len(stack) == 0) or (parentheses.get(c) != stack.pop()):
                return False
        else:
            stack.append(c)

    return True if len(stack) == 0 else False

# Test
s_1 = "()"
s_2 = ")("
s_3 = "()()"
s_4 = "(())"

print(fun_46(s_1))
print(fun_46(s_2))
print(fun_46(s_3))
print(fun_46(s_4))


def fun_48(tokens):
    """
    Evaluate an arithmetic expression in Reverse Polish notation
    You may assume all the nubmers in the expression are intergers

    Parameters
    ----------
    tokens : a list of strings

    Returns
    ----------
    the value of the arithmetic expression : a number
    0 if "divide by zero"
    """

    # Implement me
    n1 = 0
    n2 = 0
    stack = []

    for i in tokens:
        if i in ["+",'-','*',"/"]:
            n2 = stack.pop()
            n1 = stack.pop()
            if i == '+':
                stack.append(n1 + n2)
            elif i == '-':
                stack.append(n1 - n2)
            elif i == '*':
                stack.append(n1 * n2)
            elif i == '/':
                stack.append(n1 / n2 if n2 != 0 else 0)
        else:
            stack.append(int(i))
    return stack.pop()

# Test
arr_1 = ['2']
arr_2 = ['2', '3', '*']
arr_3 = ['2', '3', '*', '-4', '4', '+', '/']
arr_4 = ['2', '3', '*', '-4', '-4', '6', '+', '-', '/']

print(fun_48(arr_1))
print(fun_48(arr_2))
print(fun_48(arr_3))
print(fun_48(arr_4))


def fun_49(tokens):
    """
    Evaluate an arithmetic expression in Reverse Polish notation
    You may assume all the nubmers in the expression are intergers

    Parameters
    ----------
    tokens : a list of strings

    Returns
    ----------
    the value of the arithmetic expression : a number
    0 if "divide by zero"
    """

    operations = {'+': lambda x, y: x + y,
                  '-': lambda x, y: x - y,
                  '*': lambda x, y: x * y,
                  '/': lambda x, y: x / y if y != 0 else 0}

    stack = []

    for token in tokens:
        # If the token is an operator
        if token in operations.keys():
            # Pop the second operand
            b = stack.pop()
            # Pop the first operand
            a = stack.pop()
            # Push a operator b
            stack.append(operations[token](a, b))
        # If the token is an operand
        else:
            # Push the integer
            stack.append(int(token))

    return stack.pop()

# Test
arr_1 = ['2']
arr_2 = ['2', '3', '*']
arr_3 = ['2', '3', '*', '-4', '4', '+', '/']
arr_4 = ['2', '3', '*', '-4', '-4', '6', '+', '-', '/']

print(fun_49(arr_1))
print(fun_49(arr_2))
print(fun_49(arr_3))
print(fun_49(arr_4))