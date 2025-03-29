"""
Given the head of a linked list and the number k, Your task is to find the kth node from the end. 
If k is more than the number of nodes, then the output should be -1.

Examples

Input: LinkedList: 1->2->3->4->5->6->7->8->9, k = 2
Output: 8
Explanation: The given linked list is 1->2->3->4->5->6->7->8->9. The 2nd node from end is 8.

Input: LinkedList: 10->5->100->5, k = 5
Output: -1
Explanation: The given linked list is 10->5->100->5. Since 'k' is more than the number of nodes, the output is -1.
"""

class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None

class Solution:
    # Function to find the data of kth node from the end of a linked list
    def getKthFromLast(self, head, k):
        # Initializing two pointers
        first = head
        second = head
        
        # Move the first pointer k nodes ahead
        for i in range(k):
            if first is None:  # if k is greater than the number of nodes
                return -1
            first = first.next
        
        # Move both pointers until the first pointer reaches the end
        while first:
            first = first.next
            second = second.next
        
        # The second pointer is now pointing at the kth node from the end
        return second.data if second else -1

# Creating a linked list 1 -> 2 -> 3 -> 4 -> 5 and setting k = 2
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# Solution instance
solution = Solution()
result = solution.getKthFromLast(head, 2)
print(result)  # Output should be 4

'''
Here's a detailed explanation of how this code finds the k-th node from the end of a linked list:

Class Node:
Defines a class Node to represent each node in a linked list.
The __init__ method takes an argument data (the value to be stored in the node) and initializes self.data to store this value.
self.next is set to None, which will later point to the next node in the linked list.

Class Solution and Method getKthFromLast:
Defines a class Solution containing the method getKthFromLast, which finds the k-th node from the end of the linked list.

Setting Up Two Pointers:
Inside getKthFromLast, two pointers first and second are initialized, both pointing to the head of the linked list.

Moving the First Pointer k Steps Ahead:
A for loop is used to move first forward by k nodes. This creates a gap of k nodes between first and second.
If first becomes None during this loop, it means k is greater than the number of nodes in the list. 
In this case, the function returns -1, as there is no k-th node from the end.

Advancing Both Pointers Until the End:
A while loop moves both first and second one node at a time until first reaches the end (None).
By the time first reaches the end, second points to the k-th node from the end.

Returning the Result:
If second points to a valid node, second.data is returned, which is the value of the k-th node from the end.
If second is None, -1 is returned, although in this setup, second should not be None as long as k is valid.

Example Usage:
The linked list 1 -> 2 -> 3 -> 4 -> 5 is created manually by linking nodes together.
solution.getKthFromLast(head, 2) is called, where head is the head of the list and k = 2.
Since the 2nd node from the end is 4, the function returns 4, which is printed as output.
'''