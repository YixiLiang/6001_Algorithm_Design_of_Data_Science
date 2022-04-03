def quick_sort_last(arr, left, right):
    """
    Quick sort (using the last element of the input array as the pivot)

    Parameters
    ----------
    arr : a list of number
    left : the starting index of the list
    right : the ending index of the list

    Returns
    ----------
    The list sorted in ascending order
    """

    # Implement me
    arr_temp = list(arr)

    if left < right:
        pivot = partition_last(arr_temp, left, right)

        arr_temp = quick_sort_last(arr_temp, left, pivot - 1)
        arr_temp = quick_sort_last(arr_temp, pivot + 1, right)

    return arr_temp


def partition_last(arr, left, right):
    """
    Partition (using the last element of the input array as the pivot)
    All the number no larger than the pivot will be on the left-hand side of the pivot
    All the number larger than the pivot will be on the right-hand side of the pivot

    Parameters
    ----------
    arr : a list of number
    left : the starting index of the list
    right : the ending index of the list

    Returns
    ----------
    The index of the pivot
    """

    # Implement me
    # 循序渐进，i开始等于-1，j开始等于1，i一直在left的最右侧，j在最新的数
    pivot = arr[right]
    i = left - 1

    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


# Test
arr_1 = []
arr_2 = [3]
arr_3 = [3, 2]
arr_4 = [3, 2, 1, 4]

print(quick_sort_last(arr_1, 0, len(arr_1) - 1))
print(quick_sort_last(arr_2, 0, len(arr_2) - 1))
print(quick_sort_last(arr_3, 0, len(arr_3) - 1))
print(quick_sort_last(arr_4, 0, len(arr_4) - 1))
print(50 * '#')


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

def pre_order(root):
    """
    Pre-order traversal

    Parameters
    ----------
    root : the root of a binary tree
    """

    # Implement me
    if root == None:
        return
    print(root.val, end=" ")
    pre_order(root.left)
    pre_order(root.right)
# Test
pre_order(root)
print("")


def in_order(root):
    """
    In-order traversal

    Parameters
    ----------
    root : the root of a binary tree
    """

    # Implement me
    if root == None:
        return
    in_order(root.left)
    print(root.val, end=" ")
    in_order(root.right)

in_order(root)
print('')


def post_order(root):
    """
    Post-order traversal

    Parameters
    ----------
    root : the root of a binary tree
    """

    # Implement me
    if root == None:
        return
    post_order(root.left)
    post_order(root.right)
    print(root.val, end=" ")
# Test
post_order(root)
print('')
