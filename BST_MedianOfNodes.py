"""
Given a Binary Search Tree of size N, find the Median of its Node values.

Example 1:
Input:
       6
     /   \
   3      8   
 /  \    /  \
1    4  7    9
Output: 6
Explanation: Inorder of Given BST will be: 1, 3, 4, 6, 7, 8, 9. So, here median will 6.

Example 2:
Input:
       6
     /   \
   3      8   
 /   \    /   
1    4   7   
Output: 5
Explanation:Inorder of Given BST will be: 1, 3, 4, 6, 7, 8. So, here median will (4 + 6)/2 = 10/2 = 5.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    # Function to count the number of nodes in the BST
    def countNodes(self, root):
        if root is None:
            return 0
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
    
    # Helper function to perform inorder traversal and find the median
    def inorderTraversal(self, root, nodes_list):
        if root is None:
            return
        # Traverse the left subtree
        self.inorderTraversal(root.left, nodes_list)
        # Append the current node value to the list
        nodes_list.append(root.data)
        # Traverse the right subtree
        self.inorderTraversal(root.right, nodes_list)
    
    # Function to find the median of the BST
    def findMedian(self, root):
        if root is None:
            return 0
        
        # Step 1: Count the total number of nodes in the BST
        n = self.countNodes(root)
        
        # Step 2: Perform inorder traversal to get nodes in sorted order
        nodes_list = []
        self.inorderTraversal(root, nodes_list)
        
        # Step 3: Find the median based on the number of nodes (odd or even)
        if n % 2 == 1:
            # Odd number of nodes, median is the middle element
            return nodes_list[n // 2]
        else:
            # Even number of nodes, median is the average of the two middle elements
            return (nodes_list[n // 2 - 1] + nodes_list[n // 2]) / 2

# Example usage
if __name__ == "__main__":
    # Example 1:
    root1 = Node(6)
    root1.left = Node(3)
    root1.right = Node(8)
    root1.left.left = Node(1)
    root1.left.right = Node(4)
    root1.right.left = Node(7)
    root1.right.right = Node(9)
    
    solution = Solution()
    print(solution.findMedian(root1))  # Output: 6

    # Example 2:
    root2 = Node(6)
    root2.left = Node(3)
    root2.right = Node(8)
    root2.left.left = Node(1)
    root2.left.right = Node(4)
    root2.right.left = Node(7)
    
    print(solution.findMedian(root2))  # Output: 5
