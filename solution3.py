# Finding the minimum and maximum value in a BST
# For the minimum, go to the left child of the root; then go to the left child of that child, and so on, until you come to a node that has no left child. This node is the minimum. Similarly, for the maximum, start at the root and follow the right child links until they end.

# Example: Find the minimum and maximun value in the following BST tree in this order; 10,1,15,3,7,12,20,4,5,11,18

# The minimum value is 1 and the maximum value is 20

# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def find_min(root):
    if root is None:
        return None
    if root.left is None:
        return root.data
    return find_min(root.left)

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