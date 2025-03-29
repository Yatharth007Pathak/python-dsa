"""
Given a Binary Tree with all unique values and two nodes value, n1 and n2. 
The task is to find the lowest common ancestor of the given two nodes. 
We may assume that either both n1 and n2 are present in the tree or none of them are present.

LCA: It is the first common ancestor of both the nodes n1 and n2 from bottom of tree.

Example 1:
Input: n1 = 2 , n2 = 3  
       1 
      / \ 
     2   3
Output: 1
Explanation: LCA of 2 and 3 is 1.

Example 2:
Input: n1 = 3 , n2 = 4
           5    
          /    
         2  
        / \  
       3   4
Output: 2
Explanation: LCA of 3 and 4 is 2. 

Example 3:
Input: n1 = 5 , n2 = 4
           5    
          /    
         2  
        / \  
       3   4
Output: 5
Explanation: LCA of 5 and 4 is 5. 
"""

class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

class Solution:
    # Function to return the lowest common ancestor in a Binary Tree.
    def lca(self, root, n1, n2):
        # Base case: If root is None, there's no LCA
        if root is None:
            return None
        
        # If either n1 or n2 is found, return the current node
        if root.data == n1 or root.data == n2:
            return root
        
        # Recur for left and right subtrees
        left_lca = self.lca(root.left, n1, n2)
        right_lca = self.lca(root.right, n1, n2)
        
        # If both left and right calls return non-None values, current node is LCA
        if left_lca and right_lca:
            return root
        
        # Otherwise return non-None value from one of the subtrees
        return left_lca if left_lca is not None else right_lca

# Example usage:
root = Node(5)
root.left = Node(2)
root.left.left = Node(3)
root.left.right = Node(4)

sol = Solution()
print(sol.lca(root, 3, 4).data)  # Output: 2
print(sol.lca(root, 5, 4).data)  # Output: 5

'''
Code breakdown:

class Node:
Defines a class called Node, which represents a node in a binary tree.

def __init__(self, value):
Defines the constructor (__init__) of the Node class, which is called when a Node object is created. 
It takes one argument, value, representing the data of the node.

self.left = None
Initializes the left child of the node to None, meaning this node has no left child initially.

self.data = value
Assigns the value passed to the constructor (value) to the data attribute of the node.

self.right = None
Initializes the right child of the node to None, meaning this node has no right child initially.

class Solution:
Defines another class called Solution, which contains methods to solve a problem related to the binary tree, 
in this case, finding the Lowest Common Ancestor (LCA).

def lca(self, root, n1, n2):
Defines the lca method inside the Solution class. This method takes three arguments: 
root (the root of the binary tree), n1 (first node), and n2 (second node). It is used to find the LCA of n1 and n2.

if root is None:
Checks if the current root node is None. This is the base case for recursion. 
If root is None, it means there's no node, so the function returns None.

if root.data == n1 or root.data == n2:
Checks if the current root node contains either n1 or n2. 
If true, it means one of the nodes has been found, so it returns the current node (root).

left_lca = self.lca(root.left, n1, n2)
Recursively calls the lca method on the left subtree (root.left). The result is stored in left_lca.

right_lca = self.lca(root.right, n1, n2)
Recursively calls the lca method on the right subtree (root.right). The result is stored in right_lca.

if left_lca and right_lca:
Checks if both left_lca and right_lca are non-None, meaning both n1 and n2 are found in different subtrees. 
In this case, the current root is the LCA, so it returns root.

return left_lca if left_lca is not None else right_lca
If only one of left_lca or right_lca is non-None, it returns the non-None one. If both are None, it returns None.

Example Usage

root = Node(5)
Creates the root node of the tree with a value of 5.

root.left = Node(2)
Creates a left child of the root node with a value of 2.

root.left.left = Node(3)
Creates a left child of node 2 with a value of 3.

root.left.right = Node(4)
Creates a right child of node 2 with a value of 4.

sol = Solution()
Creates an instance of the Solution class.

print(sol.lca(root, 3, 4).data)
Calls the lca method to find the LCA of nodes 3 and 4. The result is the node with value 2, and it prints 2.

print(sol.lca(root, 5, 4).data)
Calls the lca method to find the LCA of nodes 5 and 4. The result is the node with value 5, and it prints 5.
'''