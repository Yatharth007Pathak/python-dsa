"""
Given a Binary Tree. Find the sum of all the leaf nodes that are left child of their parent of the given binary tree.

Examples:

Input:
       1
     /   \
    2     3
Output: 2

Input : 
         1
        /  \
       2    3
     /  \     \
    4    5     8 
  /  \        /  \
 7    2      6    9
Output: 13
Explanation: sum = 6 + 7 = 13
"""

# Node class definition
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    # Function to calculate the sum of all left leaves
    def leftLeavesSum(self, root):
        # Helper function to check if a node is a leaf
        def isLeaf(node):
            return node is not None and node.left is None and node.right is None

        # Base case: If root is None, return 0
        if root is None:
            return 0

        # Initialize sum
        total_sum = 0

        # If left child exists and it is a leaf, add its value to the sum
        if root.left and isLeaf(root.left):
            total_sum += root.left.data

        # Recursively calculate sum for left and right subtrees
        total_sum += self.leftLeavesSum(root.left)
        total_sum += self.leftLeavesSum(root.right)

        return total_sum

# Example usage:
solution = Solution()

# Example 1:
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
print(solution.leftLeavesSum(root1))  # Output: 2

# Example 2:
root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)
root2.left.left = Node(4)
root2.left.right = Node(5)
root2.left.left.left = Node(7)
root2.left.left.right = Node(2)
root2.right.right = Node(8)
root2.right.right.left = Node(6)
root2.right.right.right = Node(9)
print(solution.leftLeavesSum(root2))  # Output: 13 (6 + 7)

'''
Here's a line-by-line breakdown of the code:

class Node:
Defines a class Node, which represents a node in a binary tree.

def __init__(self, val):
Initializes a new instance of the Node class.

self.data = val
Sets the node's value to val.

self.left = None
Initializes the left child of the node to None.

self.right = None
Initializes the right child of the node to None.

class Solution:
Defines a class Solution, which contains a method to calculate the sum of all left leaves in a binary tree.

def leftLeavesSum(self, root):
Defines a method leftLeavesSum that takes one parameter: root, the root of the binary tree.

def isLeaf(node):
Defines a helper function isLeaf that checks if a given node is a leaf (i.e., it has no children).

return node is not None and node.left is None and node.right is None
Returns True if the node is not None and both its left and right children are None; otherwise, it returns False.

if root is None:
Checks if the root is None. This serves as the base case for the recursion.

return 0
Returns 0 if the root is None, indicating that there are no left leaves to sum.

total_sum = 0
Initializes a variable total_sum to 0. This will hold the cumulative sum of all left leaves.

if root.left and isLeaf(root.left):
Checks if the left child of the root exists and if it is a leaf.

total_sum += root.left.data
If the left child is a leaf, adds its value (root.left.data) to total_sum.

total_sum += self.leftLeavesSum(root.left)
Recursively calculates the sum of left leaves for the left subtree and adds it to total_sum.

total_sum += self.leftLeavesSum(root.right)
Recursively calculates the sum of left leaves for the right subtree and adds it to total_sum.

return total_sum
Returns the final total_sum of all left leaves in the binary tree.

Example usage:
solution = Solution()
Creates an instance of the Solution class.
Example 1:
root1 = Node(1)
Creates a binary tree with 1 as the root node.

root1.left = Node(2)
Adds 2 as the left child of the root.

root1.right = Node(3)
Adds 3 as the right child of the root.

print(solution.leftLeavesSum(root1))
Calls the leftLeavesSum method with root1 and prints the result, which is 2. In this tree, 2 is the only left leaf.

Example 2:
root2 = Node(1)
Creates a more complex binary tree with 1 as the root node.

root2.left = Node(2)
Adds 2 as the left child of the root.

root2.right = Node(3)
Adds 3 as the right child of the root.

root2.left.left = Node(4)
Adds 4 as the left child of node 2.

root2.left.right = Node(5)
Adds 5 as the right child of node 2.

root2.left.left.left = Node(7)
Adds 7 as the left child of node 4.

root2.left.left.right = Node(2)
Adds another 2 as the right child of node 4.

root2.right.right = Node(8)
Adds 8 as the right child of node 3.

root2.right.right.left = Node(6)
Adds 6 as the left child of node 8.

root2.right.right.right = Node(9)
Adds 9 as the right child of node 8.

print(solution.leftLeavesSum(root2))
Calls the leftLeavesSum method with root2 and prints the result, which is 13 (the sum of the left leaves 6 and 7).
'''