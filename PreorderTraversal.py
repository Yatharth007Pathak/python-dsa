"""
Given a binary tree, find its preorder traversal.
In preorder traversal, nodes are visited in the order of: root, left subtree, and then right subtree. 
The output from each tree is displayed in the format specified in the print statements.

Examples:

Input:
        1      
      /          
    4    
  /    \   
4       2
Output: [1, 4, 4, 2]

Input:
       6
     /   \
    3     2
     \   / 
      1 2
Output: [6, 3, 1, 2, 2] 

Input:
         8
       / \
      3   10
     / \    \
    1   6   14
       / \   /
      4   7 13
Output: [8, 3, 1, 6, 4, 7, 10, 14, 13]
"""

# Node Class
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    # Function to return a list containing the preorder traversal of the tree.
    def preorder(self, root):
        # Recursive approach
        result = []
        self._preorder_helper(root, result)
        return result

    def _preorder_helper(self, node, result):
        if node:
            result.append(node.data)  # Visit the root
            self._preorder_helper(node.left, result)  # Traverse left
            self._preorder_helper(node.right, result)  # Traverse right

# Test Cases
if __name__ == "__main__":
    # Example 1
    root1 = Node(1)
    root1.left = Node(4)
    root1.left.left = Node(4)
    root1.left.right = Node(2)
    
    solution = Solution()
    print("Preorder Traversal of Tree 1:", solution.preorder(root1))  # Output: [1, 4, 4, 2]

    # Example 2
    root2 = Node(6)
    root2.left = Node(3)
    root2.left.right = Node(1)
    root2.right = Node(2)
    root2.right.left = Node(2)
    
    print("Preorder Traversal of Tree 2:", solution.preorder(root2))  # Output: [6, 3, 1, 2, 2]

    # Example 3
    root3 = Node(8)
    root3.left = Node(3)
    root3.right = Node(10)
    root3.left.left = Node(1)
    root3.left.right = Node(6)
    root3.left.right.left = Node(4)
    root3.left.right.right = Node(7)
    root3.right.right = Node(14)
    root3.right.right.left = Node(13)
    
    print("Preorder Traversal of Tree 3:", solution.preorder(root3))  # Output: [8, 3, 1, 6, 4, 7, 10, 14, 13]

'''
Here's a line-by-line breakdown of the provided code:

Define a class Node: This class represents a single node in a binary tree.

Initialize the Node class with a value: The constructor takes a value val and assigns it to the node’s data attribute.

Set left and right attributes to None: These attributes represent the left and right children of the node and are initially set to None.

Define a class Solution: This class will contain methods to perform operations on the binary tree.

Define the method preorder within Solution: This method takes the root of the tree as an argument and 
returns a list of values from a preorder traversal.

Initialize an empty list called result: This list will store the values of nodes visited during the traversal.

Call the helper method _preorder_helper: This method performs the actual traversal, taking the root node and the result list as arguments.

Return the result list: After the traversal is complete, return the list containing the values in preorder.

Define the helper method _preorder_helper: This method takes a node and the result list as 
arguments to perform the recursive preorder traversal.

Check if the current node is not None: If the node exists, proceed with the traversal.

Append the node's value to the result list: This marks the visit to the root node.

Recursively call _preorder_helper for the left child: This traverses the left subtree.

Recursively call _preorder_helper for the right child: This traverses the right subtree after finishing the left subtree.

Begin testing the traversal in the main block: This block runs when the script is executed directly.

Create the first tree (root1): Initialize nodes and set their left and right children to create a specific tree structure.

Instantiate the Solution class: Create an instance to use the preorder method.

Print the preorder traversal of Tree 1: Call the preorder method with root1 and display the result.

Create the second tree (root2): Initialize another tree structure with different nodes.

Print the preorder traversal of Tree 2: Call the preorder method with root2 and display the result.

Create the third tree (root3): Initialize a more complex tree structure with multiple levels.

Print the preorder traversal of Tree 3: Call the preorder method with root3 and display the result.
'''