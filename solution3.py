# Finding the minimum and maximum value in a BST

#THE SOLUTION
# To find the minimum value in a BST, we need to go to the left child of the root, then go to the left child of that child, and so on, until we come to a node that has no left child. This node is the minimum value in the BST.

# To find the maximum value in a BST, we need to start at the root and follow the right child links until they end. The node at which the right child link ends is the maximum value in the BST.

#EXPLAIN THE CODE
# We define a function find_min that takes the root of the BST as input and returns the minimum value in the BST.
# If the root is None, we return None.
# If the left child of the root is None, we return the data of the root.
# Otherwise, we recursively call the find_min function on the left child of the root.
# We define a function find_max that takes the root of the BST as input and returns the maximum value in the BST.
# If the root is None, we return None.
# If the right child of the root is None, we return the data of the root.
# Otherwise, we recursively call the find_max function on the right child of the root.

#IMPLEMENTATION

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Function to find the minimum value in a BST
def find_min(root):
    if root is None:
        return None
    if root.left is None:
        return root.data
    return find_min(root.left)

# Function to find the maximum value in a BST
def find_max(root):
    if root is None:
        return None
    if root.right is None:
        return root.data
    return find_max(root.right)


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

print("The minimum value in the BST tree is: ", find_min(root))
print("The maximum value in the BST tree is: ", find_max(root))