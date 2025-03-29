"""
Given a Binary Tree. Check whether it is Symmetric or not, i.e. whether the binary tree is a Mirror image of itself or not.

Example 1:
Input:
         5
       /   \
      1     1
     /       \
    2         2
Output: True
Explanation: Tree is mirror image of itself i.e. tree is symmetric

Example 2:
Input:
         5
       /   \
      10     10
     /  \     \
    20  20     30
Output: False
"""

class Solution:
    # Function to check whether the tree is symmetric or not
    def isSymmetric(self, root):
        # An empty tree is symmetric
        if root is None:
            return True
        
        # Helper function to compare two subtrees
        def isMirror(left, right):
            # If both subtrees are empty, they are symmetric
            if left is None and right is None:
                return True
            
            # If only one subtree is empty or values are different, not symmetric
            if left is None or right is None or left.data != right.data:
                return False
            
            # Check if the left subtree of left and the right subtree of right are mirrors
            # and if the right subtree of left and the left subtree of right are mirrors
            return isMirror(left.left, right.right) and isMirror(left.right, right.left)
        
        # Start the comparison with the left and right subtrees of the root
        return isMirror(root.left, root.right)

# Example usage
class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = val

if __name__ == "__main__":
    # Construct the tree for Example 1:
    root = Node(5)
    root.left = Node(1)
    root.right = Node(1)
    root.left.left = Node(2)
    root.right.right = Node(2)
    
    solution = Solution()
    print(solution.isSymmetric(root))  # Output: True

    # Construct the tree for Example 2:
    root2 = Node(5)
    root2.left = Node(10)
    root2.right = Node(10)
    root2.left.left = Node(20)
    root2.left.right = Node(20)
    root2.right.right = Node(30)
    
    print(solution.isSymmetric(root2))  # Output: False

'''
This code defines a Solution class that contains a method isSymmetric to check whether a binary tree is symmetric. 
A symmetric tree is one that is a mirror of itself.

Explanation:

Node Class:
The Node class defines a binary tree node with data, left, and right attributes.

isSymmetric Function:
This function checks if a tree is symmetric by using a helper function isMirror.
Base Case: If the tree is empty (root is None), it is symmetric, so the function returns True.
The main idea is to check if the left and right subtrees are mirrors of each other.

isMirror Function (Helper):
This recursive function compares two nodes (left and right).

Base Cases:
If both nodes are None, they are symmetric.
If one node is None and the other is not, they are not symmetric.
If the data of the nodes is different, they are not symmetric.

Recursive Case:
It checks the following conditions:
The left subtree of the left node should mirror the right subtree of the right node.
The right subtree of the left node should mirror the left subtree of the right node.
This recursive call ensures that the tree is symmetric.

Example Usage:
Two binary trees are constructed to test the isSymmetric function.

Example 1:
Initial Tree:
      5
     / \
    1   1
   /     \
  2       2
This tree is symmetric because the left subtree mirrors the right subtree. Therefore, isSymmetric(root) will return True.

Example 2:
Initial Tree:
      5
     / \
    10  10
   /  \    \
  20  20   30
This tree is not symmetric because the right subtree does not mirror the left subtree (the right subtree has an extra node 30). 
Therefore, isSymmetric(root2) will return False.

Key Points:
Time Complexity: The time complexity is O(n), where n is the number of nodes, as each node is visited once.
Space Complexity: The space complexity is O(h), where h is the height of the tree due to the recursion stack.
'''