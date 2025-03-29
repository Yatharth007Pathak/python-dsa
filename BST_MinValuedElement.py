"""
Given the root of a Binary Search Tree. The task is to find the minimum valued element in this given BST.

In a Binary Search Tree (BST), the leftmost and rightmost nodes are defined by the following properties:

Leftmost Node:
The leftmost node is the node that has no left child and is reached by continuously traversing left from the root.
This node contains the minimum value in the BST.

Rightmost Node:
The rightmost node is the node that has no right child and is reached by continuously traversing right from the root.
This node contains the maximum value in the BST.


Example 1:
Input:
           5
         /   \
        4     6
       /       \
      3         7
     /
    1
Output: 1

Example 2:
Input:
             9
              \
               10
                \
                 11
Output: 9
"""

"""
A Binary Search Tree (BST) is a type of binary tree in which each node follows a specific ordering property, 
making it efficient for searching, inserting, and deleting data. In a BST:
The left subtree of a node contains only nodes with values less than the node's value.
The right subtree of a node contains only nodes with values greater than the node's value.
Both the left and right subtrees are also binary search trees.

Structure of a Binary Search Tree Node:
Each node in the BST typically contains:
Data: The value stored in the node.
Left Child: A pointer/reference to the left child (subtree with smaller values).
Right Child: A pointer/reference to the right child (subtree with larger values).

Example of a Binary Search Tree:
        50
       /  \
     30    70
    /  \   /  \
   20  40 60  80

Key Operations:
Search: To find a value in the tree, start at the root and repeatedly check if the value is smaller or 
greater than the current node's value, then move left or right accordingly.
Insertion: Insert a value by comparing it to the nodes, moving left if it's smaller and right if it's larger, 
until an appropriate empty spot is found.
Deletion: Removing a node involves several cases:
Node has no children (leaf node): Simply delete it.
Node has one child: Replace the node with its child.
Node has two children: Find the node's in-order successor (the smallest node in its right subtree), 
copy its value to the node, and then delete the successor.

Traversals:
Traversal methods are used to visit all nodes in the BST.
In-order Traversal: Left, Root, Right (Yields sorted values in a BST)
Pre-order Traversal: Root, Left, Right
Post-order Traversal: Left, Right, Root

Advantages of BST:
Efficient Search: In an ideal (balanced) BST, searching, inserting, and deleting nodes takes O(log n) time.
Dynamic: Like linked lists, BSTs can grow and shrink as needed.

Disadvantages:
Unbalanced Trees: If not balanced, the performance degrades to O(n) (like a linked list) in the worst case.
"""

class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

class Solution:
    # Function to find the minimum element in the given BST.
    def minValue(self, root):
        # Start from the root and keep going to the left child until you reach the leftmost node
        if root is None:
            return None  # In case the tree is empty
        
        current = root
        while current.left is not None:
            current = current.left
        
        return current.data  # Return the value of the leftmost node

# Example usage
# Creating a BST for the first example
root1 = Node(5)
root1.left = Node(4)
root1.right = Node(6)
root1.left.left = Node(3)
root1.right.right = Node(7)
root1.left.left.left = Node(1)

# Creating a BST for the second example
root2 = Node(9)
root2.right = Node(10)
root2.right.right = Node(11)

sol = Solution()

# Finding the minimum value in the first BST
min_value1 = sol.minValue(root1)
print(min_value1)  # Output: 1

# Finding the minimum value in the second BST
min_value2 = sol.minValue(root2)
print(min_value2)  # Output: 9


'''
Here's a line-by-line breakdown of the code you provided:

class Node:
Defines a class named Node, which will be used to create nodes of a binary search tree (BST).

def __init__(self, val):
Initializes a new instance of the Node class. It takes a parameter val representing the value of the node.

self.right = None
Initializes the right child of the node to None, indicating that it does not yet point to any node.

self.data = val
Sets the data attribute of the node to the provided value val.

self.left = None
Initializes the left child of the node to None, indicating that it does not yet point to any node.

class Solution:
Defines a class named Solution, which contains methods related to operations on the binary search tree.

def minValue(self, root):
Defines a method named minValue that takes a parameter root, representing the root node of the BST.

if root is None:
Checks if the root is None, which means the tree is empty.

return None
If the tree is empty, it returns None.

current = root
Initializes a variable current to the root of the tree. This variable will be used to traverse the tree.

while current.left is not None:
Starts a loop that continues as long as the current node has a left child.

current = current.left
Moves the current pointer to the left child of the current node. This continues until it reaches the leftmost node in the tree.

return current.data
Once the leftmost node is reached (where current.left is None), the method returns the data of that node, which is the minimum value in the BST.

# Example usage
A comment indicating that the following code is an example of how to use the Node and Solution classes.

root1 = Node(5)
Creates a Node instance with a value of 5, which becomes the root of the first BST.

root1.left = Node(4)
Sets the left child of root1 to a new Node with a value of 4.

root1.right = Node(6)
Sets the right child of root1 to a new Node with a value of 6.

root1.left.left = Node(3)
Sets the left child of the node with value 4 to a new Node with a value of 3.

root1.right.right = Node(7)
Sets the right child of the node with value 6 to a new Node with a value of 7.

root1.left.left.left = Node(1)
Sets the left child of the node with value 3 to a new Node with a value of 1, creating a deeper level in the tree.

root2 = Node(9)
Creates a Node instance with a value of 9, which becomes the root of the second BST.

root2.right = Node(10)
Sets the right child of root2 to a new Node with a value of 10.

root2.right.right = Node(11)
Sets the right child of the node with value 10 to a new Node with a value of 11, creating a deeper level in the tree.

sol = Solution()
Creates an instance of the Solution class, allowing access to its methods.

min_value1 = sol.minValue(root1)
Calls the minValue method on the sol instance with root1 as the argument, storing the result in min_value1.

print(min_value1)
Prints the minimum value found in the first BST. Expected output is 1.

min_value2 = sol.minValue(root2)

Calls the minValue method on the sol instance with root2 as the argument, storing the result in min_value2.

print(min_value2)
Prints the minimum value found in the second BST. Expected output is 9.
'''