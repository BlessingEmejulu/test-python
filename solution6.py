# Deleting a node from a BST

# To delete a node from a BST, we need to consider three cases:
# 1. The node to be deleted is a leaf node (i.e., it has no children).
# 2. The node to be deleted has one child.
# 3. The node to be deleted has two children.

# In the first case, we simply remove the node from the tree.
# In the second case, we replace the node with its child.
# In the third case, we find the inorder successor of the node to be deleted (i.e., the smallest node in the right subtree of the node) and replace the node with the inorder successor.

# The following code snippet demonstrates how to delete a node from a BST:

# Deleting a node from a BST
# node class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current.data

def delete_node(root, key):
    if root is None:
        return root
    if key < root.data:
        root.left = delete_node(root.left, key)
    elif key > root.data:
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        root.data = find_min(root.right)
        root.right = delete_node(root.right, root.data)
    return root

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

# Delete a node from the BST tree
key = 15
root = delete_node(root, key)

def inorder_traversal(root):
    if root is not None:
        inorder_traversal(root.left)
        print(root.data, end=' ')
        inorder_traversal(root.right)

# Print the BST tree after deleting the node
print("The BST tree after deleting the node with key", key, "is:")
inorder_traversal(root)
print()
