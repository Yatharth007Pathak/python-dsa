"""
Given a Binary Tree. Check whether the Binary tree is a full binary tree or not.

What is a Binary Tree?

A binary tree is a tree data structure with a maximum of 2 children per node. 
We commonly refer to them as the left and right child as each element in a binary tree may only have two children.

What is a Full Binary Tree?
A full binary tree is a binary tree with either zero or two child nodes for each node.


Example 1:
Input:
          1
       /    \
      2      3
    /   \
   4     5
Output: 1
Explanation: Every node except leaf node has two children so it is a full tree.

Example 2:
Input:
          1
       /    \
      2      3
    /   
   4     
Output: 0
Explanation: Node 2 has only one child so this is not a full tree.
"""

# Node Class:
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Return True if the given Binary Tree is a Full Binary Tree. Else return False
def isFullTree(root):
    # If tree is empty
    if root is None:
        return True
    
    # If leaf node (no children)
    if root.left is None and root.right is None:
        return True
    
    # If both left and right children exist, check if both subtrees are full binary trees
    if root.left is not None and root.right is not None:
        return isFullTree(root.left) and isFullTree(root.right)
    
    # If one of the children is missing, it's not a full binary tree
    return False

# Helper function to create example trees for testing
def createExampleTree1():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    return root

def createExampleTree2():
 
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    return root

# Test the first example
root1 = createExampleTree1()
result1 = isFullTree(root1)
print("Example 1 Output:", 1 if result1 else 0)  # Output: 1

# Test the second example
root2 = createExampleTree2()
result2 = isFullTree(root2)
print("Example 2 Output:", 1 if result2 else 0)  # Output: 0

'''
Here's a line-by-line breakdown of the code:

Node Class:
class Node:
Defines a class Node, which represents a node in a binary tree.

def __init__(self, val):
Constructor for the Node class. It initializes each node with:

self.data = val
Stores the value of the node (val) in the data attribute.

self.left = None
Initializes the left child of the node as None.

self.right = None
Initializes the right child of the node as None.

isFullTree function:
def isFullTree(root):
This function checks if the given binary tree is a full binary tree. 
A full binary tree is defined as one in which every node has either 0 or 2 children (no node has just one child).

if root is None:
Checks if the tree is empty. If the root is None, it means the tree is empty.

return True
If the tree is empty, it is considered a full binary tree, so the function returns True.

if root.left is None and root.right is None:
Checks if the node is a leaf node, meaning it has no children.

return True
If the node is a leaf (both left and right children are None), it is considered a full binary tree at this level, so return True.

if root.left is not None and root.right is not None:
Checks if both the left and right children exist. This means the node has two children, which is a requirement for a full binary tree.

return isFullTree(root.left) and isFullTree(root.right)
If both children exist, recursively check whether both the left and right subtrees are full binary trees.

return False
If the node has only one child (either left or right is None), return False, as this violates the condition of a full binary tree.

Helper Functions to Create Example Trees:
def createExampleTree1():
Creates a tree based on the first example provided in the function's docstring.

Creates the tree structure:
          1
       /    \
      2      3
    /   \
   4     5
The root node has two children, and the left child has two children as well, making it a full binary tree.

return root
Returns the root of the first example tree.

def createExampleTree2():
Creates a tree based on the second example provided in the function's docstring.

Creates the tree structure:
          1
       /    \
      2      3
    /   
   4     
This tree is not a full binary tree because node 2 has only one child (left child 4).

return root
Returns the root of the second example tree.

Testing the Function:
root1 = createExampleTree1()
Creates the first example tree.

result1 = isFullTree(root1)
Calls the isFullTree function to check if the first example tree is a full binary tree.

print("Example 1 Output:", 1 if result1 else 0)
Prints 1 if the tree is a full binary tree (returns True), or 0 if it's not (returns False). 
The output is 1 because the first example tree is a full binary tree.

root2 = createExampleTree2()
Creates the second example tree.

result2 = isFullTree(root2)
Calls the isFullTree function to check if the second example tree is a full binary tree.

print("Example 2 Output:", 1 if result2 else 0)
Prints 1 if the tree is a full binary tree, or 0 if it is not. The output is 0 because the second example tree is not a full binary tree.
'''