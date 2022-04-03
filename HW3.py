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

# Reference: The code below is from chapter_5_tree_search_solution.ipynb
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

    # Base
    if root == None:
        return -1

    # Recursion
    return max(fun_51(root.left), fun_51(root.right)) + 1


# Implementation
def fun_61(root):
    """
    Check whether a binary tree is height-balanced

    Parameters
    ----------
    root : the root of a binary tree

    Returns
    ----------
    True, if the tree is height balanced
    False, otherwise
    """

    # Implement me (95 marks)
    # when root is None return True
    if root is None:
        return True
    # count left and right subtree height
    rootLeft = fun_51(root.left)
    rootRight = fun_51(root.right)
    # print(rootLeft, rootRight)
    # First compare this level left and height subtree height, if the difference is bigger than 1 return False.
    # If this level left and height subtree height is the same, go to next level, until all levels done.
    return True if rootLeft - rootRight <= 1 and fun_61(root.left) and fun_61(root.right) else False


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

root6 = TreeNode(0)
root6.left = TreeNode(1)
root6.left.left = TreeNode(2)
root6.left.left.left = TreeNode(3)
root6.right = TreeNode(1)
root6.right.right = TreeNode(2)
root6.right.right.right = TreeNode(3)

print(fun_61(root1))
print(fun_61(root2))
print(fun_61(root3))
print(fun_61(root4))
print(fun_61(root5))
print(fun_61(root6))