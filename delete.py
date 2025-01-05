class TreeNode:
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

# Example Usage
root = TreeNode(50)
root.left = TreeNode(30)
root.right = TreeNode(70)
root.left.left = TreeNode(20)
root.left.right = TreeNode(40)
root.right.left = TreeNode(60)
root.right.right = TreeNode(80)

print("Original BST:")
in_order(root)
print("\nDeleting 50...")
root = delete_node(root, 50)
print("BST after deletion:")
in_order(root)
