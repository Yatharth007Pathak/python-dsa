"""
Given a singly linked list: A0→A1→...→An-2→An-1, reorder it to A0→An-1→A1→An-2→A2→An-3→...
For example: Given 1->2->3->4->5 its reorder is 1->5->2->4->3.

Examples:

Input: LinkedList: 1->2->3
Output: 1->3->2
Explanation: Here n=3, so the correct order is A0→A2→A1

Input: LinkedList: 1->7->3->4
Output: 1->4->7->3
Explanation: Here n=4, so the correct order is A0→A3→A1→A2
"""

class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None

class Solution:
    def reorderList(self, head):
        if not head or not head.next or not head.next.next:
            return
        
        # Step 1: Find the middle of the list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Split into two halves
        second = slow.next
        slow.next = None
        
        # Step 2: Reverse the second half
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        second = prev
        
        # Step 3: Merge the two halves
        first = head
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2

# Helper function to create a linked list
def createLinkedList(arr):
    if not arr:
        return None
    head = Node(arr[0])
    curr = head
    for value in arr[1:]:
        curr.next = Node(value)
        curr = curr.next
    return head

# Helper function to print a linked list
def printLinkedList(head):
    result = []
    while head:
        result.append(head.data)
        head = head.next
    print("->".join(map(str, result)))

# Test case
arr = [1, 7, 3, 4]
head = createLinkedList(arr)
Solution().reorderList(head)
printLinkedList(head)

'''

Here's a detailed step-by-step explanation of the reorderList function, followed by how it works with the helper functions:

Class Definitions
class Node:
Defines a class Node for representing a single node in the linked list.

__init__(self, data):
Initializes a Node with data and sets its next pointer to None.
class Solution:
Defines the Solution class containing the reorderList method.

Reorder Function
def reorderList(self, head):
Reorders the linked list as per the specified pattern:
First node → Last node → Second node → Second last node → ...

Base Cases
if not head or not head.next or not head.next.next:
If the list has fewer than three nodes, no reordering is needed, so return immediately.

Step 1: Find the Middle of the List

slow, fast = head, head
Initializes two pointers, slow and fast, to traverse the list.

while fast and fast.next:
Advances slow by one step and fast by two steps to locate the middle node.

slow = slow.next and fast = fast.next.next
Updates slow and fast. When the loop ends, slow points to the middle of the list.

second = slow.next and slow.next = None
Splits the list into two halves.

The first half starts from head.
The second half starts from slow.next.
slow.next is set to None to terminate the first half.

Step 2: Reverse the Second Half

prev = None
Initializes prev to None for reversing the second half.

while second:
Iterates through the second half of the list.

temp = second.next
Temporarily stores the next node.

second.next = prev
Reverses the current node’s link.

prev = second and second = temp
Updates prev to the current node and second to the next node.

When the loop ends, prev points to the new head of the reversed second half.
second = prev
Assigns prev (reversed list head) to second.

Step 3: Merge the Two Halves

first = head
Initializes first to traverse the first half.

while second:
Iterates through the reversed second half and merges it with the first half.

temp1, temp2 = first.next, second.next
Stores the next nodes of first and second.

first.next = second
Links the current node of the first half to the current node of the second half.

second.next = temp1
Links the current node of the second half to the next node of the first half.

first, second = temp1, temp2
Advances first and second to their respective next nodes.

Helper Functions
createLinkedList(arr):
Creates a linked list from an array.

Loops through the array, creating Node objects, and links them.
printLinkedList(head):
Prints the linked list as a string of values connected by ->.

Execution

Input
arr = [1, 7, 3, 4]
Creates a linked list: 1 -> 7 -> 3 -> 4.
Reorder Operation

Step 1: Find middle of 1 -> 7 -> 3 -> 4.

Middle node: 7.
Splits into 1 -> 7 and 3 -> 4.
Step 2: Reverse 3 -> 4.

Becomes 4 -> 3.
Step 3: Merge 1 -> 7 and 4 -> 3.

Result: 1 -> 4 -> 7 -> 3.
'''