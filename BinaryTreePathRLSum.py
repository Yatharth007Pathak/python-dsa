"""
Given a binary tree, where every node value is a number. Find the sum of all the numbers that are formed from root to leaf paths. 
The formation of the numbers would be like 10*parent + current (see the examples for more clarification).

Examples:

Input :      
           6                               
         /   \                          
        3     5                      
      /   \     \
     2    5      4             
        /  \                        
       7    4  

Output: 13997
Explanation : There are 4 leaves, resulting in leaf path of 632, 6357, 6354, 654 sums to 13997.

Input :    
           10                               
         /   \                          
        20     30                      
      /   \     
     40       60    

Output :  2630
Explanation: There are 3 leaves, resulting in leaf path of 1240, 1260, 130 sums to 2630.
"""

# Node class definition
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def treePathSum(self, root):
        # Helper function for DFS
        def dfs(node, current_sum):
            if node is None:
                return 0
            
            # Update the current sum for this path
            current_sum = current_sum * 10 + node.data
            
            # If we reach a leaf node, return the current sum
            if node.left is None and node.right is None:
                return current_sum
            
            # Recur for left and right subtrees and return the total sum
            return dfs(node.left, current_sum) + dfs(node.right, current_sum)
        
        # Start the DFS from the root
        return dfs(root, 0)

# Example usage:
solution = Solution()

# Example 1:
root1 = Node(6)
root1.left = Node(3)
root1.right = Node(5)
root1.left.left = Node(2)
root1.left.right = Node(5)
root1.left.right.left = Node(7)
root1.left.right.right = Node(4)

print(solution.treePathSum(root1))  # Output: 13997

# Example 2:
root2 = Node(10)
root2.left = Node(20)
root2.right = Node(30)
root2.left.left = Node(40)
root2.left.right = Node(60)

print(solution.treePathSum(root2))  # Output: 2630

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
Defines a class Solution, which contains a method to calculate the sum of all root-to-leaf paths in a binary tree.

def treePathSum(self, root):
Defines a method treePathSum that takes one parameter: root, the root of the binary tree.

def dfs(node, current_sum):
Defines a helper function dfs for performing a depth-first search (DFS) on the binary tree. 
It takes two parameters: node (the current node) and current_sum (the sum formed by the path from the root to the current node).

if node is None:
Checks if the current node is None.

return 0
Returns 0 if the node is None, which helps in stopping the recursion for non-existing nodes.

current_sum = current_sum * 10 + node.data
Updates the current_sum to account for the current node's value. 
This effectively shifts the previous sum left (multiplies by 10) and adds the current node's data.

if node.left is None and node.right is None:
Checks if the current node is a leaf (i.e., it has no left or right children).

return current_sum
If the current node is a leaf, returns the current_sum, representing the complete number formed by the path from the root to this leaf.

return dfs(node.left, current_sum) + dfs(node.right, current_sum)
Recursively calls the dfs function for both the left and right subtrees and returns the sum of their results. 
This aggregates the sums from all paths that lead to leaf nodes.

return dfs(root, 0)
Initiates the DFS from the root with an initial current_sum of 0 and returns the total sum of all root-to-leaf path values.

Example usage:
solution = Solution()
Creates an instance of the Solution class.
Example 1:
root1 = Node(6)
Creates a binary tree with 6 as the root node.

root1.left = Node(3)
Adds 3 as the left child of the root.

root1.right = Node(5)
Adds 5 as the right child of the root.

root1.left.left = Node(2)
Adds 2 as the left child of node 3.

root1.left.right = Node(5)
Adds another 5 as the right child of node 3.

root1.left.right.left = Node(7)
Adds 7 as the left child of the right 5.

root1.left.right.right = Node(4)
Adds 4 as the right child of the right 5.

print(solution.treePathSum(root1))
Calls the treePathSum method with root1 and prints the result. 
The output is 13997, which is the sum of the values formed by the paths 632, 6357, and 6354.

Example 2:
root2 = Node(10)
Creates another binary tree with 10 as the root node.

root2.left = Node(20)
Adds 20 as the left child of the root.

root2.right = Node(30)
Adds 30 as the right child of the root.

root2.left.left = Node(40)
Adds 40 as the left child of node 20.

root2.left.right = Node(60)
Adds 60 as the right child of node 20.

print(solution.treePathSum(root2))
Calls the treePathSum method with root2 and prints the result. 
The output is 2630, which is the sum of the values formed by the paths 1020, 1060, and 1030.
'''