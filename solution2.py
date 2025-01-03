#To check the Height of a BST
# The following numbers are inserted into an empty BST in the given order:  10,1,3,5,15,12,16.
# What is the height of the BST? 

# A. 7 B. 4 C. 3 D. 5
# Answer: C. 3

# Explanation: The height of a binary search tree (BST) is the maximum number of edges in the longest path from the root to a leaf node.
# In this case, the numbers are inserted in the following order: 10, 1, 3, 5, 15, 12, 16.
# The resulting BST has the following structure:

#       10
#      /  \
#     1    15
#      \   / \
#       3 12 16
#        \
#         5

# The longest path from the root to a leaf node is 10 -> 1 -> 3 -> 5, which has a height of 3.  
# Therefore, the height of the BST is 3.

#To check the Height of a BST using a recursive approach
# We can define a helper function height(node) that returns the height of the subtree rooted at node.
# The base case is when the node is None, in which case we return -1 (since the height of an empty tree is -1).
# We recursively calculate the height of the left and right subtrees and return the maximum height plus 1 (to account for the current node).
# Finally, we call the helper function with the root node of the binary tree to get the height of the entire tree.
#
# The following code snippet demonstrates how to calculate the height of a binary tree using a recursive approach:
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Helper function to calculate the height of a binary tree
def height(node):
    if node is None:
        return -1
    return max(height(node.left), height(node.right)) + 1

# Construct a binary search tree
root = TreeNode(10)
root.left = TreeNode(1)
root.left.right = TreeNode(3)
root.left.right.right = TreeNode(5)
root.right = TreeNode(15)
root.right.left = TreeNode(12)
root.right.right = TreeNode(16)

# Calculate the height of the tree
print("The height of the tree is:", height(root))
# The height of the tree is: 3
