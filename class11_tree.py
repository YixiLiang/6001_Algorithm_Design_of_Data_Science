from collections import deque

class TreeNode(object):
    """The tree node class (for a binary tree)"""

    def __init__(self, x):
        # The value of the node
        self.val = x

        # The left child
        self.left = None

        # The right child
        self.right = None
# The root
root = TreeNode(0)

# The left and right child at depth 1
root.left = TreeNode(1)
root.right = TreeNode(2)

# The children at depth 2
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)

def level_order(root):
    """
    Level-order traversal

    Parameters
    ----------
    root : the root of a binary tree
    """

    # Corner case
    if root == None:
        return

    # Initialize the queue
    queue = deque([root])

    # Level order traversal
    while len(queue) > 0:
        # Get the length of the queue
        n = len(queue)
        for _ in range(n):
            # Remove the first node in the queue
            node = queue.popleft()
            if node != None:
                print(node.val, end=' ')
                # Add the left and right children to the end of the queue
                queue.append(node.left)
                queue.append(node.right)
        print()

# Test
level_order(root)
print(50*'#')

# Implementation
def fun_51(root):
    """
    Find the height of a binary tree

    Parameters
    ----------
    root : the root of a binary tree

    Returns
    ----------
    The height of the tree : an integer
    """

    # Implement me
    if root == None:
        return -1
    leftNode = fun_51(root.left)
    rightNode = fun_51(root.right)

    return max(leftNode, rightNode)+1

    # # 老师的方法
    # # Base
    # if root == None:
    #     return -1
    #
    # # Recursion
    # return max(fun_51(root.left), fun_51(root.right)) + 1

# Test
root1 = None

root2 = TreeNode(0)

root3 = TreeNode(0)
root3.left = TreeNode(1)
root3.right = TreeNode(2)

root4 = TreeNode(0)
root4.left = TreeNode(1)
root4.right = TreeNode(2)
root4.left.left = TreeNode(3)

print(fun_51(root1))
print(fun_51(root2))
print(fun_51(root3))
print(fun_51(root4))
print(50*'#')


# Implementation
def fun_52(root1, root2):
    """
    Find whether two binary trees are the same

    Parameters
    ----------
    root : the root of a binary tree

    Returns
    ----------
    True, if the trees are the same
    False, otherwise
    """

    # Implement me
    # Method 1
    if root1 is None or root2 is None:
        if root1 is None and root2 is None:
            return True
        else:
            return False
    if root1.val != root2.val:
        return False

    return fun_52(root1.left, root2.left) and fun_52(root1.right, root2.right)

    # # 老师的方法
    # # Base
    # if root1 == None and root2 == None:
    #     return True
    #
    # # Base
    # if root1 == None or root2 == None:
    #     return False
    #
    # # Recursion
    # return (root1.val == root2.val
    #         and fun_52(root1.left, root2.left)
    #         and fun_52(root1.right, root2.right))




# Test
root1 = None
root2 = None

root3 = None
root4 = TreeNode('0')

root5 = TreeNode('0')
root6 = TreeNode('0')

root7 = TreeNode('0')
root7.left = TreeNode('1')
root8 = TreeNode('0')
root8.right = TreeNode('1')

print(fun_52(root1, root2))
print(fun_52(root3, root4))
print(fun_52(root5, root6))
print(fun_52(root7, root8))
print(50*'#')


# Implementation
def fun_53(root):
    """
    Check whether a binary tree is symmetric (i.e., mirror of itself)

    Parameters
    ----------
    root : the root of a binary tree

    Returns
    ----------
    True, if the tree is symmetric
    False, otherwise
    """

    # Implement me
    if root is None:
        return True

    return helper(root.left, root.right)


def helper(left, right):
    """
    Check whether the left subtree is the mirror of the right subtree

    Parameters
    ----------
    left : the root of the left subtree
    right : the root of the right subtree

    Returns
    ----------
    True, if the left subtree is the mirror of the right subtree
    False, otherwise
    """

    # Implement me
    if left is None or right is None:
        if left is None and right is None:
            return True
        else:
            return False
    if left.val != right.val:
        return False

    return fun_52(left.left, right.right) and fun_52(left.right, right.left)


# Test
root1 = None

root2 = TreeNode(0)

root3 = TreeNode(0)
root3.left = TreeNode(1)

root4 = TreeNode(0)
root4.left = TreeNode(1)
root4.right = TreeNode(1)

root5 = TreeNode(0)
root5.left = TreeNode(1)
root5.left.left = TreeNode(2)
root5.right = TreeNode(1)
root5.right.left = TreeNode(2)

root6 = TreeNode(0)
root6.left = TreeNode(1)
root6.left.left = TreeNode(2)
root6.right = TreeNode(1)
root6.right.right = TreeNode(2)

print(fun_53(root1))
print(fun_53(root2))
print(fun_53(root3))
print(fun_53(root4))
print(fun_53(root5))
print(fun_53(root6))
print(50*'#')





