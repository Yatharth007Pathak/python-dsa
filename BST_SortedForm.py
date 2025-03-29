"""
Given two BSTs, return elements of merged BSTs in sorted form.

Examples :

Input:
BST1:
       5
     /   \
    3     6
   / \
  2   4  
BST2:
        2
      /   \
     1     3
            \
             7
            /
           6
Output: 1 2 2 3 3 4 5 6 6 7
Explanation: After merging and sorting the two BST we get 1 2 2 3 3 4 5 6 6 7.

Input:
BST1:
       12
     /   
    9
   / \    
  6   11
BST2:
      8
    /  \
   5    10
  /
 2
Output: 2 5 6 8 9 10 11 12
Explanation: After merging and sorting the two BST we get 2 5 6 8 9 10 11 12.
"""

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def in_order_traversal(self, root):
        if not root:
            return []
        # Traverse left, root, right
        return self.in_order_traversal(root.left) + [root.data] + self.in_order_traversal(root.right)

    def merge(self, root1, root2):
        # Get sorted lists from both BSTs
        list1 = self.in_order_traversal(root1)
        list2 = self.in_order_traversal(root2)
        
        # Merge the two sorted lists
        merged_list = []
        i, j = 0, 0
        while i < len(list1) and j < len(list2):
            if list1[i] < list2[j]:
                merged_list.append(list1[i])
                i += 1
            else:
                merged_list.append(list2[j])
                j += 1
        
        # If there are remaining elements in list1
        while i < len(list1):
            merged_list.append(list1[i])
            i += 1
            
        # If there are remaining elements in list2
        while j < len(list2):
            merged_list.append(list2[j])
            j += 1
        
        return merged_list

# Example usage
def build_bst1():
    # Build first BST
    root1 = Node(5)
    root1.left = Node(3)
    root1.right = Node(6)
    root1.left.left = Node(2)
    root1.left.right = Node(4)
    return root1

def build_bst2():
    # Build second BST
    root2 = Node(2)
    root2.left = Node(1)
    root2.right = Node(3)
    root2.right.right = Node(7)
    root2.right.right.left = Node(6)
    return root2

solution = Solution()
bst1 = build_bst1()
bst2 = build_bst2()
result = solution.merge(bst1, bst2)
print("Merged sorted elements:", result)  # Output: 1 2 2 3 3 4 5 6 6 7

'''
Let's break down the provided code that merges two Binary Search Trees (BSTs) into a sorted list, step by step.

class Node:
This defines a node in a binary tree.

def __init__(self, val):
Initializes a new node with a value val.
Sets self.data to val, and initializes self.left and self.right to None (indicating no children initially).

class Solution:
This defines a class Solution that contains methods for working with BSTs.

def in_order_traversal(self, root):
This method performs an in-order traversal of the BST.

if not root:
Checks if the current node (root) is None. If it is, returns an empty list.
return self.in_order_traversal(root.left) + [root.data] + self.in_order_traversal(root.right)
Recursively traverses the left subtree, appends the current node's data, and then traverses the right subtree. 
This results in a sorted list of values from the BST since in-order traversal of a BST visits nodes in ascending order.

def merge(self, root1, root2):
This method merges two BSTs.
list1 = self.in_order_traversal(root1)
list2 = self.in_order_traversal(root2)
Calls in_order_traversal on both BST roots (root1 and root2) to obtain two sorted lists of their elements.

merged_list = []
Initializes an empty list to store the merged sorted elements.

i, j = 0, 0
Initializes two pointers, i and j, to traverse list1 and list2, respectively.

while i < len(list1) and j < len(list2):
Merges the two sorted lists:

if list1[i] < list2[j]:
If the current element in list1 is smaller, append it to merged_list and move to the next element in list1.

else:
If the current element in list2 is smaller or equal, append it to merged_list and move to the next element in list2.

Remaining Elements:
The following two while loops append any remaining elements in list1 or list2 to merged_list:
while i < len(list1):
    merged_list.append(list1[i])
    i += 1
while j < len(list2):
    merged_list.append(list2[j])
    j += 1

return merged_list
Returns the fully merged list of sorted elements from both BSTs.

def build_bst1(): and def build_bst2():
These functions build two example BSTs for testing:
build_bst1 creates the following BST:
      5
    /   \
   3     6
  / \
 2   4

build_bst2 creates the following BST:
      2
    /   \
   1     3
          \
           7
          /
         6

solution = Solution()
Creates an instance of the Solution class.

bst1 = build_bst1() and bst2 = build_bst2()
Calls the build functions to create the two BSTs.

result = solution.merge(bst1, bst2)
Calls the merge method to merge the two BSTs and store the result.

print("Merged sorted elements:", result)
Prints the merged sorted elements. The expected output is:
Merged sorted elements: [1, 2, 2, 3, 3, 4, 5, 6, 6, 7]
'''