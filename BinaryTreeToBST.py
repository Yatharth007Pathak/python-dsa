"""
Given a Binary Tree, convert it to Binary Search Tree in such a way that keeps the original structure of Binary Tree intact.
 
Example 1:
Input:
      1
    /   \
   2     3
Output: 1 2 3
Explanation: The converted BST will be 
      2
    /   \
   1     3


Example 2:
Input:
          1
       /    \
     2       3
   /        
 4       
Output: 1 2 3 4
Explanation:The converted BST will be
        3
      /   \
    2      4
  /
 1
"""

# Tree Node class
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    # Helper function to perform an in-order traversal and collect node values
    def inorderTraversal(self, root, inorder):
        if root is None:
            return
        self.inorderTraversal(root.left, inorder)
        inorder.append(root.data)
        self.inorderTraversal(root.right, inorder)
    
    # Helper function to assign the sorted values to the Binary Tree in in-order fashion
    def convertToBST(self, root, sorted_values, index):
        if root is None:
            return index
        
        # Traverse left subtree
        index = self.convertToBST(root.left, sorted_values, index)
        
        # Assign value from sorted_values to the current node
        root.data = sorted_values[index]
        index += 1
        
        # Traverse right subtree
        index = self.convertToBST(root.right, sorted_values, index)
        
        return index

    # Function to convert Binary Tree to Binary Search Tree
    def binaryTreeToBST(self, root):
        if root is None:
            return None
        
        # Step 1: Collect all node values from the Binary Tree
        inorder = []
        self.inorderTraversal(root, inorder)
        
        # Step 2: Sort the node values
        inorder.sort()
        
        # Step 3: Reassign the sorted values back to the Binary Tree to convert it to BST
        self.convertToBST(root, inorder, 0)
        
        return root

# Helper function to print the in-order traversal of the tree (for checking the BST)
def printInorder(root):
    if root is None:
        return
    printInorder(root.left)
    print(root.data, end=' ')
    printInorder(root.right)

# Example usage:
# Binary Tree construction
root = Node(1)
root.left = Node(2)
root.right = Node(3)

# Convert to Binary Search Tree
solution = Solution()
solution.binaryTreeToBST(root)

# Print the in-order traversal of the converted BST
printInorder(root)

'''
Here's a breakdown of the code line by line:

class Node:
This defines a class Node, which will represent a node in a binary tree.

def __init__(self, val):
Initializes the Node class. This is the constructor method that will be called when a new node object is created.

self.right = None
Creates an attribute right for the Node object and initializes it to None. 
This attribute will hold the reference to the right child of the node.

self.data = val
Sets the data attribute of the node, which stores the value (in this case, val) passed to the constructor.

self.left = None
Creates an attribute left for the Node object and initializes it to None. 
This attribute will hold the reference to the left child of the node.

class Solution:
Defines a class Solution, which will contain methods to convert a binary tree into a binary search tree (BST).

def inorderTraversal(self, root, inorder):
Defines a helper method to perform an in-order traversal of the binary tree. 
It takes the root of the tree and an empty list inorder to store node values in in-order sequence.

if root is None:
Checks if the current node (root) is None. If true, it returns and stops further recursion.

self.inorderTraversal(root.left, inorder)
Recursively traverses the left subtree of the binary tree.

inorder.append(root.data)
Appends the value of the current node (root.data) to the list inorder.

self.inorderTraversal(root.right, inorder)
Recursively traverses the right subtree of the binary tree.

def convertToBST(self, root, sorted_values, index):
Defines a helper method to assign sorted values back to the binary tree, converting it into a BST. 
It takes the root, a list of sorted values, and an index to track the current position in the list.

if root is None:
Checks if the current node is None. If true, returns the current index value.

index = self.convertToBST(root.left, sorted_values, index)
Recursively traverses the left subtree and updates the index.

root.data = sorted_values[index]
Assigns the sorted value at the current index to the node’s data attribute.

index += 1
Increments the index to move to the next value in the sorted list.

index = self.convertToBST(root.right, sorted_values, index)
Recursively traverses the right subtree and updates the index.

return index
Returns the current index after processing both subtrees.

def binaryTreeToBST(self, root):
Defines a function to convert the given binary tree into a binary search tree (BST). It accepts the root of the tree.

if root is None:
Checks if the tree is empty. If true, returns None.

inorder = []
Creates an empty list inorder to store the in-order traversal of the tree.

self.inorderTraversal(root, inorder)
Calls the helper method to collect the in-order traversal of the binary tree.

inorder.sort()
Sorts the collected node values to convert them into the form required for a BST.

self.convertToBST(root, inorder, 0)
Calls the helper method to reassign the sorted values to the tree, thus converting it into a BST.

return root
Returns the root of the converted BST.

def printInorder(root):
Defines a function to print the in-order traversal of the tree.

if root is None:
Checks if the tree is empty. If true, returns without printing.

printInorder(root.left)
Recursively prints the left subtree in in-order sequence.

print(root.data, end=' ')
Prints the value of the current node, followed by a space.

printInorder(root.right)
Recursively prints the right subtree in in-order sequence.

root = Node(1)
Creates a root node with the value 1.

root.left = Node(2)
Creates a left child node with the value 2.

root.right = Node(3)
Creates a right child node with the value 3.

solution = Solution()
Creates an object solution of the Solution class.

solution.binaryTreeToBST(root)
Calls the method to convert the binary tree into a binary search tree.

printInorder(root)
Prints the in-order traversal of the converted BST.
'''