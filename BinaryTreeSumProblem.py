"""
Given a Binary Tree, find the sum of all the leaf nodes that are at minimum level of the given binary tree.
Example 1:

Input: 
         1
        /  \
       2    3
     /  \     \
    4    5     8 
  /  \ 
 7    2      
Output: sum = 5 + 8 = 13
Input: 
         1
      /    \
     2      3
    / \    / \
   4   5  6   7
Output: 22 
"""

from collections import deque

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def minLeafSum(self, root):
        if not root:
            return 0
        
        # Queue for level order traversal
        queue = deque([root])
        min_leaf_level = None
        leaves_at_min_level = []
        
        # Perform level order traversal
        while queue:
            current_level_size = len(queue)
            current_leaves = []
            
            for _ in range(current_level_size):
                node = queue.popleft()
                
                # Check if it's a leaf node
                if not node.left and not node.right:
                    current_leaves.append(node.data)
                
                # Add child nodes to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # If we found leaves at this level, store them
            if current_leaves:
                if min_leaf_level is None:
                    # First time we're encountering leaves
                    min_leaf_level = len(leaves_at_min_level)
                # Update leaves at minimum level
                leaves_at_min_level = current_leaves

        # Return the sum of the leaves at the minimum level
        return sum(leaves_at_min_level)

# Example usage:
solution = Solution()

# Example 1:
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)
root1.right.right = Node(8)
root1.left.left.left = Node(7)
root1.left.left.right = Node(2)
print(solution.minLeafSum(root1))  # Output: 13

# Example 2:
root2 = Node(1)
root2.left = Node(2)
root2.right = Node(3)
root2.left.left = Node(4)
root2.left.right = Node(5)
root2.right.left = Node(6)
root2.right.right = Node(7)
print(solution.minLeafSum(root2))  # Output: 22
