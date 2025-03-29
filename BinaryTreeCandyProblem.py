"""
Given a binary tree with N nodes, in which each node value represents number of candies present at that node. 
In one move, one may choose two adjacent nodes and move only one candy from one node to another 
(the move may be from parent to child, or from child to parent.) 
The task is to find the minimum number of moves required such that every node has exactly one candy.
Note that the testcases are framed such that it is always possible to achieve a configuration in which every node has exactly one candy, 
after some moves.

Example 1:
Input :      3
           /   \
          0     0 
Output : 2
Explanation: From the root of the tree, we move one candy to its left child, and one candy to its right child.

Example 2:
Input :      0
           /   \
          3     0  
Output : 3
Explanation: From the left child of the root, we move two candies to the root [taking two moves]. 
Then, we move one candy from the root of the tree to the right child.
"""

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    def __init__(self):
        self.moves = 0  # To store the total number of moves

    def distributeCandy(self, root):
        # Helper function for post-order traversal
        def post_order_balance(node):
            if not node:
                return 0  # Base case: no surplus/deficit for null nodes
            
            # Recur for the left and right subtrees
            left_balance = post_order_balance(node.left)
            right_balance = post_order_balance(node.right)
            
            # Total moves needed is the sum of absolute balances at each step
            self.moves += abs(left_balance) + abs(right_balance)
            
            # Current balance for this node
            # `node.data - 1` is the surplus or deficit for this node itself
            return node.data - 1 + left_balance + right_balance

        # Call the helper function
        post_order_balance(root)
        
        return self.moves

solution = Solution()

# Example 1
root1 = Node(3)
root1.left = Node(0)
root1.right = Node(0)
print(solution.distributeCandy(root1))  # Expected Output: 2

# Example 2
root2 = Node(0)
root2.left = Node(3)
root2.right = Node(0)

solution = Solution()
print(solution.distributeCandy(root2))  # Expected Output: 3

# Example 3: Single node with excess candies
root3 = Node(5)
solution = Solution()
print(solution.distributeCandy(root3))  # Expected Output: 4

# Example 4: Larger tree
root4 = Node(1)
root4.left = Node(0)
root4.right = Node(0)
root4.left.left = Node(2)
root4.left.right = Node(3)
solution = Solution()
print(solution.distributeCandy(root4))  # Expected Output: Total moves required

'''
Here's a line-by-line breakdown of the code:

Define a Node class: Represents a node in a binary tree.
Attributes:
right: points to the right child of the node.
data: holds the number of candies in the node.
left: points to the left child of the node.

Define the Solution class: This class includes a method to calculate the minimum moves required to balance candies across the nodes.
Attributes:
moves: an integer to track the total number of moves needed, initialized to 0.

Define the distributeCandy function in Solution: This function calculates the minimum moves required to balance the tree.
Parameters:
root: the root node of the binary tree.

Define post_order_balance function within distributeCandy: This recursive helper function uses post-order traversal 
to calculate the balance of candies at each node.
Parameters:
node: the current node being processed.

Check if node is None: If node is None, return 0, indicating no surplus or deficit of candies.

Recurse through the left subtree: Calculate left_balance by calling post_order_balance on node.left.

Recurse through the right subtree: Calculate right_balance by calling post_order_balance on node.right.

Calculate total moves required at this node:
Add abs(left_balance) + abs(right_balance) to self.moves since each represents a move needed 
to transfer surplus or deficit candies to achieve balance.

Calculate and return current node balance: This value is calculated as node.data - 1 + left_balance + right_balance, 
representing the net balance of candies after balancing the subtree rooted at node.

Call post_order_balance on root: Begin the post-order traversal from the root node to distribute candies.

Return self.moves: This returns the total number of moves required after processing the entire tree.

Test Cases:

Create a tree for Test Case 1:
Tree structure:
    3
   / \
  0   0
This tree requires 2 moves to distribute candies. Print the result.

Create a tree for Test Case 2:
Tree structure:
    0
   / \
  3   0
This tree requires 3 moves. Print the result.

Create a tree for Test Case 3: A single node with excess candies (5), needing 4 moves to balance. Print the result.

Create a tree for Test Case 4: Larger tree structure:
      1
     / \
    0   0
   / \
  2   3
This tree tests handling of deeper trees with multiple moves required. Print the total moves.

This solution calculates the minimal moves needed to balance candies across nodes by using a post-order traversal, 
which ensures that balances are propagated from the leaves up to the root.
'''