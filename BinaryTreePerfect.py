"""
Given a Binary Tree, write a function to check whether the given Binary Tree is a prefect Binary Tree or not. 
A Binary tree is Perfect Binary Tree in which all internal nodes have two children and all leaves are at same level.

Example 1:
Input: 
        7
      /  \
     4    9
Output: YES
Explanation: As the root node 7 has two children and two leaf nodes 4 and 9 are at same level so it is a perfect binary tree.

Example 2:
Input: 
                7
              /   \
             3     8
           /   \     \
          2     5     10
        /
       1
Output: NO
"""

# Node class for creating nodes of the binary tree
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Solution class to check if the binary tree is perfect
class Solution:
    def isPerfect(self, root):
        # Find the depth of the leftmost leaf (this gives the expected leaf level)
        depth = self.findDepth(root)
        
        # Check if the tree is perfect
        return self.isPerfectUtil(root, 0, depth)
    
    # Helper function to calculate the depth of the leftmost node (leaf)
    def findDepth(self, node):
        depth = 0
        while node is not None:
            depth += 1
            node = node.left
        return depth
    
    # Helper function to check if the tree is perfect
    def isPerfectUtil(self, node, level, depth):
        # If the node is None (empty tree)
        if node is None:
            return True
        
        # If it's a leaf node, check if it's at the correct depth
        if node.left is None and node.right is None:
            return depth == level + 1
        
        # If the node has only one child, it's not a perfect binary tree
        if node.left is None or node.right is None:
            return False
        
        # Recursively check left and right subtrees
        return (self.isPerfectUtil(node.left, level + 1, depth) and
                self.isPerfectUtil(node.right, level + 1, depth))

# Helper function to create example trees for testing
def createExampleTree1():
    """
    Example 1:
              7
           /    \
          4      9
    """
    root = Node(7)
    root.left = Node(4)
    root.right = Node(9)
    return root

def createExampleTree2():
    """
    Example 2:
                  7
              /     \
             3       8
           /   \       \
          2     5       10
        /
       1
    """
    root = Node(7)
    root.left = Node(3)
    root.right = Node(8)
    root.left.left = Node(2)
    root.left.right = Node(5)
    root.left.left.left = Node(1)
    root.right.right = Node(10)
    return root

# Driver code to test the examples
def main():
    solution = Solution()
    
    # Test Example 1
    root1 = createExampleTree1()
    print("Example 1 Output:", "YES" if solution.isPerfect(root1) else "NO")  # Output: YES
    
    # Test Example 2
    root2 = createExampleTree2()
    print("Example 2 Output:", "NO" if not solution.isPerfect(root2) else "YES")  # Output: NO

if __name__ == "__main__":
    main()

'''

Here's an explanation of the code:

Node Class:
class Node:
This defines the structure of a node in the binary tree.

def __init__(self, val):
Constructor for the Node class, which initializes:

self.data = val: The node's data value.
self.left = None: The left child node.
self.right = None: The right child node.
Solution Class:
class Solution:
This class contains methods to check if a binary tree is perfect.

def isPerfect(self, root):
The main function that checks if the binary tree is perfect.

depth = self.findDepth(root)
Calls the helper function findDepth to find the depth of the leftmost node, which helps establish the expected depth of a perfect binary tree.

return self.isPerfectUtil(root, 0, depth)
Calls another helper function isPerfectUtil to check recursively whether the tree satisfies the conditions of a perfect binary tree. 
It passes the root, the current level (0), and the computed depth.

Helper Functions:
def findDepth(self, node):
This function calculates the depth of the leftmost node in the binary tree:

It initializes depth = 0 and traverses down the left side of the tree.
Each time it moves to the left child, it increments the depth.
It stops when it reaches a None node and returns the depth value.
def isPerfectUtil(self, node, level, depth):
This function checks if the binary tree is perfect:

if node is None:
Returns True if the node is None (an empty tree is considered perfect).

if node.left is None and node.right is None:
If the node is a leaf (has no children), it checks whether this leaf is at the correct depth.

if node.left is None or node.right is None:
If a node has only one child, it's not a perfect binary tree, so it returns False.

return self.isPerfectUtil(node.left, level + 1, depth) and self.isPerfectUtil(node.right, level + 1, depth):
Recursively checks both the left and right subtrees to verify that the tree satisfies the conditions for being perfect.

Example Trees:

createExampleTree1:
Builds a simple tree:
    7
   / \
  4   9
This is a perfect binary tree because all internal nodes have two children, and all leaf nodes are at the same level.

createExampleTree2:
Builds a more complex tree:
          7
       /     \
      3       8
    /   \       \
   2     5       10
  /
 1
This is not a perfect binary tree because:

The node with value 8 has only a right child.
Not all leaf nodes are at the same depth.

Output:

Test Example 1:
Example 1 Output: YES
The tree is perfect.

Test Example 2:
Example 2 Output: NO
The tree is not perfect.
'''