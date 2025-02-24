# Trees are hierarchical data structures with nodes connected by edges.

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Creating nodes
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)