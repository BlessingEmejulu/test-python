# Steps to Delete a Node from a BST
# Case 1: The Node is a Leaf (No Children)
# Simply remove the node from the tree.
# Case 2: The Node Has One Child
# Replace the node with its child.
# Case 3: The Node Has Two Children
# Replace the node with:
# Inorder Successor (smallest node in the right subtree), or
# Inorder Predecessor (largest node in the left subtree).
# Delete the successor/predecessor from its original position.

# Pseudo code for  Deleting node in BST
# we define our node class
# we define our function to delete a node in BST
# we define our helper function to find the minimum node in the right subtree
# we define our helper function to perform an inorder traversal of the BST
# we create a BST tree
# we delete a node from the BST tree
# we print the BST tree after deleting the node


# Deleting a node from a BST

# node class
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def delete_node(root, key):
    if root is None:
        return root

    # Traverse the tree to find the node
    if key < root.key:
        root.left = delete_node(root.left, key)
    elif key > root.key:
        root.right = delete_node(root.right, key)
    else:
        # Case 1: Node has no children (leaf node)
        if root.left is None and root.right is None:
            return None

        # Case 2: Node has one child
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        # Case 3: Node has two children
        # Find the inorder successor (smallest in the right subtree)
        min_node = find_min(root.right)
        root.key = min_node.key
        # Delete the inorder successor
        root.right = delete_node(root.right, min_node.key)

    return root

def find_min(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

# Helper function to print tree in-order
def in_order(root):
    if root:
        in_order(root.left)
        print(root.key, end=" ")
        in_order(root.right)

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

print("Original BST:")
in_order(root)
print("\nDeleting 15...")
root = delete_node(root, 15)
print("BST after deletion:")
in_order(root)
