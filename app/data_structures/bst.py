class BSTNode:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        if self.root == None:
            self.root = BSTNode(value)
            return
        pointer = self.root
        while True:
            if pointer.value < value:
                if pointer.right is None:
                    pointer.rihgt = BSTNode(value)
                    pointer.right.parent = pointer
                    return
                else:
                    pointer = pointer.right
            else:
                if pointer.left is None:
                    pointer.left = BSTNode(value)
                    pointer.left.parent = pointer
                    return
                else:
                    pointer = pointer.left



    def search(self, value):
        pointer = self.root
        while pointer:
            if pointer.value == value:
                return pointer
            if pointer.value > value:
                pointer = pointer.left
            else:
                pointer = pointer.right
        else:
            raise IndexError("\nNot Such A Data is Available\n")
        
    def successor(self, node):
        y = node.right
        while y.left:
            y = y.left
        return y


        
    def delete(self, value):
        node = self.search(value)
        parent = node.parent

        if node.rihgt is None and node.left is None:
            if parent.left.value == value:
                parent.left = None
                del node
                return True
            elif parent.right.value == value:
                parent.right = None
                del node
                return True
        
        if node.right and node.left is None:
            if parent.right.value == value:
                parent.right = node.right
                del node
                return True
            elif parent.left.value == value:
                parent.left = node.right
                del node
                return True
        if node.left and node.right is None:
            if parent.right.value == value:
                parent.right = node.left
                del node
                return True
            elif parent.left.value == value:
                parent.left = node.left
                del node
                return True
        if node.right and node.left:
            pass # need to be correct also for root

        

    def inorder(self, root):
        if root is not None:
            self.inorder(self.left)
            print(root.data)
            self.inorder(self.right)

