"""
Given two linked lists (L1 & L2), your task is to complete the function makeUnion(), which returns the union list of two linked lists. 
This union list should include all the distinct elements only and it should be sorted in ascending order.

Examples:

Input: L1 = 9->6->4->2->3->8, L2 = 1->2->8->6->2
Output: 1 -> 2 -> 3 -> 4 -> 6 -> 8 -> 9
Explanation: All the distinct numbers from two lists, when sorted form the list in the output. 

Input: L1 = 1->5->1->2->2->5, L2 = 4->5->6->7->1
Output: 1 -> 2 -> 4 -> 5 -> 6 -> 7
Explaination: All the distinct numbers from two lists, when sorted forms the list in the output.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def union(self, head1, head2):
        # Step 1: Use a set to store unique elements from both linked lists
        elements = set()
        
        # Traverse the first linked list and add elements to the set
        current = head1
        while current:
            elements.add(current.data)
            current = current.next
        
        # Traverse the second linked list and add elements to the set
        current = head2
        while current:
            elements.add(current.data)
            current = current.next
        
        # Step 2: Sort the elements
        sorted_elements = sorted(elements)
        
        # Step 3: Create a new linked list from the sorted unique elements
        union_head = Node(sorted_elements[0]) if sorted_elements else None
        current = union_head
        for value in sorted_elements[1:]:
            current.next = Node(value)
            current = current.next
        
        return union_head

# Helper function to print the linked list
def printList(head):
    while head:
        print(head.data, end=" -> " if head.next else "\n")
        head = head.next

# Creating linked lists L1: 9->6->4->2->3->8 and L2: 1->2->8->6->2
L1 = Node(9)
L1.next = Node(6)
L1.next.next = Node(4)
L1.next.next.next = Node(2)
L1.next.next.next.next = Node(3)
L1.next.next.next.next.next = Node(8)

L2 = Node(1)
L2.next = Node(2)
L2.next.next = Node(8)
L2.next.next.next = Node(6)
L2.next.next.next.next = Node(2)

solution = Solution()
union_head = solution.union(L1, L2)
printList(union_head)  # Expected Output: 1 -> 2 -> 3 -> 4 -> 6 -> 8 -> 9

'''

Here's a breakdown of how the union function works:

Collecting Unique Elements:
A set, elements, is used to store the unique elements from both linked lists. The set automatically handles duplicates, 
so we don't need to worry about repeated values between the two lists.
The function traverses each linked list (head1 and head2), adding each node's data to the set.

Sorting the Elements:
After collecting all unique elements, they are sorted in ascending order using Python's built-in sorted() function.

Creating a New Linked List:
A new linked list is constructed from the sorted list of unique elements.
The first element is used to create the head of the new linked list, and subsequent elements are added one by one.

Example:
Given:
L1: 9 -> 6 -> 4 -> 2 -> 3 -> 8
L2: 1 -> 2 -> 8 -> 6 -> 2

The unique elements are:
9, 6, 4, 2, 3, 8 from L1
1, 2, 8, 6, 2 from L2

Union of these two sets, sorted: 1, 2, 3, 4, 6, 8, 9
The resulting linked list will be: 1 -> 2 -> 3 -> 4 -> 6 -> 8 -> 9.

Output:
Expected Output: 1 -> 2 -> 3 -> 4 -> 6 -> 8 -> 9

Complexity:
Time Complexity: Traversing both linked lists is O(n+m), where n and m are the lengths of the two linked lists.
Sorting the elements is O(klogk), where k is the number of unique elements.
Creating the new linked list takes O(k).
So, the overall time complexity is O(n+m+klogk).

Space Complexity: We use a set to store the unique elements, so the space complexity is O(k), where k is the number of unique elements.
This approach efficiently handles finding the union and creating the result in a sorted linked list.
'''