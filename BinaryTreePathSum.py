"""
Given a binary tree in which each node element contains a number. 
Find the maximum possible path sum from one special node to another special node.

Note: Here special node is a node which is connected to exactly one different node.

Example 1:
Input:      
           3                               
         /    \                          
       4       5                     
      /  \      
    -10   4                          
Output: 16
Explanation: Maximum Sum lies between special node 4 and 5. 4 + 4 + 3 + 5 = 16.

Example 2:
Input:    
            -15                               
         /      \                          
        5         6                      
      /  \       / \
    -8    1     3   9
   /  \              \
  2   -3              0
                     / \
                    4  -1
                       /
                     10  
Output:  27
Explanation: The maximum possible sum from one special node to another is (3 + 6 + 9 + 0 + -1 + 10 = 27)
"""

# Node Class:
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:        
    def maxPathSum(self, root):
        # Initialize the maximum path sum variable
        self.max_sum = float('-inf')

        # Helper function to perform DFS
        def dfs(node):
            if not node:
                return 0
            
            # Recursively calculate the maximum path sum from left and right children
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            # Check if the current node is a special node
            if node.left and not node.right:
                # If the node has only a left child
                current_sum = node.data + left_sum
            elif node.right and not node.left:
                # If the node has only a right child
                current_sum = node.data + right_sum
            else:
                # If the node is not a special node, return 0
                current_sum = 0
            
            # Update the global maximum path sum
            self.max_sum = max(self.max_sum, current_sum)

            # Return the maximum sum for the current node to pass to its parent
            return max(current_sum, node.data)

        # Start the DFS from the root
        dfs(root)
        return self.max_sum

# Example usage:
# Constructing the tree from the first example
root1 = Node(3)
root1.left = Node(4)
root1.right = Node(5)
root1.left.left = Node(-10)
root1.left.right = Node(4)

# Constructing the tree from the second example
root2 = Node(-15)
root2.left = Node(5)
root2.right = Node(6)
root2.left.left = Node(-8)
root2.left.right = Node(1)
root2.right.left = Node(3)
root2.right.right = Node(9)
root2.left.left.left = Node(2)
root2.left.left.right = Node(-3)
root2.right.right.right = Node(0)
root2.right.right.right.left = Node(4)
root2.right.right.right.right = Node(-1)
root2.right.right.right.right.left = Node(10)

solution = Solution()
print(solution.maxPathSum(root1))  # Output: 16
print(solution.maxPathSum(root2))  # Output: 27

'''

'''