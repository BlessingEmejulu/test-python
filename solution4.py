# Searching for a value in a BST
# To find a value in BST, we start at the root and compare the value with the data of the current node. If the value is equal to the data of the current node, we return True. If the value is less than the data of the current node, we search in the left subtree. If the value is greater than the data of the current node, we search in the right subtree. We continue this process until we find the value or reach a leaf node (i.e., a node with no children).

# The following code snippet demonstrates how to search for a value in a BST:

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to search a given key in BST
def search(root, key):
    # Base Cases: root is null or key is present at root
    if root is None or root.data == key:
        return root
    # Key is greater than root's key
    if root.data < key:
        return search(root.right, key)
    # Key is smaller than root's key
    return search(root.left, key)

# Create a BST tree
root = Node(10)
root.left = Node(3)
root.right = Node(15)
root.left.left = Node(1)
root.left.right = Node(5)
root.left.right.left = Node(4)
root.left.right.right = Node(7)
root.right.left = Node(12)
root.right.right = Node(20)
root.right.left.left = Node(11)
root.right.right.left = Node(18)

# Search for a value in the BST tree
key = 7
result = search(root, key)
if result:
    print("Value found in the BST tree")
else:
    print("Value NOT found in the BST tree")