"""
Given two binary trees, the task is to find if both of them are identical or not.
Note: You need to return true or false, the printing is done by the driver code.

Examples:

Input:
     1          1
   /   \      /   \
  2     3    2     3
Output: Yes
Explanation: There are two trees both having 3 nodes and 2 edges, 
both trees are identical having the root as 1, left child of 1 is 2 and right child of 1 is 3.

Input:
    1       1
  /  \     /  \
 2    3   3    2
Output: No
Explanation: There are two trees both having 3 nodes and 2 edges, but both trees are not identical.
"""

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    # Function to check if two trees are identical.
    def isIdentical(self, root1, root2):
        # If both nodes are None, the trees are identical
        if root1 is None and root2 is None:
            return True
        
        # If one node is None and the other is not, the trees are not identical
        if root1 is None or root2 is None:
            return False
        
        # If the values of the current nodes are different, the trees are not identical
        if root1.data != root2.data:
            return False
        
        # Recursively check if the left and right subtrees are identical
        return self.isIdentical(root1.left, root2.left) and self.isIdentical(root1.right, root2.right)

# Example usage:
if __name__ == "__main__":
    # Construct two identical trees
    root1 = Node(1)
    root1.left = Node(2)
    root1.right = Node(3)

    root2 = Node(1)
    root2.left = Node(2)
    root2.right = Node(3)

    solution = Solution()
    print(solution.isIdentical(root1, root2))  # Output: True

    # Construct two non-identical trees
    root3 = Node(1)
    root3.left = Node(3)
    root3.right = Node(2)

    print(solution.isIdentical(root1, root3))  # Output: False

'''
Here's a detailed breakdown of the code, which checks if two binary trees are identical:

class Node:
This defines a class Node that represents a node in a binary tree.

def __init__(self, val):
This is the constructor method for the Node class. It initializes a node with:
data set to val (the value passed when creating the node),
left and right pointers both set to None (since the node initially has no children).

class Solution:
This defines a class Solution that contains the method to check if two binary trees are identical.

def isIdentical(self, root1, root2):
This method takes two root nodes (root1 and root2) and checks if the trees rooted at these nodes are identical.

Base Case 1:
if root1 is None and root2 is None:
If both root1 and root2 are None, this means that both trees (or subtrees) are empty at the current nodes, so they are identical.
return True ensures the recursion ends for this case.

Base Case 2:
if root1 is None or root2 is None:
If only one of the nodes is None while the other is not, it means the structures of the two trees are different, so they cannot be identical.
return False terminates the recursion for this case.

Base Case 3:
if root1.data != root2.data:
If the current nodes of both trees have different values, it indicates the trees are not identical.
return False ensures the trees are identified as different.

return self.isIdentical(root1.left, root2.left) and self.isIdentical(root1.right, root2.right):
This checks both the left and right subtrees of the current nodes. Both subtrees must be identical for the trees to be considered identical. 
It uses recursion to go down the tree structure.

root1 = Node(1)
This creates the root node of the first tree with a value of 1. 
Similarly, nodes 2 and 3 are created as its left and right children, respectively.

root2 = Node(1)
This creates the root node of the second tree. The second tree is constructed in the same way as the first tree.

solution.isIdentical(root1, root2)
This calls the isIdentical method to check if the two trees are identical. In this case, they are identical, so the output is True.

Non-identical Trees: Another tree root3 is created, but its left and right children have swapped values compared to root1. 
Therefore, the trees are not identical, and the output is False.

Output:
First Check (root1 vs root2): True because the trees are identical.

Second Check (root1 vs root3): False because the trees are not identical.
'''