from typing import NamedTuple, Any
from app.data_structures.array import Array

class Value(NamedTuple):
    key : Any
    value : Any

class BSTNode:
    def __init__(self, key, value):
        self.value = Value(key, value)
        self.parent = None
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, key, value):
        if self.root == None:
            self.root = BSTNode(key, value)
            return
        pointer = self.root
        while True:
            if pointer.value.key < key:
                if pointer.right is None:
                    pointer.right = BSTNode(key, value)
                    pointer.right.parent = pointer
                    return
                else:
                    pointer = pointer.right
            else:
                if pointer.left is None:
                    pointer.left = BSTNode(key, value)
                    pointer.left.parent = pointer
                    return
                else:
                    pointer = pointer.left



    def search(self, value):
        pointer = self.root
        while pointer:
            if pointer.value.key == value:
                return pointer
            if pointer.value.key >= value:
                pointer = pointer.left
            else:
                pointer = pointer.right
        else:
            raise ValueError("\nNot Such A Data is Available\n")
        

        
    def successor(self, node):
        y = node.right
        while y.left:
            y = y.left
        return y


        
    def delete(self, value):
        node = self.search(value)
        parent = node.parent

        if parent is None:
            if node.left is None and node.right is None:
                self.root = None
                del node
                return True
            elif node.left is None:
                self.root = node.right
                self.root.parent = None
                del node
                return True
            elif node.right is None:
                self.root = node.left
                self.root.parent = None
                del node
                return True

        if node.right is None and node.left is None:
            if parent.left == node:
                parent.left = None
                del node
                return True
            elif parent.right == node:
                parent.right = None
                del node
                return True
        
        elif node.right and node.left is None:
            if parent.right == node:
                parent.right = node.right
                del node
                return True
            elif parent.left == node:
                parent.left = node.right
                del node
                return True
            
        elif node.left and node.right is None:
            if parent.right == node:
                parent.right = node.left
                del node
                return True
            elif parent.left == node:
                parent.left = node.left
                del node
                return True
            
        elif node.left and node.right:
            succ = self.successor(node)
            node.value = succ.value
            if succ.parent.left == succ:
                succ.parent.left = succ.right
                if succ.right:
                    succ.right.parent = succ.parent
            else:
                succ.parent.right = succ.right
                if succ.right:
                    succ.right.parent = succ.parent
            del succ
            return True


    def preorder(self, root, preOrder=None):
        if preOrder is None:
            preOrder = Array()
        if root is not None:
            preOrder.append(
                root.value.value
            )
            self.preorder(root.left, preOrder)
            self.preorder(root.right, preOrder)

        return preOrder

    def _preorder(self):
        return self.preorder(self.root)


    def inorder(self, root, inOrder=None):
        if inOrder is None:
            inOrder = Array()
        if root is not None:
            self.inorder(root.left, inOrder)
            inOrder.append(
                root.value.value
            )
            self.inorder(root.right, inOrder)
        return inOrder
    def _inorder(self):
        return self.inorder(self.root)
    

    def postorder(self, root, postOrder=None):
        if postOrder is None:
            postOrder = Array()
        if root is not None:
            self.postorder(root.left, postOrder)
            self.postorder(root.right, postOrder)
            postOrder.append(
                root.value.value
            )
        return postOrder
    def _postorder(self):
        return self.postorder(self.root)
        
