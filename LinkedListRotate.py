"""
Given the head of a singly linked list, the task is to rotate the left shift of the linked list by k nodes, 
where k is a given positive integer smaller than or equal to the length of the linked list.

Examples:

Input: linkedlist: 2->4->7->8->9 , k = 3
Output: 8->9->2->4->7
Explanation:
Rotate 1: 4 -> 7 -> 8 -> 9 -> 2
Rotate 2: 7 -> 8 -> 9 -> 2 -> 4
Rotate 3: 8 -> 9 -> 2 -> 4 -> 7

Input: linkedlist: 1->2->3->4->5->6->7->8 , k = 4
Output: 5->6->7->8->1->2->3->4
"""

class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None

class Solution:
    # Function to rotate the linked list to the left by k nodes
    def rotate(self, head, k):
        if head is None or k == 0:
            return head
        
        # Step 1: Traverse the list to find the k-th node
        current = head
        count = 1
        
        while count < k and current is not None:
            current = current.next
            count += 1
        
        # If k is equal to the length of the list, no rotation is needed
        if current is None or current.next is None:
            return head
        
        # Step 2: current now points to the k-th node; make it the new tail
        kthNode = current
        new_head = current.next
        
        # Step 3: Traverse to the end of the list
        while current.next is not None:
            current = current.next
        
        # Step 4: Link the last node to the old head, making the list circular
        current.next = head
        
        # Step 5: Break the link after the k-th node to finish the rotation
        kthNode.next = None
        
        # new_head is the new head of the rotated list
        return new_head

# Helper function to print the linked list
def printList(head):
    while head:
        print(head.data, end="->" if head.next else "\n")
        head = head.next

# Creating the linked list 2 -> 4 -> 7 -> 8 -> 9
head = Node(2)
head.next = Node(4)
head.next.next = Node(7)
head.next.next.next = Node(8)
head.next.next.next.next = Node(9)

# Rotate by k = 3
solution = Solution()
new_head = solution.rotate(head, 3)

# Print the rotated list
printList(new_head)  # Expected Output: 8->9->2->4->7

'''
Here's a step-by-step breakdown of how the code rotates a linked list to the left by k nodes:

Class Node:
Defines the structure of a single node in a linked list.
The __init__ method initializes each node with a data value and a next pointer set to None initially.

Class Solution and Method rotate:
The rotate method in the Solution class rotates the linked list to the left by k nodes.

Initial Checks:
The method checks if the list is empty (head is None) or if k is zero. 
If either condition is true, it returns the head as-is because no rotation is needed.

Finding the k-th Node:
A variable current is initialized to head, and a count is set to 1. 
The method traverses the list until it reaches the k-th node (i.e., the count equals k).
If current reaches None before reaching k nodes, it means k is equal to or greater than the list's length, 
and the method returns the original head as no rotation is necessary.

Setting up the Rotation Point:
After reaching the k-th node, it's stored in kthNode.
The new_head is set to kthNode.next, making it the new head of the rotated list.

Connecting the End of the List to the Original Head:
The method continues traversing the list until it reaches the last node.
The next pointer of the last node is then set to the original head, forming a temporary circular list.

Breaking the Circular Link:
The next pointer of kthNode is set to None to break the circular connection, finalizing the rotation.
The new_head is returned as the head of the rotated list.

Helper Function printList:
This function prints the elements of the linked list starting from head until it reaches the end (None).

Example Execution:
The linked list 2 -> 4 -> 7 -> 8 -> 9 is created, and we call rotate(head, 3).
After rotating left by k=3, the expected output is 8 -> 9 -> 2 -> 4 -> 7. The printList function prints this rotated list.
'''