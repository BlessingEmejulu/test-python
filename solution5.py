# Inserting a value into BST

# To insert a value into a BST, we start at the root and compare the value with the data of the current node. If the value is less than the data of the current node and the left child is None, we insert the value as the left child of the current node. If the value is greater than the data of the current node and the right child is None, we insert the value as the right child of the current node. If the left or right child is not None, we recursively insert the value into the left or right subtree, respectively.

# The following code snippet demonstrates how to insert a value into a BST:

# Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Function to insert a value into a BST
def insert(root, value):
    if not root:
        return TreeNode(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

# Helper function to perform an inorder traversal of the BST
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.value, end=' ')
        inorder_traversal(root.right)

# Create a REAL bst AND INSERT THE VALUE 8 IN IT
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.left = Node(12)
root.right.right = Node(18)

value = 8
print("The BST tree before inserting the value", value, "is:")
inorder_traversal(root)
print()