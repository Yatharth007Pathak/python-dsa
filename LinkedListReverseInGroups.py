"""
Given a linked list, the task is to reverse every k node (where k is an input to the function) in the linked list. 
If the number of nodes is not a multiple of k then left-out nodes, in the end, should be considered as a group and must be reversed 
(See Example 2 for clarification).

Examples:

Input: Linked List: 1->2->2->4->5->6->7->8, k = 4
Output: 4 -> 2 -> 2 -> 1 -> 8 -> 7 -> 6 -> 5 
Explanation: The first 4 elements 1,2,2,4 are reversed first and then the next 4 elements 5,6,7,8. 
Hence, the resultant linked list is 4->2->2->1->8->7->6->5.

Input: LinkedList: 1->2->3->4->5, k = 3
Output: 3 -> 2 -> 1 -> 5 -> 4
Explanation: The first 3 elements 1,2,3 are reversed first and then element 4,5 are reversed. Hence, the resultant linked list is 3->2->1->5->4.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def reverse(self, head, k):
        if head is None:
            return None

        current = head
        prev = None
        next_node = None
        count = 0

        # Step 1: Reverse the first k nodes
        while current is not None and count < k:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            count += 1

        # Step 2: Recursively call for the next group of k nodes
        if next_node is not None:
            head.next = self.reverse(next_node, k)

        # Step 3: Return the new head of the reversed list
        return prev

# Helper function to create a linked list from a list
def create_linked_list(values):
    head = Node(values[0])
    current = head
    for value in values[1:]:
        current.next = Node(value)
        current = current.next
    return head

# Helper function to print linked list
def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

# Test the reverse function
values = [1, 2, 2, 4, 5, 6, 7, 8]
k = 4
head = create_linked_list(values)

solution = Solution()
new_head = solution.reverse(head, k)
print_linked_list(new_head)

'''
Here's an explanation of the code:

Node Class:
Defines a Node class to represent a node in a linked list, where data holds the value of the node and next is a reference to the next node.

Solution Class:
Contains the reverse function that reverses nodes of the linked list in groups of size k.

reverse(self, head, k):
Base Case: If head is None, it means the list is empty, so it returns None.
Step 1: The function initializes current to head, and prev and next_node to None. 
It then reverses the first k nodes in the list using a while loop that runs until count < k.

Inside the loop:
It stores current.next in next_node.
Reverses the next pointer of current to point to prev.
Moves prev to current and current to next_node.
Increments count to keep track of the number of nodes reversed.
Step 2: If there are more nodes to process, it recursively calls reverse for the next group of k nodes. 
It attaches the returned head of the reversed sublist to head.next.
Step 3: Returns prev, which becomes the new head of the reversed segment.

Helper Functions:
create_linked_list(values): Creates a linked list from a given list of values.
print_linked_list(head): Prints the linked list in a readable format.

Example Usage:

Linked List Creation:
The list [1, 2, 2, 4, 5, 6, 7, 8] is created as a linked list with create_linked_list.

Reversal and Printing:
Calls solution.reverse(head, k) to reverse the list in groups of 4.
print_linked_list(new_head) prints the modified linked list.

Expected Output:
For values = [1, 2, 2, 4, 5, 6, 7, 8] and k = 4:
4 -> 2 -> 2 -> 1 -> 8 -> 7 -> 6 -> 5 -> None
'''