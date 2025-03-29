"""
Given the head of a linked list, the task is to find the middle. For example, the middle of 1->2->3->4->5 is 3. 
If there are two middle nodes (even count), return the second middle. For example, middle of 1->2->3->4->5->6 is 4.
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def findMid(self, head):
        # Initialize two pointers, slow and fast
        slow = head
        fast = head
        
        # Traverse the list. Move 'slow' by one and 'fast' by two steps.
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        # 'slow' will now be at the middle
        return slow.data

# Example usage:
# Create linked list 1 -> 2 -> 3 -> 4 -> 5 -> 6
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
head.next.next.next.next.next = Node(6)

sol = Solution()
print(sol.findMid(head))  # Output: 4
