"""
Given a Binary Tree, find the In-Order Traversal of it.
In inorder traversal, nodes are visited in the order of: left subtree, root, and then right subtree. 
The output from each tree is displayed in the format specified in the print statements.

Examples:

Input:
       1
     /  \
    3    2
Output: [3, 1, 2]
Explanation: The in-order traversal of the given binary tree is [3, 1, 2].

Input:
        10
     /      \ 
    20       30 
  /    \    /
 40    60  50
Output: [40, 20, 60, 10, 50, 30]
Explanation: The in-order traversal of the given binary tree is [40, 20, 60, 10, 50, 30].
"""

# Node Class
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    # Function to return a list containing the inorder traversal of the tree.
    def InOrder(self, root):
        result = []
        self._inorder_helper(root, result)
        return result

    def _inorder_helper(self, node, result):
        if node:
            self._inorder_helper(node.left, result)  # Traverse left
            result.append(node.data)  # Visit the root
            self._inorder_helper(node.right, result)  # Traverse right

# Test Cases
if __name__ == "__main__":
    # Example 1
    root1 = Node(1)
    root1.left = Node(3)
    root1.right = Node(2)

    solution = Solution()
    print("In-Order Traversal of Tree 1:", solution.InOrder(root1))  # Output: [3, 1, 2]

    # Example 2
    root2 = Node(10)
    root2.left = Node(20)
    root2.right = Node(30)
    root2.left.left = Node(40)
    root2.left.right = Node(60)
    root2.right.left = Node(50)

    print("In-Order Traversal of Tree 2:", solution.InOrder(root2))  # Output: [40, 20, 60, 10, 50, 30]

'''
Here's a line-by-line breakdown of the provided code:

Define a class Node: This class represents a single node in a binary tree.

Initialize the Node class with a value: The constructor takes a parameter val and assigns it to the data attribute of the node.

Set the left and right attributes to None: These attributes represent the left and right children of the node and are initially set to None.

Define a class Solution: This class will contain methods for performing operations on the binary tree, specifically the inorder traversal.

Define the method InOrder within Solution: This method takes the root of the tree as an argument and 
returns a list of values from the inorder traversal.

Initialize an empty list called result: This list will store the values of nodes visited during the traversal.

Call the helper method _inorder_helper: This method performs the actual traversal, taking the root node and the result list as arguments.

Return the result list: After the traversal is complete, return the list containing the values in inorder.

Define the helper method _inorder_helper: This method takes a node and the result list as arguments to perform the recursive inorder traversal.

Check if the current node is not None: If the node exists, proceed with the traversal.

Recursively call _inorder_helper for the left child: This traverses the left subtree first.

Append the node's value to the result list: This marks the visit to the root node after traversing the left subtree.

Recursively call _inorder_helper for the right child: This traverses the right subtree after visiting the root.

Begin testing the traversal in the main block: This block runs when the script is executed directly.

Create the first tree (root1): Initialize nodes and set their left and right children to create a specific tree structure.

Instantiate the Solution class: Create an instance to use the InOrder method.

Print the inorder traversal of Tree 1: Call the InOrder method with root1 and display the result.

Create the second tree (root2): Initialize another tree structure with different nodes and more levels.

Print the inorder traversal of Tree 2: Call the InOrder method with root2 and display the result.
'''