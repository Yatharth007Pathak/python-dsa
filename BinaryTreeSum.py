"""
Given a Binary Tree of size N, your task is to complete the function sumBt(), 
that should return the sum of all the nodes of the given binary tree.

Input:
First line of input contains the number of test cases T. For each test case, there will be two lines:
First line of each test case will be an integer N denoting the number of parent child relationships.
Second line of each test case will print the level order traversal of the tree in the form of N space separated triplets. 
The description of triplets is as follows:
Each triplet will contain three space-separated elements of the form (int, int char).
The first integer element will be the value of parent. 
The second integer will be the value of corresponding left or right child. In case the child is null, this value will be -1.
The third element of triplet which is a character can take any of the three values 'L', 'R' or 'N'. 
L denotes that the children is a left child, R denotes that the children is a Right Child and N denotes that the child is NULL.

Please note that the relationships are printed only for internal nodes and not for leaf nodes.

Output:
The function should return the sum of all the nodes of the binary tree.
"""

# Node class for creating nodes of the binary tree
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Function to compute the sum of all nodes in the binary tree
def sumBT(root):
    if root is None:
        return 0
    # Recursively compute the sum of left and right subtrees and add the root's data
    return root.data + sumBT(root.left) + sumBT(root.right)

# Helper function to build the binary tree from input
def buildTree(relationships, N):
    # Dictionary to store node references
    nodes = {}
    
    # Create nodes and build relationships
    for i in range(N):
        parent_val, child_val, position = relationships[i]
        
        # Get or create the parent node
        if parent_val not in nodes:
            nodes[parent_val] = Node(parent_val)
        parent_node = nodes[parent_val]
        
        # Handle non-null child
        if child_val != -1:
            if child_val not in nodes:
                nodes[child_val] = Node(child_val)
            child_node = nodes[child_val]
            
            # Attach child to parent based on position
            if position == 'L':
                parent_node.left = child_node
            elif position == 'R':
                parent_node.right = child_node
    
    # Return the root node (which should be the node with value `relationships[0][0]`)
    return nodes[relationships[0][0]]

# Driver function to read input and process multiple test cases
def main():
    # Sample Input with 2 test cases
    test_cases = [
        (3, [(1, 2, 'L'), (1, 3, 'R'), (2, 4, 'L')]),
        (4, [(10, 20, 'L'), (10, 30, 'R'), (20, 40, 'L'), (30, 50, 'R')])
    ]
    
    # Process each test case
    for relationships_data in test_cases:
        N, relationships = relationships_data
        
        # Build the tree from the relationships
        root = buildTree(relationships, N)
        
        # Calculate the sum of all nodes in the tree
        result = sumBT(root)
        
        # Print the result for this test case
        print(result)

# Call the main function to run the program
if __name__ == "__main__":
    main()

'''
Here's a breakdown of the code, explaining each part:

Node Class:
class Node:
This defines the structure of a node in the binary tree.

def __init__(self, val):
Constructor for the Node class, which initializes:

self.data = val
Stores the value (val) of the node.

self.left = None
Initializes the left child of the node as None.

self.right = None
Initializes the right child of the node as None.

sumBT Function:
def sumBT(root):
This function recursively computes the sum of all nodes in the binary tree.

if root is None:
Checks if the tree or subtree is empty. If root is None, the function returns 0.

return root.data + sumBT(root.left) + sumBT(root.right)
If the node is not None, it adds the current node's data (root.data) to the sum of the left subtree and the right subtree, computed recursively.

buildTree Function:
def buildTree(relationships, N):
This function builds the binary tree based on relationships between parent and child nodes, given in the form of tuples.

nodes = {}
Initializes a dictionary to store node references, with node values as keys.

for i in range(N):
Iterates through the relationships list to process each relationship.

parent_val, child_val, position = relationships[i]
Unpacks the parent node value (parent_val), child node value (child_val), 
and position (position - either 'L' for left or 'R' for right) from the current relationship tuple.

if parent_val not in nodes:
Checks if the parent node has already been created. If not, it creates a new Node for the parent.

parent_node = nodes[parent_val]
Retrieves the parent node from the nodes dictionary.

if child_val != -1:
Checks if the child node is not -1 (which would indicate no child).

if child_val not in nodes:
Checks if the child node has already been created. If not, it creates a new Node for the child.

child_node = nodes[child_val]
Retrieves the child node from the nodes dictionary.

if position == 'L':
Attaches the child node to the parent's left child if the position is 'L' (left).

elif position == 'R':
Attaches the child node to the parent's right child if the position is 'R' (right).

return nodes[relationships[0][0]]
After all relationships are processed, the function returns the root node (which is the parent node of the first relationship).

main Function:
def main():
This function handles multiple test cases and coordinates the tree-building and sum calculation.

test_cases = [...]
A list containing test cases. Each test case consists of the number of relationships N and 
a list of tuples representing the relationships between nodes.

for relationships_data in test_cases:
Loops through each test case.

N, relationships = relationships_data
Unpacks the number of relationships (N) and the relationships list for the current test case.

root = buildTree(relationships, N)
Calls the buildTree function to construct the binary tree from the relationships.

result = sumBT(root)
Calls the sumBT function to calculate the sum of all nodes in the tree.

print(result)
Prints the result of the sum for the current test case.

Execution:
if __name__ == "__main__":
This checks if the script is being run directly (not imported as a module), and if so, it calls the main() function to start the program.
Example Input and Output:
Test Case 1:

Input: (3, [(1, 2, 'L'), (1, 3, 'R'), (2, 4, 'L')])
Output: 10 (sum of nodes 1 + 2 + 3 + 4)
Test Case 2:

Input: (4, [(10, 20, 'L'), (10, 30, 'R'), (20, 40, 'L'), (30, 50, 'R')])
Output: 150 (sum of nodes 10 + 20 + 30 + 40 + 50)
'''