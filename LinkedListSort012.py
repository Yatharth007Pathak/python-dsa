"""
Given a linked list where nodes can contain values 0s, 1s, and 2s only. The task is to segregate 0s, 1s, and 2s linked list 
such that all zeros segregate to the head side, 2s at the end of the linked list, and 1s in the middle of 0s and 2s.

Examples:

Input: LinkedList: 1->2->2->1->2->0->2->2
Output: 0->1->1->2->2->2->2->2
Explanation: All the 0s are segregated to the left end of the linked list, 2s to the right end of the list, and 1s in between.
 
Input: LinkedList: 2->2->0->1
Output: 0->1->2->2
Explanation: After arranging all the 0s,1s and 2s in the given format, the output will be 0 1 2 2.
"""

class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None

class Solution:
    # Function to sort a linked list of 0s, 1s, and 2s.
    def segregate(self, head):
        # Step 1: Count occurrences of 0s, 1s, and 2s
        count = [0, 0, 0]  # count[0] for 0s, count[1] for 1s, count[2] for 2s
        
        current = head
        while current:
            count[current.data] += 1
            current = current.next
        
        # Step 2: Update the linked list with sorted values based on counts
        current = head
        index = 0  # Start filling with 0s, then 1s, then 2s
        
        while current:
            # Skip to the next non-zero count
            while count[index] == 0:
                index += 1
            # Assign value and reduce the count
            current.data = index
            count[index] -= 1
            current = current.next
        
        return head

# Helper function to print the linked list
def printList(head):
    while head:
        print(head.data, end="->" if head.next else "\n")
        head = head.next

# Creating the linked list 1->2->2->1->2->0->2->2
head = Node(1)
head.next = Node(2)
head.next.next = Node(2)
head.next.next.next = Node(1)
head.next.next.next.next = Node(2)
head.next.next.next.next.next = Node(0)
head.next.next.next.next.next.next = Node(2)
head.next.next.next.next.next.next.next = Node(2)

solution = Solution()
sorted_head = solution.segregate(head)

# Print the segregated list
printList(sorted_head)  # Expected Output: 0->1->1->2->2->2->2->2

'''
Here's a breakdown of how the code sorts a linked list of 0s, 1s, and 2s using counting:

Class Node:
Defines the structure of a node in the linked list with data to store the value (0, 1, or 2) and next to point to the next node.

Class Solution and Method segregate:
The segregate method sorts the linked list by counting occurrences of each value and then modifying the list accordingly.

Counting Occurrences:
A list count = [0, 0, 0] is used to store the number of 0s, 1s, and 2s in the linked list.
The method iterates through the linked list, updating the count list based on the value of each node:
count[0] is incremented for each 0.
count[1] is incremented for each 1.
count[2] is incremented for each 2.

Updating the List Based on Counts:
The list is updated in-place with sorted values:
Starting with index = 0 (for 0s), the method fills each node’s data with the current index value.
It decrements the count for the current index and moves to the next node.
When count[index] becomes 0, it increments index to the next number (1 or 2) and continues filling nodes until all counts are exhausted.

Return Value:
The method returns the modified head of the linked list.

Helper Function printList:
This function prints each node’s data, connecting values with -> until the end of the list.

Example Execution:
Given linked list 1 -> 2 -> 2 -> 1 -> 2 -> 0 -> 2 -> 2, the method segregates the values in-place.
After segregation, the expected sorted output is 0 -> 1 -> 1 -> 2 -> 2 -> 2 -> 2 -> 2, which printList displays.
This approach uses constant space for counting and runs in linear time O(n) 
due to the two passes over the list (one for counting and another for updating values).
'''