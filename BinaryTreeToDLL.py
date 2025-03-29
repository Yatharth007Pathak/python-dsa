"""
Given a Binary Tree (BT), convert it to a Doubly Linked List (DLL) in place. 
The left and right pointers in nodes will be used as previous and next pointers respectively in converted DLL. 
The order of nodes in DLL must be the same as the order of the given Binary Tree. 
The first node of Inorder traversal (leftmost node in BT) must be the head node of the DLL.

Note: h is the tree's height, and this space is used implicitly for the recursion stack.

Examples:

Input:
      1
    /  \
   3    2
Output:
3 1 2 
2 1 3
Explanation: DLL would be 3<=>1<=>2

Input:
       10
      /   \
     20   30
   /   \
  40   60
Output:
40 20 60 10 30 
30 10 60 20 40
Explanation:  DLL would be 40<=>20<=>60<=>10<=>30.
"""

class Node:
    """Class Node representing a tree node."""
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None

class Solution:
    def __init__(self):
        self.head = None  # Head of the DLL
        self.prev = None  # Previous node in DLL
        
    # Function to convert binary tree to doubly linked list
    def bToDLL(self, root):
        # Perform in-order traversal to convert the tree to DLL
        def inorder_convert(node):
            if not node:
                return
            
            # Traverse the left subtree
            inorder_convert(node.left)
            
            # If prev is None, we're at the head of the DLL
            if self.prev is None:
                self.head = node  # Set head of DLL
            else:
                # Link the previous node with the current node
                self.prev.right = node
                node.left = self.prev
            
            # Move prev to the current node
            self.prev = node
            
            # Traverse the right subtree
            inorder_convert(node.right)
        
        # Start the conversion process
        inorder_convert(root)
        
        return self.head  # Return the head of the created DLL

# Helper function to print the doubly linked list from left to right
def print_dll(head):
    current = head
    while current:
        print(current.data, end=" ")
        current = current.right
    print()

# Helper function to print the doubly linked list from right to left
def print_dll_reverse(head):
    current = head
    while current.right:
        current = current.right
    while current:
        print(current.data, end=" ")
        current = current.left
    print()

# Test cases
# Constructing the binary tree:
#       1
#     /   \
#    3     2
root1 = Node(1)
root1.left = Node(3)
root1.right = Node(2)

solution = Solution()
dll_head1 = solution.bToDLL(root1)
print("DLL from left to right:")
print_dll(dll_head1)  # Expected Output: 3 1 2
print("DLL from right to left:")
print_dll_reverse(dll_head1)  # Expected Output: 2 1 3

# Constructing another binary tree:
#       10
#      /   \
#     20   30
#   /   \
#  40   60
root2 = Node(10)
root2.left = Node(20)
root2.right = Node(30)
root2.left.left = Node(40)
root2.left.right = Node(60)

solution = Solution()
dll_head2 = solution.bToDLL(root2)
print("DLL from left to right:")
print_dll(dll_head2)  # Expected Output: 40 20 60 10 30
print("DLL from right to left:")
print_dll_reverse(dll_head2)  # Expected Output: 30 10 60 20 40

'''
Here's a line-by-line breakdown of the code in plain text.

Define a Node class: This class represents a node in a binary tree.
Attributes:
left: points to the left child of the node.
data: holds the node's value.
right: points to the right child of the node.

Define the Solution class: This class contains methods and properties to convert a binary tree to a doubly linked list (DLL).
Attributes:
head: stores the head of the DLL, initially set to None.
prev: tracks the previous node in the DLL during in-order traversal, initially set to None.

Define the bToDLL function in Solution: This function converts a binary tree to a DLL using in-order traversal.
Parameters:
root: the root node of the binary tree.

Define inorder_convert function within bToDLL: This recursive function performs an in-order traversal to link nodes in correct order for a DLL.
Parameters:
node: the current node being processed.

Check if node is None: If node is None, the function returns, allowing traversal to continue or terminate at a leaf.

Traverse the left subtree recursively: This ensures left subtree nodes are added first in the DLL.

Check if prev is None: If prev is None, this is the first node in the traversal, making it the head of the DLL.
Set self.head to node, designating it as the head of the DLL.

Link prev and the current node if prev is not None:
Set self.prev.right to node to link the previous node's right pointer to the current node.
Set node.left to self.prev, establishing a link back to the previous node.

Move prev to the current node: Update self.prev to node, marking it as the last node added to the DLL.

Traverse the right subtree recursively: This completes the in-order traversal, adding right-side nodes.

Return self.head after conversion is complete: The head of the DLL is now established and returned.

Helper functions to print the DLL:

Define print_dll: This function prints the DLL from left to right.
Parameters:
head: the head of the DLL.
Traverse each node from left to right, printing the data value.

Define print_dll_reverse: This function prints the DLL from right to left.
Parameters:
head: the head of the DLL.
Move to the rightmost node, then traverse leftward, printing each node's data value.

Test Cases:

Construct binary tree root1: Tree structure:
    1
   / \
  3   2
Create an instance of Solution and call bToDLL with root1: Convert the binary tree to a DLL and store the head in dll_head1.

Print DLL from left to right and right to left for root1:
Expected output (left to right): 3 1 2
Expected output (right to left): 2 1 3

Construct binary tree root2: Tree structure:
    10
   /   \
  20   30
 /  \
40  60
Create another instance of Solution and call bToDLL with root2: Convert the binary tree to a DLL and store the head in dll_head2.

Print DLL from left to right and right to left for root2:
Expected output (left to right): 40 20 60 10 30
Expected output (right to left): 30 10 60 20 40
'''