"""
Given the head of a linked list, the task is to find the middle. For example, the middle of 1-> 2->3->4->5 is 3. 
If there are two middle nodes (even count), return the second middle. For example, middle of 1->2->3->4->5->6 is 4.

Examples:

Input: Linked list: 1->2->3->4->5
Output: 3
Explanation: The given linked list is 1->2->3->4->5 and its middle is 3.

Input: Linked list: 2->4->6->7->5->1
Output: 7 
Explanation: The given linked list is 2->4->6->7->5->1 and its middle is 7.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    # Function to return the data of the middle node. If the linked list is empty, return -1.
    def getMiddle(self, head):
        if not head:
            return -1  # Return -1 if the linked list is empty
        
        slow = head
        fast = head
        
        # Move slow pointer by 1 and fast pointer by 2
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # When the fast pointer reaches the end, the slow pointer will be at the middle
        return slow.data

# Example usage:

# Helper function to create a linked list from a list
def createLinkedList(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for value in arr[1:]:
        current.next = Node(value)
        current = current.next
    return head

# Test case examples
arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4, 6, 7, 5, 1]

# Creating linked lists
head1 = createLinkedList(arr1)
head2 = createLinkedList(arr2)

# Instantiate the solution class
sol = Solution()

# Getting the middle of each list
print(sol.getMiddle(head1))  # Expected output: 3
print(sol.getMiddle(head2))  # Expected output: 7

'''
Here's a breakdown of each part of the code:

Class Node:
Defines a class called Node, which represents an element (or node) in a linked list.

Method __init__ in Node class:
This constructor initializes a node with a data value passed as an argument.
self.data = data sets the data attribute of the node to the provided value.
self.next = None initializes the next pointer to None, indicating that there is no subsequent node initially.

Class Solution:
Defines a class called Solution, which contains methods to operate on linked lists.

Method getMiddle in Solution class:
This method returns the data of the middle node of the linked list, or -1 if the list is empty.

Check for empty list:
if not head: checks if the head of the linked list is None (indicating the list is empty).
return -1 returns -1 if the linked list is empty.

Initialize pointers:
slow = head sets the slow pointer to the head node, which will move one step at a time.
fast = head sets the fast pointer to the head node, which will move two steps at a time.

Loop to find the middle:
while fast and fast.next: continues as long as the fast pointer is not None and fast.next is also not None.

Inside the loop:
slow = slow.next moves the slow pointer one step forward.
fast = fast.next.next moves the fast pointer two steps forward.

Return the middle node data:
Once the loop finishes (when fast reaches the end of the list), slow will be positioned at the middle node.
return slow.data returns the data stored in the middle node.

Helper Function createLinkedList:
A function to create a linked list from a list of values (arr).
if not arr: checks if the input list is empty and returns None if true.
head = Node(arr[0]) creates the first node (head) with the first value in the array.
current = head initializes current to point to the head node for building the list.
for value in arr[1:]: iterates through the remaining values in the array.
current.next = Node(value) creates a new node for each value and links it to the current node.
current = current.next moves current to the newly created node to continue linking.
Finally, head is returned as the starting node of the linked list.

Example Usage Section:
This section demonstrates how to use the classes and functions defined.

Test Case Arrays:
arr1 = [1, 2, 3, 4, 5] defines an array for the first linked list.
arr2 = [2, 4, 6, 7, 5, 1] defines an array for the second linked list.

Creating Linked Lists:
head1 = createLinkedList(arr1) creates the first linked list from arr1.
head2 = createLinkedList(arr2) creates the second linked list from arr2.

Instantiate the Solution Class:
sol = Solution() creates an instance of the Solution class.

Get Middle Node Data:
print(sol.getMiddle(head1)) calls the getMiddle method with head1 and prints the middle value of the first linked list, which is 3.
print(sol.getMiddle(head2)) calls the getMiddle method with head2 and prints the middle value of the second linked list, which is 7.
'''