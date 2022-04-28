# Implementation
def fun_21(matrix, target):
    """
    Find a target in a m * n matrix

    Parameters
    ----------
    matrix : list[list[int]] (i.e., a list of list of integers)
    target : an integer

    Returns
    ----------
    True  : if the target is in the matrix
    False : otherwise
    """

    # Implement me (25 marks)
    # If matrix is empty [] or [[]] return None
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return False
    # Get the number of row and column store thm as m, n
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        left, right = 0, n - 1
        while left <= right:
            # Get the middle column
            mid = left + (right - left)//2
            if matrix[i][mid] == target:
                return True
            elif matrix[i][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
    return False


# Test
matrix_1 = []
target_1 = 2

matrix_2 = [[]]
target_2 = 2

matrix_3 = [[1], [2]]
target_3 = 2

matrix_4 = [[1, 2, 3, 15],
            [4, 5, 6, 16],
            [7, 8, 9, 17]]
target_4 = 10

matrix_5 = [[1, 2, 3, 15],
            [4, 5, 6, 16],
            [7, 8, 9, 17]]
target_5 = 6

print(fun_21(matrix_1, target_1))
print(fun_21(matrix_2, target_2))
print(fun_21(matrix_3, target_3))
print(fun_21(matrix_4, target_4))
print(fun_21(matrix_5, target_5))

print(50*'#')

# Reference: The code below is from chapter_5_tree_search_solution.ipynb
class TreeNode(object):
    """The tree node class (for a binary tree)"""

    def __init__(self, x):
        # The value of the node
        self.val = x
        # The left child
        self.left = None
        # The right child
        self.right = None


# Implementation
def fun_31(root, target):
    """
     tree such that the sum of value of nodes in the path equals a target

    Parameters
    ----------
    root : the root of a binary tree
    target : an integer

    Returns
    ----------
    True,  if there is such a path
    False, otherwise
    """

    # Implement me (15 marks)
    # Base
    if root == None:
        return False
    if root.left == None and root.right == None:
        if target == root.val:
            return True
        else:
            return False
    # Recursion the function, set the target as current target - node value.
    # If there is a true in the tree, it will return true.
    return fun_31(root.left, target-root.val) or fun_31(root.right, target-root.val)




# Test
root1 = None
target1 = 0

root2 = TreeNode(1)
target2 = 0

root3 = TreeNode(1)
root3.left = TreeNode(-1)
target3 = 0

root4 = TreeNode(1)
root4.left = TreeNode(-1)
root4.right = TreeNode(1)
target4 = 1

root5 = TreeNode(1)
root5.left = TreeNode(-1)
root5.left.left = TreeNode(-2)
root5.right = TreeNode(1)
root5.right.right = TreeNode(2)
target5 = 3

root6 = TreeNode(1)
root6.left = TreeNode(-1)
root6.left.left = TreeNode(-2)
root6.right = TreeNode(1)
root6.right.right = TreeNode(2)
target6 = 4

print(fun_31(root1, target1))
print(fun_31(root2, target2))
print(fun_31(root3, target3))
print(fun_31(root4, target4))
print(fun_31(root5, target5))
print(fun_31(root6, target6))
print(50*'#')


# Reference: Part of the code below is from chapter_5_tree_search_solution.ipynb
# Implementation
def fun_32(matrix):
    """
    Find the number of (vertically or horizontally) connected deserts in a map (represented by a matrix)

    Parameters
    ----------
    matrix : a matrix where 1 denotes desert and 0 denotes grassland

    Returns
    ----------
    the number of connected deserts
    """

    # Corner case
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return 0

    m, n = len(matrix), len(matrix[0])
    # The number of connected deserts
    count = 0

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                count += 1
                # DFS: remove '1's conntected to entry [i, j]
                helper(matrix, m, n, i, j)

    # Implement me (5 marks)
    # Restore the matrix
    # Replace None with 1
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == None:
                matrix[i][j] = 1
    return count

def helper(matrix, m, n, i, j):
    """
    DFS: remove '1's conntected to entry [i, j]

    Parameters
    ----------
    matrix : a matrix where 1 denotes desert and 0 denotes grass land
    m : the nubmer of rows in the matrix
    n : the nubmer of columns in the matrix
    i, j : entry [i, j]
    """

    # Implement me (5 marks)
    # if i and j is invalid and matrix is not 1, return None
    if i < 0 or i >= m or j < 0 or j >= n or matrix[i][j] != 1:
        return

    # Replace '1' with None
    matrix[i][j] = None

    # Remove '1' above [i, j]
    helper(matrix, m, n, i-1, j)
    # Remove '1' below [i, j]
    helper(matrix, m, n, i+1, j)
    # Remove '1' on the left-hand side of [i, j]
    helper(matrix, m, n, i, j - 1)
    # Remove '1' on the right-hand side of [i, j]
    helper(matrix, m, n, i, j + 1)


# Test
matrix1 = []
matrix2 = [[]]
matrix3 = [[1]]
matrix4 = [[1, 1],
           [0, 1]]
matrix5 = [[1, 0],
           [0, 1]]
matrix6 = [[1, 0, 0],
           [0, 1, 0],
           [0, 0, 1]]
matrix7 = [[1, 1, 0],
           [0, 1, 0],
           [0, 0, 1]]
matrix8 = [[1, 1, 1],
           [0, 1, 0],
           [0, 0, 1]]
matrix9 = [[1, 1, 0],
           [0, 1, 0],
           [1, 0, 1]]
matrix10 = [[1, 1, 0],
            [1, 1, 0],
            [1, 0, 1]]

print(fun_32(matrix1))
print(fun_32(matrix2))
print(fun_32(matrix3))
print(fun_32(matrix4))
print(fun_32(matrix5))
print(fun_32(matrix6))
print(fun_32(matrix7))
print(fun_32(matrix8))
print(fun_32(matrix9))
print(fun_32(matrix10), end='\n\n')

print('As shown below, the map remains the same as the input one')
print(matrix1)
print(matrix2)
print(matrix3)
print(matrix4)
print(matrix5)
print(matrix6)
print(matrix7)
print(matrix8)
print(matrix9)
print(matrix10)
print(50*'#')

# Implementation
from collections import deque


def fun_41(root, target):
    """
    Find whether there is a path in the binary tree such that the sum of value of nodes in the path equals a target

    Parameters
    ----------
    root : the root of a binary tree
    target : an integer

    Returns
    ----------
    True,  if there is such a path
    False, otherwise
    """

    # Implement me (15 marks)
    # Corner case
    if root == None:
        return False
    # create queue
    queue = deque([root])
    # BFS
    while len(queue) > 0:
        n = len(queue)
        for _ in range(n):
            # Remove the first node in the queue
            node = queue.popleft()
            # if the node is leaves node, and the value is equal to target, return true
            if node.left == None and node.right == None:
                if node.val == target:
                    return True

            if node.left != None:
                # Add the left child to the end of the queue and change the left node value as the sum of itself and parent value
                queue.append(node.left)
                node.left.val += node.val
            if node.right != None:
                # Add the right child to the end of the queue and change the right node value as the sum of itself and parent value
                queue.append(node.right)
                node.right.val += node.val

    return False

# Test
root1 = None
target1 = 0

root2 = TreeNode(1)
target2 = 0

root3 = TreeNode(1)
root3.left = TreeNode(-1)
target3 = 0

root4 = TreeNode(1)
root4.left = TreeNode(-1)
root4.right = TreeNode(1)
target4 = 1

root5 = TreeNode(1)
root5.left = TreeNode(-1)
root5.left.left = TreeNode(-2)
root5.right = TreeNode(1)
root5.right.right = TreeNode(2)
target5 = 3

root6 = TreeNode(1)
root6.left = TreeNode(-1)
root6.left.left = TreeNode(-2)
root6.right = TreeNode(1)
root6.right.right = TreeNode(2)
target6 = 4

print(fun_41(root1, target1))
print(fun_41(root2, target2))
print(fun_41(root3, target3))
print(fun_41(root4, target4))
print(fun_41(root5, target5))
print(fun_41(root6, target6))
print(50*'#')


# Implementation
def fun_42(root):
    """
    Find the bottom-right node in a binary tree

    Parameters
    ----------
    root : the root of a tree

    Returns
    ----------
    The value of the bottom-right node in a binary tree
    """

    # Implement me (10 marks)
    # Corner case
    if root == None:
        return None
    # create queue
    queue = deque([root])

    while len(queue) > 0:
        # Get the length of the queue
        n = len(queue)
        # loop the level
        for _ in range(n):
            # pop out the left node
            node = queue.popleft()
            # Update bottom_right using the value of the node
            rightNodeValue = node.val
            if node.left != None:
                # Add the value of the left child to the end of the queue
                queue.append(node.left)
            if node.right != None:
                # Add the value of the right child to the end of the queue
                queue.append(node.right)
    return rightNodeValue
# Test
root1 = None

root2 = TreeNode(0)

root3 = TreeNode(0)
root3.left = TreeNode(1)

root4 = TreeNode(0)
root4.left = TreeNode(1)
root4.right = TreeNode(2)

root5 = TreeNode(0)
root5.left = TreeNode(1)
root5.left.left = TreeNode(3)
root5.right = TreeNode(2)
root5.right.left = TreeNode(4)

root6 = TreeNode(0)
root6.left = TreeNode(1)
root6.left.left = TreeNode(3)
root6.right = TreeNode(2)
root6.right.right = TreeNode(4)

print(fun_42(root1))
print(fun_42(root2))
print(fun_42(root3))
print(fun_42(root4))
print(fun_42(root5))
print(fun_42(root6))