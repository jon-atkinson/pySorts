import numpy as np

class AVL_Node(object):
    def __init__(self, data):
        self.data = data
        self.depth = 0
        self.left = None
        self.right = None


def avl_insert(root, data):
    if not root:
        return AVL_Node(data=data)
    elif data < root.data:
        root.left = avl_insert(root.left, data)
    else:
        root.right = avl_insert(root.right, data)

    root.depth = 1 + max(avl_get_depth(root.left), avl_get_depth(root.right))

    bal_factor = avl_get_balance_factor(root)

    if bal_factor > 1:
        if data < root.left.data:
            return avl_right_rotate(root)
        else:
            root.left = avl_left_rotate(root.left)
            return avl_right_rotate(root)
    if bal_factor < -1:
        if data > root.right.data:
            return avl_left_rotate(root)
        else:
            root.right = avl_right_rotate(root.right)
            return avl_left_rotate(root)
    return root


def avl_get_depth(root):
    if not root:
        return 0
    return root.depth


def avl_get_balance_factor(root):
    if not root:
        return 0
    return avl_get_depth(root.left) - avl_get_depth(root.right)


def avl_left_rotate(root):
    a = root.right
    root.right = a.left
    a.left = root
    root.depth = 1 + max(avl_get_depth(root.left), avl_get_depth(root.right))
    a.depth = 1 + max(avl_get_depth(a.left), avl_get_depth(a.right))
    return a


def avl_right_rotate(root):
    a = root.left
    root.left = a.right
    a.right = root
    root.depth = 1 + max(avl_get_depth(root.left), avl_get_depth(root.right))
    a.depth = 1 + max(avl_get_depth(a.left), avl_get_depth(a.right))
    return a


def avl_to_sorted_array(root, array=None, index=0):
    if array is None:
        array = np.zeros(0, dtype=int)
    if root is not None:
        index = avl_to_sorted_array(root.left, array, index)

        array[index] = root.data
        index += 1

        index = avl_to_sorted_array(root.right, array, index)

    return index