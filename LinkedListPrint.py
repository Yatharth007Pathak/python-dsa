"""
Given a linked list. Print all the elements of the linked list separated by space followed.

Examples:

Input: LinkedList : 1 -> 2
Output: 1 2
Explanation: The linked list contains two elements 1 and 2.The elements are printed in a single line.

Input: Linked List : 49 -> 10 -> 30
Output: 49 10 30
Explanation: The linked list contains 3 elements 49, 10 and 30. The elements are printed in a single line.
"""

"""
A linked list is a linear data structure in which elements, called nodes, 
are stored in sequence but not in contiguous memory locations like arrays. Each node consists of two parts:
Data: The value stored in the node.
Pointer/Reference: A link to the next node in the sequence.

Types of Linked Lists
Singly Linked List: Each node contains a reference to the next node, and the last node points to null (or None in Python).
Doubly Linked List: Each node contains a reference to both the next and the previous node.
Circular Linked List: The last node points back to the first node instead of null, forming a circle.

Example (Singly Linked List):
[Data | Next] -> [Data | Next] -> [Data | Next] -> None

Key Operations:
Insert: Add a new node to the list.
Delete: Remove a node from the list.
Search: Find an element in the list.
Traversal: Visit each node in sequence.

Advantages:
Dynamic Size: Memory is allocated as needed, making it easier to grow and shrink than arrays.
Efficient Insert/Delete: Inserting or deleting elements at the beginning or middle is more efficient than in arrays, 
as no shifting of elements is required.

Disadvantages:
Access Time: Accessing elements by index is slower because you must traverse the list from the head.
Extra Memory: Requires extra memory for storing the pointers.
"""

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class Solution:
    # Function to display the elements of a linked list
    def display(self, head):
        current = head
        while current is not None:
            # Print current node's data, followed by a space (but avoid extra space at the end)
            print(current.data, end=" ")
            current = current.next


# Driver Code Starts
if __name__ == "__main__":
    t = int(input())  # number of test cases
    for _ in range(t):
        input_list = list(map(int, input().split()))  # reading input list of integers
        head = None
        tail = None

        # Building the linked list from input
        for x in input_list:
            if head is None:
                head = Node(x)
                tail = head
            else:
                tail.next = Node(x)
                tail = tail.next

        ob = Solution()
        ob.display(head)
        print()  # newline after printing the linked list



