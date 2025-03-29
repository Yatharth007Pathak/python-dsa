"""
Given the head of a linked list, the task is to reverse this list and return the reversed head.

Examples:

Input: Linked list: 1->2->3->4->5->6
Output: 6->5->4->3->2->1

Input: Linked list: 2->7->10->9->8 
Output: 8->9->10->7->2

Input: Linked List: 10
Output: 10
Explanation: For a single node list, the reverse would be same as original
"""

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

class Solution:
    # Function to reverse a linked list.
    def reverseList(self, head):
        prev = None
        current = head
        
        # Loop through the list and reverse the pointers
        while current:
            next_node = current.next  # Temporarily store the next node
            current.next = prev       # Reverse the current node's pointer
            prev = current            # Move prev to this node
            current = next_node       # Move to the next node
            
        # prev will be the new head of the reversed list
        return prev

# Helper function to create a linked list from a list of values
def createLinkedList(arr):
    if not arr:
        return None
    head = Node(arr[0])
    current = head
    for value in arr[1:]:
        current.next = Node(value)
        current = current.next
    return head

# Helper function to print the linked list
def printLinkedList(head):
    current = head
    while current:
        print(current.data, end="->" if current.next else "\n")
        current = current.next

# Example usage:
sol = Solution()

# Test case 1
arr1 = [1, 2, 3, 4, 5, 6]
head1 = createLinkedList(arr1)
print("Original List:")
printLinkedList(head1)
reversed_head1 = sol.reverseList(head1)
print("Reversed List:")
printLinkedList(reversed_head1)

# Test case 2
arr2 = [2, 7, 10, 9, 8]
head2 = createLinkedList(arr2)
print("\nOriginal List:")
printLinkedList(head2)
reversed_head2 = sol.reverseList(head2)
print("Reversed List:")
printLinkedList(reversed_head2)

# Test case 3
arr3 = [10]
head3 = createLinkedList(arr3)
print("\nOriginal List:")
printLinkedList(head3)
reversed_head3 = sol.reverseList(head3)
print("Reversed List:")
printLinkedList(reversed_head3)

'''
Here's line-by-line breakdown of the code:

Class Node:
Defines a class called Node which represents each element or "node" in a linked list.

Method __init__ in Node class:
The constructor initializes a node with a value (val) passed as an argument.
self.data = val sets the data attribute of the node to val.
self.next = None sets the next pointer of the node to None, indicating the end of the list initially.

Class Solution:
Defines a class called Solution which contains methods to operate on linked lists.

Method reverseList in Solution class:
A method to reverse the linked list, taking the head node (head) as an argument.

Initial Setup in reverseList:
prev = None initializes a variable prev to store the previous node during reversal. Initially, it's None as there is no previous node.
current = head sets current to the head node of the list, to start traversing from the beginning.

Loop through the list:
while current: This loop will continue as long as current is not None (indicating nodes remain in the list).

Inside the loop:
next_node = current.next stores the next node temporarily, so it isn't lost when we reverse the link.
current.next = prev reverses the current node's next pointer to point to the previous node instead of the next node.
prev = current moves prev to the current node, so it will be the previous node in the next iteration.
current = next_node advances current to the next node, which we stored earlier in next_node.

Return the new head:
After the loop, prev will point to the last node processed, which is the new head of the reversed list. This is returned as the result.

Helper Function createLinkedList:
A function to create a linked list from a list of values (arr).
if not arr: checks if the list is empty and returns None if true.
head = Node(arr[0]) creates the first node (head) with the first value in arr.
current = head sets current to point to the head node to start building the rest of the list.
for value in arr[1:]: loops through the rest of the values.
current.next = Node(value) creates a new node with the current value and links it to the next of current.
current = current.next moves current to the new node to continue building.
Finally, head is returned as the starting node of the created linked list.

Helper Function printLinkedList:
A function to print each node in the linked list, given the head node (head).
current = head initializes current to the head node.
while current: loops through each node in the list until current is None.
print(current.data, end="->" if current.next else "\n") prints data of the current node. 
If there is a next node, it prints "->" after the value; otherwise, it prints a newline.
current = current.next advances to the next node.

Example Usage Section:
This part demonstrates how to use the classes and functions defined.

Creating an instance of Solution:
sol = Solution() creates an instance of the Solution class.

Test Case 1:
arr1 = [1, 2, 3, 4, 5, 6] defines a list of values for the linked list.
head1 = createLinkedList(arr1) creates a linked list from arr1.
print("Original List:") prints a heading for the original list.
printLinkedList(head1) prints the original linked list.
reversed_head1 = sol.reverseList(head1) reverses the linked list.
print("Reversed List:") prints a heading for the reversed list.
printLinkedList(reversed_head1) prints the reversed linked list.

Test Case 2:
Similar to Test Case 1 but with arr2 = [2, 7, 10, 9, 8] as the list values.

Test Case 3:
Similar to the other test cases but with arr3 = [10], which has only one value.
'''