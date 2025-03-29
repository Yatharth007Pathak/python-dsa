"""
Given a binary tree with n nodes and two node values, a and b, your task is to find the minimum distance between them. 
The given two nodes are guaranteed to be in the binary tree and all node values are unique.

Examples :

Input: Tree = [1, 2, 3]
        1
      /  \
     2    3
a = 2, b = 3
Output: 2
Explanation: We need the distance between 2 and 3. Being at node 2, we need to take two steps ahead in order to reach node 3. 
The path followed will be: 2 -> 1 -> 3. Hence, the result is 2. 

Input: Tree = [11, 22, 33, 44, 55, 66, 77]
        11
      /    \
     22     33
    /  \    /  \
  44   55  66  77
a = 77, b = 22
Output: 3
Explanation: We need the distance between 77 and 22. Being at node 77, we need to take three steps ahead in order to reach node 22. 
The path followed will be: 77 -> 33 -> 11 -> 22. Hence, the result is 3.

Input: Tree = [1, 2, 3]
        1
      /  \
     2    3
a = 1, b = 3
Output: 1
"""

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    # Helper function to find the Lowest Common Ancestor (LCA)
    def findLCA(self, root, a, b):
        if root is None:
            return None
        if root.data == a or root.data == b:
            return root
        
        left_lca = self.findLCA(root.left, a, b)
        right_lca = self.findLCA(root.right, a, b)
        
        if left_lca and right_lca:
            return root
        return left_lca if left_lca else right_lca

    # Helper function to find the distance from root to a given node
    def findDistance(self, root, target, dist):
        if root is None:
            return -1
        if root.data == target:
            return dist
        
        left_dist = self.findDistance(root.left, target, dist + 1)
        if left_dist != -1:
            return left_dist
        
        return self.findDistance(root.right, target, dist + 1)

    # Main function to find the distance between two nodes
    def findDist(self, root, a, b):
        # Find the Lowest Common Ancestor (LCA) of nodes a and b
        lca = self.findLCA(root, a, b)
        
        # Calculate the distance from LCA to a and b
        dist_a = self.findDistance(lca, a, 0)
        dist_b = self.findDistance(lca, b, 0)
        
        return dist_a + dist_b

# Construct the binary tree
root = Node(11)
root.left = Node(22)
root.right = Node(33)
root.left.left = Node(44)
root.left.right = Node(55)
root.right.left = Node(66)
root.right.right = Node(77)

solution = Solution()
print(solution.findDist(root, 77, 22))  # Output: 3
print(solution.findDist(root, 22, 33))  # Output: 2
print(solution.findDist(root, 11, 77))  # Output: 2

'''
Line-by-Line Explanation

class Node:
Defines a Node class representing each node in a binary tree.

def __init__(self, val):
Constructor method initializes a node with:
val as the data value.
left and right pointers initialized to None.

class Solution:
Defines the Solution class, which contains helper and main methods for solving the distance problem.

def findLCA(self, root, a, b):
A recursive function to find the Lowest Common Ancestor (LCA) of two nodes a and b.

if root is None:
If the current node is None, return None.

if root.data == a or root.data == b:
If the current node matches either a or b, the LCA is the current node.

left_lca = self.findLCA(root.left, a, b)
Recursively checks the left subtree for a or b.

right_lca = self.findLCA(root.right, a, b)
Recursively checks the right subtree for a or b.

if left_lca and right_lca:
If both subtrees return non-None values, it means one node is in each subtree, so the current node is the LCA.

return left_lca if left_lca else right_lca
If only one subtree returns a non-None value, that subtree contains the LCA.

def findDistance(self, root, target, dist):
A recursive function to find the distance from a given root node to the target node.

if root is None:
If the current node is None, return -1 (indicating the target is not in this path).

if root.data == target:
If the current node is the target, return the current distance dist.

left_dist = self.findDistance(root.left, target, dist + 1)
Recursively computes the distance in the left subtree.

if left_dist != -1:
If the target is found in the left subtree, return the computed distance.

return self.findDistance(root.right, target, dist + 1)
If the target is not in the left subtree, recursively search in the right subtree.

def findDist(self, root, a, b):
Main function to calculate the distance between two nodes a and b.

lca = self.findLCA(root, a, b)
Finds the LCA of nodes a and b.

dist_a = self.findDistance(lca, a, 0)
Computes the distance from the LCA to node a.

dist_b = self.findDistance(lca, b, 0)
Computes the distance from the LCA to node b.

return dist_a + dist_b
Returns the sum of the distances from the LCA to a and b.

root = Node(11)
Creates the root node of the binary tree with value 11.

root.left = Node(22)
Sets the left child of the root to a node with value 22.

root.right = Node(33)
Sets the right child of the root to a node with value 33.

root.left.left = Node(44), etc.
Constructs additional nodes to form the tree.

solution = Solution()
Creates an instance of the Solution class.

print(solution.findDist(root, 77, 22)) # Output: 3

LCA of 77 and 22 is 11.
Distance from 11 to 77: 2.
Distance from 11 to 22: 1.
Total distance: 2 + 1 = 3.
print(solution.findDist(root, 22, 33)) # Output: 2

LCA of 22 and 33 is 11.
Distance from 11 to 22: 1.
Distance from 11 to 33: 1.
Total distance: 1 + 1 = 2.
print(solution.findDist(root, 11, 77)) # Output: 2

LCA of 11 and 77 is 11 (root itself).
Distance from 11 to 77: 2.
Total distance: 2.
'''