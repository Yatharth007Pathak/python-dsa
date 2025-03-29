"""
Given a Binary Tree. Check for the Sum Tree for every node except the leaf node. Return true if it is a Sum Tree otherwise, return false.

A SumTree is a Binary Tree where the value of a node is equal to the sum of the nodes present in its left subtree and right subtree. 
An empty tree is also a Sum Tree as the sum of an empty tree can be considered to be 0. A leaf node is also considered a Sum Tree.

Examples:

Input:
    3
  /   \    
 1     2
Output: true
Explanation: The sum of left subtree and right subtree is 1 + 2 = 3, which is the value of the root node. 
Therefore,the given binary tree is a sum tree.

Input:
          10
        /    \
      20      30
    /   \ 
   10    10
Output: false
Explanation: The given tree is not a sum tree. For the root node, 
sum of elements in left subtree is 40 and sum of elements in right subtree is 30. Root element = 10 which is not equal to 30+40.

Input:
   25
  /   \    
 9     15
Output: false
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def is_sum_tree(self, node):
        # Helper function to check the sum property and calculate the total sum
        def check_sum_tree(root):
            if root is None:  # An empty tree is a sum tree
                return True, 0
            if root.left is None and root.right is None:  # Leaf nodes are sum trees
                return True, root.data
            
            # Recursively check left and right subtrees
            left_is_sum_tree, left_sum = check_sum_tree(root.left)
            right_is_sum_tree, right_sum = check_sum_tree(root.right)
            
            # Check the current node's value against the sum of its subtrees
            current_is_sum_tree = (root.data == left_sum + right_sum)
            
            # Return True if current tree is a Sum Tree, along with the total sum
            return (
                left_is_sum_tree and right_is_sum_tree and current_is_sum_tree,
                left_sum + right_sum + root.data
            )
        
        # Only return the boolean result from the helper function
        is_sum_tree, _ = check_sum_tree(node)
        return is_sum_tree

root = Node(3)
root.left = Node(1)
root.right = Node(2)
solution = Solution()
print(solution.is_sum_tree(root))  # Output: True


root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(10)
root.left.right = Node(10)
solution = Solution()
print(solution.is_sum_tree(root))  # Output: False

'''
Here's a line-by-line breakdown of the code:

class Solution:
Declares a class named Solution. It will hold the method to check if a binary tree is a sum tree.

def is_sum_tree(self, node):
Defines the method is_sum_tree, which determines if the given binary tree rooted at node satisfies the sum tree property.

def check_sum_tree(root):
Declares a helper function check_sum_tree inside is_sum_tree. 
This function recursively verifies the sum tree property and calculates the sum of the subtree rooted at root.

if root is None:
Checks if the current node (root) is None. An empty tree is considered a sum tree.

return True, 0
For an empty tree, returns True (it is a sum tree) and the sum as 0.

if root.left is None and root.right is None:
Checks if the current node is a leaf (both left and right children are None). A leaf node is also considered a sum tree.

return True, root.data
Returns True (it is a sum tree) and the value of the leaf node as its sum.

left_is_sum_tree, left_sum = check_sum_tree(root.left)
Recursively checks if the left subtree is a sum tree and calculates the sum of its nodes.

right_is_sum_tree, right_sum = check_sum_tree(root.right)
Similarly, checks if the right subtree is a sum tree and calculates the sum of its nodes.

current_is_sum_tree = (root.data == left_sum + right_sum)
Verifies if the current node satisfies the sum tree property: the node's value must equal the sum of its left and right subtrees.

return (left_is_sum_tree and right_is_sum_tree and current_is_sum_tree, left_sum + right_sum + root.data)
Returns a tuple:
True if the current tree (rooted at root) is a sum tree. 
This requires that both subtrees are sum trees and the current node satisfies the sum tree property.
The total sum of the subtree rooted at root.

is_sum_tree, _ = check_sum_tree(node)
Calls the helper function check_sum_tree with the root node. 
The result is unpacked to get whether the tree is a sum tree (is_sum_tree), ignoring the total sum (_).

return is_sum_tree
Returns the result of whether the tree is a sum tree.

Example 1:

root = Node(3)
Creates the root node with value 3.

root.left = Node(1)
Creates the left child of the root with value 1.

root.right = Node(2)
Creates the right child of the root with value 2.

solution = Solution()
Creates an instance of the Solution class.

print(solution.is_sum_tree(root))
Outputs True because the tree satisfies the sum tree property (3 = 1 + 2).

Example 2:

root = Node(10)
Creates the root node with value 10.

root.left = Node(20)
Creates the left child of the root with value 20.

root.right = Node(30)
Creates the right child of the root with value 30.

root.left.left = Node(10)
Adds a left child to the left child of the root with value 10.

root.left.right = Node(10)
Adds a right child to the left child of the root with value 10.

print(solution.is_sum_tree(root))
Outputs False because the tree does not satisfy the sum tree property (10 ≠ 20 + 30).
'''