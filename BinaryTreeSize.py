"""
Given a binary tree, you have to return the size of it. Size of binary tree is defined as number of nodes in it.

Examples:

Input:      
       1
     /  \
    2    3
Output: 3
Explanation: There are three nodes in given binary tree.
Input:
      10
     /  \
   5     9
   \    / \
    1  3   6
Output: 6
Explanation: There are six nodes in given binary tree.
"""

from typing import Optional
from collections import deque

# Definition of the binary tree node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def getSize(self, node: Optional[Node]) -> int:
        # Base case: if the node is None, return size as 0
        if node is None:
            return 0
        
        # Recursively compute the size of left and right subtrees and add 1 for the current node
        left_size = self.getSize(node.left)
        right_size = self.getSize(node.right)
        
        return 1 + left_size + right_size

# Helper function to create example trees for testing
def createExampleTree1():
    """
    Example 1:
          1
        /   \
       2     3
    """
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    return root

def createExampleTree2():
    """
    Example 2:
          10
         /   \
        5     9
         \   /  \
          1 3    6
    """
    root = Node(10)
    root.left = Node(5)
    root.right = Node(9)
    root.left.right = Node(1)
    root.right.left = Node(3)
    root.right.right = Node(6)
    return root

# Driver code to test the examples
def main():
    solution = Solution()
    
    # Test Example 1
    root1 = createExampleTree1()
    print("Size of Example 1 Tree:", solution.getSize(root1))  # Output: 3
    
    # Test Example 2
    root2 = createExampleTree2()
    print("Size of Example 2 Tree:", solution.getSize(root2))  # Output: 6

if __name__ == "__main__":
    main()

'''
The code defines a binary tree structure and a method to calculate the number of nodes in a given binary tree. 
It tests this functionality using two example trees. The size is computed recursively by adding the sizes of the left and right 
subtrees plus one for the root node itself.



Here's a breakdown of the provided code, which calculates the size of a binary tree:

Node Class:
class Node:
Defines a class Node, representing a node in a binary tree.

def __init__(self, val):
Constructor for the Node class, which initializes the node with:

self.data = val
Stores the value of the node (val) in the data attribute.

self.left = None
Initializes the left child of the node as None.

self.right = None
Initializes the right child of the node as None.

Solution Class:
class Solution:
Defines a class Solution, which contains methods to work with the binary tree.

def getSize(self, node: Optional[Node]) -> int:
This method computes the size of the binary tree rooted at the given node. 
The method is annotated with Optional[Node], indicating that the input may be a Node or None.

if node is None:
Checks if the current node is None. This is the base case for recursion.

return 0
If the node is None, it returns 0 as the size of the tree.

left_size = self.getSize(node.left)
Recursively computes the size of the left subtree.

right_size = self.getSize(node.right)
Recursively computes the size of the right subtree.

return 1 + left_size + right_size
Returns the total size by adding 1 (for the current node) to the sizes of the left and right subtrees.

Helper Functions to Create Example Trees:
def createExampleTree1():
Creates the first example tree based on the diagram in the docstring.

Creates the tree structure:
      1
    /   \
   2     3
The root node has two children.

return root
Returns the root of the first example tree.

def createExampleTree2():
Creates the second example tree based on the diagram in the docstring.

Creates the tree structure:
      10
     /   \
    5     9
     \   /  \
      1 3    6
This tree has a more complex structure with various child nodes.

return root
Returns the root of the second example tree.

Driver Code to Test the Examples:
def main():
Defines the main function to test the getSize method.

solution = Solution()
Creates an instance of the Solution class.

root1 = createExampleTree1()
Creates the first example tree.

print("Size of Example 1 Tree:", solution.getSize(root1))
Calls getSize on the first tree and prints the result. The expected output is 3, as there are three nodes.

root2 = createExampleTree2()
Creates the second example tree.

print("Size of Example 2 Tree:", solution.getSize(root2))
Calls getSize on the second tree and prints the result. The expected output is 6, as there are six nodes.

Main Block:
if __name__ == "__main__":
This line ensures that the main() function runs only when the script is executed directly, not when imported as a module.

main()
Calls the main() function to execute the test cases.
'''