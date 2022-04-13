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

# Implementation
def fun_54(root1, root2):
    """
    Find whether two binary trees have the same sequence of leaves

    Parameters
    ----------
    root : the root of a binary tree

    Returns
    ----------
    True, if the trees have the same sequence of leaves
    False, otherwise
    """

    # Implement me
    return helper(root1) == helper(root2)




def helper(root):
    """
    Find the sequence of leaves of a tree

    Parameters
    ----------
    root : the root of a binary tree

    Returns
    ----------
    The sequence of leaves : a list
    """

    # Implement me
    if root == None:
        return []
    if root.left == None and root.right == None:
        return [root.val]
    return helper(root.left) + helper(root.right)

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

print(fun_54(root1, root2))
print(fun_54(root3, root4))
print(fun_54(root5, root6))
print(fun_54(root7, root8))
print(50*'#')


# Implementation
def fun_55(root):
    """
    Find the paths (from the root to a leaf) of a binary tree

    Parameters
    ----------
    root : the root of a binary tree

    Returns
    ----------
    The paths
    """

    # Implement me
    global paths
    paths = []
    helper(root,'')
    return paths


def helper(root, path):
    """
    Find the paths (from the root to a leaf) of a binary tree

    Parameters
    ----------
    root : the root of a binary tree

    Returns
    ----------
    The paths
    """

    # Implement me
    if root == None:
        return

    if root.left == None and root.right == None:
        path += str(root.val)
        paths.append(path)
        return
    else:
        path += str(root.val) + '->'
        helper(root.left, path)
        helper(root.right, path)

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

print(fun_55(root1))
print(fun_55(root2))
print(fun_55(root3))
print(fun_55(root4))
print(fun_55(root5))
print(fun_55(root6))
print(50*'#')


# Implementation
def fun_56(root):
    """
    Find whether a binary tree is a Binary Search Tree (BST)

    Parameters
    ----------
    root : the root of a binary tree

    Returns
    ----------
    True, if the tree is a BST
    False, otherwise
    """

    # Implement me
    # Base
    if root == None:
        return True
    return helper(root.left, float('-inf'), root.val) and helper(root.right, root.val, float('inf'))


def helper(root, min_, max_):
    """
    Find whether a binary tree is a Binary Search Tree (BST)

    Parameters
    ----------
    root : the root of a binary tree
    min_ : the lower bound of the value of the tree
    max_ : the upper bound of the value of the tree

    Returns
    ----------
    True, if the tree is a BST
    False, otherwise
    """


    # Implement me
    # Base
    if root == None:
        return True

    # Base
    if root.val <= min_ or root.val >= max_:
        return False

    # Recursion
    return helper(root.left, min_, root.val) and helper(root.right, root.val, max_)


# Implementation
def fun_57(arr):
    """
    Build a height-balanced binary tree from an array

    Parameters
    ----------
    arr : a list of integers

    Returns
    ----------
    A height-balanced binary tree
    """

    # Implement me

