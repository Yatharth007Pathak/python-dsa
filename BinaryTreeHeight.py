"""
Given a binary tree, find its height.

Example 1:
Input:
     1
    /  \
   2    3
Output: 2

Example 2:
Input:
  2
   \
    1
   /
 3
Output: 3   
"""

# Node class to represent each node of the binary tree
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    # Function to find the height of a binary tree
    def height(self, root):
        # Base case: if the root is None, the height is 0
        if root is None:
            return 0
        
        # Recursive case: height of tree is 1 + max of left and right subtree heights
        left_height = self.height(root.left)
        right_height = self.height(root.right)
        
        return 1 + max(left_height, right_height)

# Helper function to create a binary tree manually for testing
def create_example_tree_1():
    # Creating the binary tree from the first example:
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    return root

def create_example_tree_2():
    # Creating the binary tree from the second example:
    root = Node(2)
    root.right = Node(1)
    root.right.left = Node(3)
    return root

# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    tree1 = create_example_tree_1()
    result1 = sol.height(tree1)
    print(f"Height of tree 1: {result1}")  # Output should be 2

    # Test case 2
    tree2 = create_example_tree_2()
    result2 = sol.height(tree2)
    print(f"Height of tree 2: {result2}")  # Output should be 3

'''
Here's a line-by-line breakdown of the code that calculates the height of a binary tree:

Node Class Definition

class Node:
Defines a class Node to represent each node in the binary tree.

def __init__(self, val):
The constructor method initializes the node with:
self.data = val: The value or data stored in the node.
self.left = None: A pointer to the left child, initially set to None.
self.right = None: A pointer to the right child, initially set to None.

Solution Class Definition

class Solution:
Defines the class Solution that contains methods to operate on the binary tree.

def height(self, root):
A method that calculates the height of the binary tree rooted at root.
Base Case (Height of Empty Tree)

if root is None:
Checks if the root node is None, meaning the tree is empty.

return 0
If the tree is empty, the height is 0.

Recursive Case (Height of Non-Empty Tree)
left_height = self.height(root.left)

Recursively calculates the height of the left subtree.
right_height = self.height(root.right)

Recursively calculates the height of the right subtree.
return 1 + max(left_height, right_height)

The height of the current node is 1 plus the maximum of the left and right subtree heights.
Helper Functions to Create Example Trees

def create_example_tree_1():
A function to manually create a binary tree for testing (Example 1):
root = Node(1): Creates the root node with value 1.
root.left = Node(2): Creates a left child with value 2.
root.right = Node(3): Creates a right child with value 3.
return root: Returns the root of this binary tree.

def create_example_tree_2():
A function to manually create another binary tree for testing (Example 2):
root = Node(2): Creates the root node with value 2.
root.right = Node(1): Creates a right child with value 1.
root.right.left = Node(3): Creates a left child under the right child with value 3.
return root: Returns the root of this binary tree.

Test Cases

if __name__ == "__main__":
This block ensures that the test cases will only run if the script is executed directly.

Test Case 1
tree1 = create_example_tree_1()
Calls the create_example_tree_1 function to create a binary tree for the first test case.

result1 = sol.height(tree1)
Calls the height method on tree1 and stores the result in result1.

print(f"Height of tree 1: {result1}")
Prints the height of the first tree, which should be 2.

Test Case 2

tree2 = create_example_tree_2()
Calls the create_example_tree_2 function to create a binary tree for the second test case.

result2 = sol.height(tree2)
Calls the height method on tree2 and stores the result in result2.

print(f"Height of tree 2: {result2}")
Prints the height of the second tree, which should be 3.

Explanation of Output
Tree 1: The height of the tree is 2, as it has two levels.
Tree 2: The height of the tree is 3, as it has three levels.

Time Complexity
The time complexity of the height method is O(n), where n is the number of nodes in the binary tree, because each node is visited once.
'''