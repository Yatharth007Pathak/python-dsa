"""
Given a Binary Tree, convert it into its mirror.

Examples:

Input:
      1
    /  \
   2    3
Output: 3 1 2
Explanation: The tree is
  1      (mirror)     1
 /  \       =>       /  \
2    3              3    2
The inorder of mirror is 3 1 2

Input:
      10
     /  \
    20   30
   /  \
  40  60
Output: 30 10 60 20 40
Explanation: The tree is
      10                     10
    /    \     (mirror)    /    \
   20    30       =>      30    20
  /  \                         /   \
 40  60                       60   40
The inroder traversal of mirror is: 30 10 60 20 40.
"""

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    # Function to convert a binary tree into its mirror tree.
    def mirror(self, root):
        # Base case: If root is None, do nothing
        if root is None:
            return
        
        # Recursively convert left and right subtrees to their mirrors
        self.mirror(root.left)
        self.mirror(root.right)
        
        # Swap the left and right children of the current node
        root.left, root.right = root.right, root.left

    # Function for inorder traversal of the tree
    def inorderTraversal(self, root):
        if root is None:
            return []
        # Inorder traversal: left -> root -> right
        return self.inorderTraversal(root.left) + [root.data] + self.inorderTraversal(root.right)

# Example usage
if __name__ == "__main__":
    # Create the binary tree
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    
    # Create Solution object
    solution = Solution()
    
    # Convert to mirror
    solution.mirror(root)
    
    # Print the inorder traversal of the mirror tree
    print(solution.inorderTraversal(root))  # Output: [3, 1, 2]

    # Another example
    root2 = Node(10)
    root2.left = Node(20)
    root2.right = Node(30)
    root2.left.left = Node(40)
    root2.left.right = Node(60)
    
    solution.mirror(root2)
    print(solution.inorderTraversal(root2))  # Output: [30, 10, 60, 20, 40]

'''
This code defines a Solution class that provides methods to convert a binary tree into its mirror 
and to perform an inorder traversal of the tree.

Breakdown of the Code:

Node Class:
The Node class defines the structure of a binary tree node with three attributes: data, left, and right.
data stores the value of the node, while left and right point to the left and right child nodes, respectively.

mirror Function:
The mirror function converts a binary tree into its mirror.
Base Case: If the node is None, the function returns immediately (no action is required).
Recursive Case: The function recursively mirrors the left and right subtrees. 
After that, it swaps the left and right child nodes of the current node.
This process mirrors the binary tree by flipping it at every level.

inorderTraversal Function:
This function performs an inorder traversal of the tree. It visits nodes in the following order: left subtree -> root node -> right subtree.
The function returns a list containing the data from the inorder traversal.

Example Usage:
Two example binary trees are constructed to demonstrate the functionality.
The mirror function is called to convert the trees into their mirror images, 
and then the inorderTraversal function is used to print the inorder traversal of the mirrored trees.

Key Points:
Time Complexity: Both mirror and inorderTraversal functions take O(n) time, where n is the number of nodes in the binary tree.
Space Complexity: The space complexity is O(h) due to the recursion stack, where h is the height of the tree.
'''