"""
Given the root of a binary tree. Check whether it is a BST or not.
Note: We are considering that BSTs can not contain duplicate Nodes.
A BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Examples:

Input:
   2
 /   \
1     3
       \
        5
Output: true 
Explanation: The left subtree of every node contains smaller keys and right subtree of every node contains greater. Hence, the tree is a BST.

Input:
  2
   \
    7
     \
      6
       \
        9
Output: false 
Explanation: Since the node with value 7 has right subtree nodes with keys less than 7, this is not a BST. 

Input:
   10
 /    \
5      20
      /   \
     9     25
Output: false
Explanation: The node is present in the right subtree of 10, but it is smaller than 10.
"""

class Solution:
    # Helper function to validate the BST
    def isBSTUtil(self, root, min_val, max_val):
        # Base case: An empty tree is a BST
        if root is None:
            return True
        
        # The current node must be within the range [min_val, max_val]
        if root.data <= min_val or root.data >= max_val:
            return False
        
        # Recursively check the left and right subtrees
        # Left subtree must be in the range [min_val, root.data]
        # Right subtree must be in the range [root.data, max_val]
        return (self.isBSTUtil(root.left, min_val, root.data) and
                self.isBSTUtil(root.right, root.data, max_val))
    
    # Main function to check if the binary tree is a BST
    def isBST(self, root):
        # Start with the entire range of valid values
        return self.isBSTUtil(root, float('-inf'), float('inf'))

# Example usage:
# Constructing the binary tree for test cases
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Test case 1:
root1 = Node(2)
root1.left = Node(1)
root1.right = Node(3)
root1.right.right = Node(5)

solution = Solution()
print(solution.isBST(root1))  # Output: True

# Test case 2:
root2 = Node(2)
root2.right = Node(7)
root2.right.right = Node(6)
root2.right.right.right = Node(9)

print(solution.isBST(root2))  # Output: False

# Test case 3:
root3 = Node(10)
root3.left = Node(5)
root3.right = Node(20)
root3.right.left = Node(9)
root3.right.right = Node(25)

print(solution.isBST(root3))  # Output: False


'''
Here is a line-by-line breakdown of the code:

Solution Class:
class Solution:
Defines a class Solution which contains methods to check if a binary tree is a Binary Search Tree (BST).

def isBSTUtil(self, root, min_val, max_val):
This is a helper function used to recursively validate if the binary tree rooted at root is a BST. 
It takes 3 arguments: the root node (root), the minimum allowed value (min_val), and the maximum allowed value (max_val) for the node's data.

if root is None:
Base case: If the current root node is None, it means you've reached the end of a branch, so it's a valid BST up to this point.

return True
Since an empty tree or an empty branch is always a valid BST, the function returns True.

if root.data <= min_val or root.data >= max_val:
This checks whether the current node's data violates the properties of a BST. 
A valid node must have a value that is strictly greater than min_val and less than max_val.

return False
If the node's value violates the BST property (not within the valid range), return False, meaning the tree is not a valid BST.

return (self.isBSTUtil(root.left, min_val, root.data) and Recursively check the left subtree of the current node. 
The left subtree must have values between min_val and the current node's data (root.data). 
The function recursively ensures that all nodes in the left subtree satisfy this condition.

self.isBSTUtil(root.right, root.data, max_val))
Similarly, the right subtree is checked recursively. 
All nodes in the right subtree must have values between the current node's data (root.data) and max_val.

Main Function:
def isBST(self, root):
This is the main function that checks if a binary tree is a BST. 
It starts the process by calling the helper function isBSTUtil with the root node and the widest possible range of values (-inf to +inf).

return self.isBSTUtil(root, float('-inf'), float('inf'))
The root of the tree is initially checked with the range of valid values from negative infinity (-inf) to positive infinity (+inf). 
This ensures that all nodes in the tree follow the BST rules.

Node Class:
class Node:
This defines a class Node that is used to create nodes for binary tree. Each node has a data value and pointers to left and right children.

def __init__(self, data):
The constructor of the Node class initializes a node with its data and 
sets the left and right pointers to None (indicating no children initially).

Test Case 1:
root1 = Node(2)
Creates the root node of the first test tree with the value 2.

root1.left = Node(1)
Adds a left child to the root with the value 1.

root1.right = Node(3)
Adds a right child to the root with the value 3.

root1.right.right = Node(5)
Adds a right child to the node with value 3, which has the value 5.

solution = Solution()
Creates an instance of the Solution class to access its methods.

print(solution.isBST(root1))
Calls the isBST function with root1 to check if the tree is a valid BST. The expected output is True since the tree follows the BST rules.

Test Case 2:
root2 = Node(2)
Creates the root node for the second test case with the value 2.

root2.right = Node(7)
Adds a right child to the root with the value 7.

root2.right.right = Node(6)
Adds a right child to the node with value 7, which has the value 6. 
This violates the BST property since 6 is less than 7 but is in the right subtree.

root2.right.right.right = Node(9)
Adds a right child to the node with value 6, with the value 9.

print(solution.isBST(root2))
Calls the isBST function with root2. The expected output is False because the node with value 6 violates the BST rules.

Test Case 3:
root3 = Node(10)
Creates the root node for the third test case with the value 10.

root3.left = Node(5)
Adds a left child to the root with the value 5.

root3.right = Node(20)
Adds a right child to the root with the value 20.

root3.right.left = Node(9)
Adds a left child to the node with value 20, which has the value 9. 
This violates the BST property because 9 is less than 10 but is in the right subtree.

root3.right.right = Node(25)
Adds a right child to the node with value 20, with the value 25.

print(solution.isBST(root3))
Calls the isBST function with root3. The expected output is False because the node with value 9 violates the BST rules.
'''