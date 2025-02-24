# Linked lists are linear data structures where 
# each element is a separate object.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
# Creating nodes
node01 = Node(1)
node02 = Node(2)
node03 = Node(3)

# Linking nodes
node01.next = node02
node02.next = node03
