"""
Given two binary trees with head reference as T and S having at most N nodes. The task is to check if S is present as subtree in T.
A subtree of a tree T1 is a tree T2 consisting of a node in T1 and all of its descendants in T1.

Example 1:
Input:
T:      1          S:   3
      /   \            /
     2     3          4
   /  \    /
  N    N  4
Output: 1 
Explanation: S is present in T

Example 2:
Input:
T:      26         S:   26
       /   \           /  \
     10     N        10    N
   /    \           /  \
   20    30        20  30
  /  \            /  \
 40   60         40  60
Output: 1 
Explanation: S and T are both same. Hence, it can be said that S is a subtree of T.
"""

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = val

class Solution:
    def isSubTree(self, T, S):
        # If S is None, it is always a subtree
        if S is None:
            return True
        # If T is None and S is not None, then S cannot be a subtree
        if T is None:
            return False

        # Check if the trees rooted at current nodes of T and S are identical
        if self.isIdentical(T, S):
            return True

        # Check if S is a subtree of either the left or right subtree of T
        return self.isSubTree(T.left, S) or self.isSubTree(T.right, S)
    
    # Helper function to check if two trees are identical
    def isIdentical(self, root1, root2):
        # If both trees are empty, they are identical
        if root1 is None and root2 is None:
            return True
        
        # If one of the trees is empty and the other is not, they are not identical
        if root1 is None or root2 is None:
            return False
        
        # Check if the current nodes and their subtrees are identical
        return (root1.data == root2.data and 
                self.isIdentical(root1.left, root2.left) and 
                self.isIdentical(root1.right, root2.right))

# Example usage:
# Tree T
rootT = Node(26)
rootT.left = Node(10)
rootT.left.left = Node(20)
rootT.left.right = Node(30)
rootT.left.left.left = Node(40)
rootT.left.left.right = Node(60)

# Tree S
rootS = Node(10)
rootS.left = Node(20)
rootS.right = Node(30)
rootS.left.left = Node(40)
rootS.left.right = Node(60)

solution = Solution()
print(solution.isSubTree(rootT, rootS))  # Output: True (1 in problem terms)

'''
Here's a line-by-line breakdown of the code:

class Node:
Defines a class named Node for creating nodes in a binary tree.

def __init__(self, val):
Initializes the Node class with a constructor method. Takes one parameter, val, which is the value for the node.

self.left = None
Sets the left child of the node to None, indicating there is no left child by default.

self.right = None
Sets the right child of the node to None, indicating there is no right child by default.

self.data = val
Sets the data attribute of the node to val, storing the node's value.

class Solution:
Defines a class named Solution containing methods to check if one tree is a subtree of another.

def isSubTree(self, T, S):
Defines a method isSubTree within the Solution class. 
It takes self (instance), T (root of the main tree), and S (root of the potential subtree) as parameters.

if S is None:
Checks if S is None (empty).

return True
If S is empty, it is always a subtree, so it returns True.

if T is None:
Checks if T is None.

return False
If T is None and S is not, S cannot be a subtree of T, so it returns False.

if self.isIdentical(T, S):
Calls the helper method isIdentical to check if the trees rooted at the current nodes of T and S are identical.

return True
If T and S are identical, returns True.

return self.isSubTree(T.left, S) or self.isSubTree(T.right, S)
If T and S are not identical, recursively checks if S is a subtree of either the left or right subtree of T.

def isIdentical(self, root1, root2):
Defines a helper method isIdentical to check if two trees rooted at root1 and root2 are identical.

if root1 is None and root2 is None:
Checks if both root1 and root2 are None.

return True
If both are empty, the trees are identical, so it returns True.

if root1 is None or root2 is None:
Checks if only one of root1 or root2 is None.

return False
If only one of the trees is empty, they are not identical, so it returns False.

return (root1.data == root2.data and ...
Checks if the data of root1 is equal to root2 and recursively calls isIdentical for the left and right children of root1 and root2.

Example Usage:

Creating Tree T:

rootT = Node(26) creates the root of tree T with data 26.
rootT.left = Node(10) adds a left child with data 10.
Additional nodes are created similarly to build T.
Creating Tree S:

rootS = Node(10) creates the root of tree S with data 10.
Additional nodes are created similarly to build S.
solution = Solution()
Creates an instance of the Solution class.

print(solution.isSubTree(rootT, rootS)) # Output: True
Calls isSubTree on rootT and rootS to check if S is a subtree of T. Outputs True because S matches a subtree in T.
'''