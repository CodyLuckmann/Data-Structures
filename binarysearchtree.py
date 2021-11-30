from node import Node


class BinarySearchTree:
    def __init__(self):
        self.root = None
            
    def insert_node (self, newValue):
        node = Node(newValue)

        # if tree is empty make new node, declare it as root
        if self.root is None:
            self.root = node
        else:
            temp_node = self.root
            # if tree not empty, insert node into tree
            # if new value is less than value of root, add to left subtree
            if newValue < temp_node:
                self.root.leftChild = node
            else:
            # if new value greater than root, add to right subtree
                self.root.rightChild = node
            
            

# can only add value in a left/right child if the child is None
# if the child is NOT None, we need to move down to the next node
# need some way to re-apply decision on each layer we encounter while loop            
# use a temp node to represent the current node we're testing against       
                