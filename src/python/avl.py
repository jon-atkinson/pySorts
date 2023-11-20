class AVL_Node(object):
    def __init__(self, data=0):
        self.data = data
        self.depth = 0
        self.left = None
        self.right = None

class AVL_Tree(object):
    def __init__(self, data = 0):
        self.root = AVL_Node(data=data)


    def insert(self, root, data):
        if not root:
            return AVL_Node(data=data)
        elif data < root.data:
            root.left = self.insert(root.right, data)
        else:
            root.right = self.insert(root.left, data)
        
        root.depth = 1 + max(self.get_depth(root.left), self.get_depth(root.right))
        
        bal_factor = self.get_balance_factor(root)

        if bal_factor > 1:
            if data < root.left.data:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)
        if bal_factor < -1:
            if data > root.right.data:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)

        return root


    def get_depth(self, root):
        if not root:
            return 0
        return self.depth


    def get_balance_factor(self, root):
        if not root:
            return 0
        return self.get_depth(root.left) - self.get_depth(root.right)


    def left_rotate(self, root):
        a = root.right
        new_root = a.left
        a.left = root
        root.right = new_root
        root.depth = 1 + max(self.get_depth(root.left), self.get_depth(root.right))
        a.depth = 1 + max(self.get_depth(a.left), self.get_depth(a.right))
        return new_root
    

    def right_rotate(self, root):
        a = root.left
        new_root = a.right
        a.right = root
        root.left = new_root
        root.depth = 1 + max(self.get_depth(root.left), self.get_depth(root.right))
        a.depth = 1 + max(self.get_depth(a.left), self.get_depth(a.right))
        return new_root

    def to_sorted_array(self, root, array=[]):
        if root != None:
            self.to_sorted_array(root.left, array)
            array.append(root.data)
            self.to_sorted_array(root.right, array)
        return array