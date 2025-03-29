"""
Given a singly linked list of integers. The task is to check if the given linked list is palindrome or not.

Examples:

Input: LinkedList: 1->2->1->1->2->1
Output: true
Explanation: The given linked list is 1->2->1->1->2->1 , which is a palindrome and Hence, the output is true.

Input: LinkedList: 1->2->3->4
Output: false
Explanation: The given linked list is 1->2->3->4, which is not a palindrome and Hence, the output is false.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def isPalindrome(self, head):
        # Step 1: Find the middle of the linked list
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the linked list
        prev = None
        while slow:
            next_node = slow.next
            slow.next = prev
            prev = slow
            slow = next_node
        
        # Step 3: Check if the first half and the reversed second half are the same
        left, right = head, prev
        while right:  # Only need to check till right half
            if left.data != right.data:
                return False
            left = left.next
            right = right.next
        
        return True

# Helper function to print the linked list
def printList(head):
    while head:
        print(head.data, end="->" if head.next else "\n")
        head = head.next

# Creating the linked list 1->2->1->1->2->1
head = Node(1)
head.next = Node(2)
head.next.next = Node(1)
head.next.next.next = Node(1)
head.next.next.next.next = Node(2)
head.next.next.next.next.next = Node(1)

solution = Solution()
print(solution.isPalindrome(head))  # Expected Output: True

# Creating the linked list 1->2->3->4
head2 = Node(1)
head2.next = Node(2)
head2.next.next = Node(3)
head2.next.next.next = Node(4)

print(solution.isPalindrome(head2))  # Expected Output: False

'''
Here's how the isPalindrome method works to determine if a linked list is a palindrome:

Finding the Middle of the Linked List:
The slow and fast pointers are used to locate the middle of the list.
slow moves one step at a time, while fast moves two steps.
When fast reaches the end, slow is at the middle.

Reversing the Second Half:
Starting from slow, the second half of the list is reversed using a simple iterative approach:
Each node's next pointer is redirected to the previous node, creating a reversed linked list from the middle onward.
prev eventually points to the head of this reversed second half.

Comparing Both Halves:
Two pointers, left (starting from the head) and right (starting from prev), 
are used to compare each node in the first half with the corresponding node in the reversed second half.
If all corresponding nodes match, the list is a palindrome. If any values differ, it returns False.

Return Result:
The method returns True if all nodes match, meaning the linked list is a palindrome.

Example Usage:
Palindrome Case (1 -> 2 -> 1 -> 1 -> 2 -> 1):
Expected Output: True

Non-Palindrome Case (1 -> 2 -> 3 -> 4):
Expected Output: False

Complexity:
Time Complexity: O(n) due to traversing the list twice — once to find the middle and reverse, and once to compare.
Space Complexity:O(1) as the algorithm modifies the list in place (reversing the second half) without additional storage.

This approach is efficient for checking palindromes in a singly linked list, leveraging two-pointer techniques and in-place reversal.
'''