from node import Node


class BinarySearchTree:
    def __init__(self):
        self.root = None
            
    def insert_node (self, new_value):
        node = Node(new_value)

        # if tree is empty make new node, declare it as root
        if self.root is None:
            self.root = node
            return
        current_node = self.root
        prev_node = None
           
        while current_node:
            prev_node = current_node
            if new_value < current_node.data:
                current_node = current_node.leftChild
            else:
                current_node = current_node.rightChild
            
        if new_value < prev_node.data:
            prev_node.leftChild = node
        else:
            prev_node.rightChild = node
            
            
           
            
            

# can only add value in a left/right child if the child is None
# if the child is NOT None, we need to move down to the next node
# need some way to re-apply decision on each layer we encounter while loop            
# use a temp node to represent the current node we're testing against       
                