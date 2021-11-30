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
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child
            
        if new_value < prev_node.data:
            prev_node.left_child = node
        else:
            prev_node.right_child = node
            
    def search_node(self, data):
        if self.root == data:
            print("Node is found!")
        if data < self.root:
            if self.left_child:
                self.left_child.search(data)
            else:
                print("Node is not present in tree!")
        else:
            if self.right_child:
                self.right_child(data)
            else:
                print("Node is not present in tree!")
        
                
        
        
            
            
           
            
            

# can only add value in a left/right child if the child is None
# if the child is NOT None, we need to move down to the next node
# need some way to re-apply decision on each layer we encounter while loop            
# use a temp node to represent the current node we're testing against       
                