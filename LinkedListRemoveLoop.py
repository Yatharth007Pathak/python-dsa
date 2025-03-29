"""
Given the head of a linked list that may contain a loop.  A loop means that the last node of the linked list is connected back 
to a node in the same list.  So if the next of the previous node is null. then there is no loop.  Remove the loop from the linked list, 
if it is present (we mainly need to make the next of the last node null). Otherwise, keep the linked list as it is.

Note: Given an integer, pos (1 based index)  Position of the node to which the last node links back if there is a loop. 
If the linked list does not have any loop, then pos = 0.
The generated output will be true if your submitted code is correct, otherwise, false.

Examples:

Input: Linked list: 1->3->4, pos = 2
Output: true
Explanation: A loop is present. If you remove it successfully, the answer will be true. 

Input: Linked list: 1->8->3->4, pos = 0
Output: true
Explanation: The Linked list does not contains any loop. 

Input: Linked list: 1->2->3->4, pos = 1
Output: true
Explanation: A loop is present. If you remove it successfully, the answer will be true.



To solve the problem of detecting and removing a loop in a linked list, we can use Floyd's Cycle-Finding Algorithm, 
also known as the "tortoise and hare" algorithm. Here's how it works:

Detect the Loop: Use two pointers, slow and fast, to traverse the list. slow moves one step at a time, while fast moves two steps. 
If there's a loop, slow and fast will eventually meet at some point within the loop.

Find the Loop Start: Once a loop is detected, keep slow at the meeting point and reset fast to the head of the linked list. 
Then, move both slow and fast one step at a time. They will meet at the start of the loop.

Remove the Loop: Once the start of the loop is identified, iterate through the loop to find the last node. 
Set the next of this last node to None, effectively breaking the loop.
"""

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Solution:
    # Function to remove a loop in the linked list.
    def removeLoop(self, head):
        if not head or not head.next:
            return
        
        slow, fast = head, head
        
        # Step 1: Detect loop using the Floyd’s Cycle-Finding Algorithm
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            # If no loop is found, return
            return
        
        # Step 2: Find the starting point of the loop
        slow = head
        if slow == fast:
            # Loop starts at the head, find the end of the loop
            while fast.next != slow:
                fast = fast.next
        else:
            # Loop starts somewhere else, find the entry point of the loop
            while slow.next != fast.next:
                slow = slow.next
                fast = fast.next
        
        # Step 3: Remove the loop by setting the next of the last node to None
        fast.next = None

# Example usage:

# Helper function to create a linked list with a loop for testing
def createLinkedList(arr, pos):
    head = Node(arr[0])
    current = head
    loop_node = None
    for i in range(1, len(arr)):
        current.next = Node(arr[i])
        current = current.next
        if i == pos - 1:
            loop_node = current
    if loop_node:
        current.next = loop_node
    return head

# Test case example
arr = [1, 2, 3, 4]
pos = 1  # Position where the last node links back to form a loop
head = createLinkedList(arr, pos)

# Instantiate the solution and remove the loop
sol = Solution()
sol.removeLoop(head)

# Function to print linked list after loop removal (for validation)
def printLinkedList(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

printLinkedList(head)  # Expected output: 1 -> 2 -> 3 -> 4 -> None

'''
Here's an explanation of each part of this code:

Class Node:
Defines a class called Node, which represents an element (or node) in a linked list.

Method __init__ in Node class:
The constructor initializes a node with a value (val) passed as an argument.
self.data = val sets the data attribute of the node to the provided value.
self.next = None initializes the next pointer to None, indicating there is no subsequent node initially.

Class Solution:
Defines a class called Solution, which contains methods to operate on linked lists.

Method removeLoop in Solution class:
This method removes a loop in the linked list, taking the head node (head) as an argument.

Check for empty or single-node list:
if not head or not head.next: checks if the linked list is empty or has only one node. If true, the method returns since no loop can exist.

Initialize pointers:
slow, fast = head, head initializes two pointers: slow and fast, both pointing to the head node.

Detect loop using Floyd's Cycle-Finding Algorithm:
while fast and fast.next: continues as long as the fast pointer and fast.next are not None.

Inside the loop:
slow = slow.next moves the slow pointer one step forward.
fast = fast.next.next moves the fast pointer two steps forward.
if slow == fast: checks if the two pointers meet, indicating a loop is detected.
break exits the loop if a cycle is found.

Check for no loop found:
The else: block runs if the while loop completes without finding a loop, leading to a return.

Finding the starting point of the loop:
slow = head resets the slow pointer to the head node.
if slow == fast: checks if the loop starts at the head.

If true, it finds the end of the loop:
while fast.next != slow: iterates until fast.next points back to slow.
fast = fast.next moves the fast pointer forward.

Finding the entry point of the loop:

If the loop starts elsewhere:
while slow.next != fast.next: continues until the next nodes of both pointers are equal.

Inside the loop, both pointers are moved one step forward:
slow = slow.next
fast = fast.next

Remove the loop:
fast.next = None breaks the loop by setting the next pointer of the last node in the loop to None.

Example Usage Section:
This section demonstrates how to use the classes and functions defined.

Helper Function createLinkedList:
A function to create a linked list from a list of values (arr) and a position (pos) to form a loop.
head = Node(arr[0]) creates the head node with the first value in the array.
current = head initializes current to point to the head node for building the list.
loop_node = None initializes a variable to keep track of the node that will create the loop.
for i in range(1, len(arr)): iterates through the remaining values in the array.
current.next = Node(arr[i]) creates a new node for each value.
If the current index matches pos - 1, loop_node is set to the current node.
After the loop, if loop_node is found, current.next = loop_node creates the loop by linking the last node to the loop node.
The function returns the head of the created linked list.

Test Case Example:
arr = [1, 2, 3, 4] defines an array for the linked list.
pos = 1 indicates the position where the last node links back to form a loop.
head = createLinkedList(arr, pos) creates a linked list with a loop.

Instantiate the Solution Class:
sol = Solution() creates an instance of the Solution class.

Remove the Loop:
sol.removeLoop(head) calls the removeLoop method with head, which removes the loop from the linked list.

Function printLinkedList:
A function to print the linked list after the loop has been removed for validation.
current = head initializes current to the head node.
while current: loops through each node until current is None.
print(current.data, end=" -> ") prints the data of the current node, followed by " -> ".
After exiting the loop, print("None") indicates the end of the linked list.

Print the Linked List:
printLinkedList(head) prints the linked list after loop removal, with the expected output being 1 -> 2 -> 3 -> 4 -> None.
'''