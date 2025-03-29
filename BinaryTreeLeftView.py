"""
Given a Binary Tree, return its Left view. The left view of a Binary Tree is a set of nodes visible when the tree is visited from the Left side.
If no left view is possible, return an empty array.

Examples :

Input: root[] = [1, 2, 3, 4, 5, 6, 7, N, 8]
          1
       /     \
     2        3
   /     \    /  \
  4     5   6     7
   \
     8   
Output: [1, 2, 4, 8]
Explanation: When we view the tree from the left side, we can only see the nodes 1, 2, 4, and 8.

Input: root[] = [1, 3, N, N, 4]
Output: [1, 3, 4]

Input: root[] = [N]
Output: []
"""

from collections import deque

# Node Class
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Function to return a list containing elements of left view of the binary tree.
def LeftView(root):
    if not root:
        return []
    
    left_view = []
    queue = deque([root])
    
    while queue:
        level_length = len(queue)
        
        for i in range(level_length):
            node = queue.popleft()
            
            # If it's the first node of this level, add it to the left view
            if i == 0:
                left_view.append(node.data)
                
            # Enqueue left child first, then right child
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    return left_view

# Example usage:
# Constructing the binary tree for the first test case
root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)
root1.right.left = Node(6)
root1.right.right = Node(7)
root1.left.left.right = Node(8)

print(LeftView(root1))  # Output: [1, 2, 4, 8]

# Constructing the binary tree for the second test case
root2 = Node(1)
root2.left = Node(3)
root2.left.right = Node(4)

print(LeftView(root2))  # Output: [1, 3, 4]

# Test case for an empty tree
root3 = None
print(LeftView(root3))  # Output: []


'''
Here's a detailed breakdown of the code that retrieves the left view of a binary tree:

Node Class
class Node:
Defines a class named Node which represents each node in the binary tree.

def __init__(self, val):
This is the constructor method for the Node class. It initializes a node with a value (val) and sets both the left and right children to None.

self.data = val
Assigns the passed value to the data attribute of the node.

self.left = None
Initializes the left child of the node to None.

self.right = None
Initializes the right child of the node to None.

Left View Function
def LeftView(root):
Defines a function named LeftView that takes the root of the binary tree as an argument 
and returns a list of elements that form the left view of the tree.

if not root:
Checks if the root is None. If the tree is empty, it returns an empty list.

left_view = []
Initializes an empty list to store the elements of the left view.

queue = deque([root])
Initializes a queue using deque from the collections module. 
The queue starts with the root node, which will be used for level-order traversal (BFS).

Level-Order Traversal
while queue:
Starts a loop that continues as long as there are nodes in the queue.

level_length = len(queue)
Stores the number of nodes at the current level in level_length. This helps in processing each level of the tree.

for i in range(level_length):
Begins a loop to iterate through all nodes at the current level.

node = queue.popleft()
Removes and retrieves the leftmost node from the queue for processing.

if i == 0:
Checks if the current node is the first node at this level. If so, it means this node contributes to the left view.

left_view.append(node.data)
Adds the data of the first node at the current level to the left_view list.

if node.left:
Checks if the current node has a left child. If it does, it will be added to the queue for processing in the next level.

queue.append(node.left)
Enqueues the left child of the current node.

if node.right:
Checks if the current node has a right child. If it does, it will also be added to the queue.

queue.append(node.right)
Enqueues the right child of the current node.

Return Result
return left_view
After all levels have been processed, the function returns the left_view list,
 which contains the elements visible from the left side of the tree.

Example Usage
Test Case 1:
root1 = Node(1): Creates the root node with the value 1.
Adding children: Constructs the rest of the binary tree structure.
print(LeftView(root1)): Calls the LeftView function and prints the result, which outputs [1, 2, 4, 8].

Test Case 2:
root2 = Node(1): Creates a new root node.
Adding children: Constructs a different tree structure.
print(LeftView(root2)): Calls the LeftView function, which outputs [1, 3, 4].

Test Case 3:
root3 = None: Represents an empty tree.
print(LeftView(root3)): Calls the LeftView function on the empty tree, which outputs [].
'''