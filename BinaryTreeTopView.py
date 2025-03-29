"""
Given below is a binary tree. The task is to print the top view of binary tree. 
Top view of a binary tree is the set of nodes visible when the tree is viewed from the top. For the given below tree

       1
    /     \
   2       3
  /  \    /  \
 4    5  6    7

Top view will be: 4 2 1 3 7
Note: Return nodes from leftmost node to rightmost node. Also if 2 nodes are outside the shadow of the tree 
and are at same position then consider the left ones only(i.e. leftmost). 
For ex - 1 2 3 N 4 5 N 6 N 7 N 8 N 9 N N N N N will give 8 2 1 3 as answer. Here 8 and 9 are on the same position but 9 will get shadowed.

Example 1:
Input:
     1
   /   \
  2     3
Output: 2 1 3

Example 2:
Input:
       10
    /      \
  20        30
 /   \    /    \
40   60  90    100
Output: 40 20 10 30 100
"""

from collections import deque

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def topView(self, root):
        if not root:
            return []

        # Map to store the first node at each horizontal distance
        hd_map = {}
        
        # Queue for level order traversal, stores nodes and their horizontal distance
        queue = deque([(root, 0)])  # (node, horizontal_distance)
        
        while queue:
            node, hd = queue.popleft()
            
            # If this horizontal distance is not in the map, we add the node
            if hd not in hd_map:
                hd_map[hd] = node.data
            
            # Enqueue the left child with horizontal distance - 1
            if node.left:
                queue.append((node.left, hd - 1))
            
            # Enqueue the right child with horizontal distance + 1
            if node.right:
                queue.append((node.right, hd + 1))
        
        # Get the nodes in top view by sorting horizontal distances and returning the nodes in that order
        top_view = [hd_map[hd] for hd in sorted(hd_map.keys())]
        
        return top_view

# Construct the binary tree
root = Node(10)
root.left = Node(20)
root.right = Node(30)
root.left.left = Node(40)
root.left.right = Node(60)
root.right.left = Node(90)
root.right.right = Node(100)

sol = Solution()
print(sol.topView(root))  # Output: [40, 20, 10, 30, 100]

'''
Here's a line-by-line breakdown of the code:

class Node:
Defines a Node class representing each node in the binary tree.

def __init__(self, val):
Initializes a node with a given value (val) and sets its left and right children to None.

class Solution:
Defines the Solution class which contains the method to compute the top view of a binary tree.

def topView(self, root):
Defines the method topView which takes the root of a binary tree as input and returns the top view of the tree.

if not root:
Checks if the root is None. If the tree is empty, it returns an empty list [].
Initialize Data Structures

hd_map = {}
Initializes an empty dictionary hd_map to store the first node at each horizontal distance (HD).

queue = deque([(root, 0)])
Initializes a deque queue for level order traversal. The queue stores pairs of nodes and their corresponding horizontal distance (HD), 
starting with the root at HD = 0.

while queue:
Loops through the queue to perform a level-order traversal (BFS) of the tree.

node, hd = queue.popleft()
Dequeues the first element in the queue, which consists of a node and its horizontal distance (hd).

if hd not in hd_map:
Checks if the current horizontal distance (hd) is already in the hd_map. 
If not, it adds the current node's data to the map, ensuring only the first node at each horizontal distance is included in the top view.

if node.left:
If the current node has a left child, it is enqueued with a horizontal distance of hd - 1 
(since the left child is positioned to the left of the current node).

if node.right:
Similarly, if the current node has a right child, it is enqueued with a horizontal distance of hd + 1.

top_view = [hd_map[hd] for hd in sorted(hd_map.keys())]
After the level-order traversal, hd_map contains the first node at each horizontal distance. 
The horizontal distances are sorted, and the corresponding node values are added to the top_view list in order.
Return the Result

return top_view
The method returns the top_view list containing the nodes visible from the top of the binary tree.

Example Usage
Tree Structure:
     10
    /  \
   20   30
  /  \   / \
 40   60 90 100

Top View:
The top view of the tree is the sequence of nodes visible when viewed from the top. In this case, the nodes are [40, 20, 10, 30, 100].

Output:
Input: The tree defined above.
Execution: The method computes the top view by performing level-order traversal and sorting horizontal distances.
Output: [40, 20, 10, 30, 100]

Key Concepts:
Horizontal Distance (HD): The HD of a node is defined relative to the root. 
The root has an HD of 0, left child nodes have a HD of -1, and right child nodes have an HD of +1.
Top View: The top view of a binary tree is the sequence of nodes visible when viewed from the top, 
considering nodes at the same horizontal distance only once.
'''