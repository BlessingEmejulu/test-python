# To check if a binary tree is a binary search tree (BST), we can use a recursive approach.
# We define a helper function is_bst(node, min_value, max_value) that returns True if the subtree rooted at node is a BST and all its nodes have values within the range [min_value, max_value].
# The function returns False if the subtree violates the BST property.
# The base case is when the node is None, in which case we return True.
# We check if the current node violates the BST property by comparing its value with the min_value and max_value.
# If the current node violates the BST property, we return False.
# Otherwise, we recursively check the left and right subtrees, updating the range of valid values.
# Finally, we call the helper function with the root node of the binary tree to check if it is a BST.

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_bst(node, min_value=float('-inf'), max_value=float('inf')):
    # Base case: an empty tree is a BST
    if node is None:
        return True
    
    # Check if the current node violates the BST property
    if not (min_value < node.value < max_value):
        return False
    
    # Recursively check the left and right subtrees
    return (is_bst(node.left, min_value, node.value) and
            is_bst(node.right, node.value, max_value))

# Construct a binary tree
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.left.left = TreeNode(2)
root.left.right = TreeNode(7)

# Check if the tree is a BST
print("The tree is a BST" if is_bst(root) 
      else "The tree is not a BST")

# The tree is a BST
