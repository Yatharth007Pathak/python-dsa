"""
Given the head of a Singly Linked List and a value x, insert that value x at the end of the LinkedList and return the modified Linked List.

Examples :

Input: LinkedList: 1->2->3->4->5 , x = 6
Output: 1->2->3->4->5->6

Input: LinkedList: 5->4 , x = 1
Output: 5->4->1
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    # Function to insert a node at the end of the linked list.
    def insertAtEnd(self, head, x):
        new_node = Node(x)  # Create a new node with the given value x
        if head is None:
            # If the linked list is empty, the new node becomes the head
            return new_node
        
        # Traverse to the last node
        current = head
        while current.next:
            current = current.next
        
        # Link the last node to the new node
        current.next = new_node
        
        return head

# Create a linked list: 1 -> 2 -> 3 -> 4 -> 5
head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# Insert 6 at the end
solution = Solution()
head = solution.insertAtEnd(head, 6)

# Print the modified linked list: 1 -> 2 -> 3 -> 4 -> 5 -> 6
current = head
while current:
    print(current.data, end=" -> " if current.next else "")
    current = current.next

'''
Here's a line-by-line explanation of the code:

class Node:
Defines a class Node to represent a node in a singly linked list. Each node contains:
data: the value of the node.
next: a reference to the next node in the list.
def __init__(self, data):
Initializes a new node with the given data. By default, the next reference is set to None.

class Solution:
Defines a Solution class that contains methods for manipulating the linked list.

def insertAtEnd(self, head, x):
This method inserts a new node with value x at the end of the linked list. 
It takes the current head of the list and the new value x as parameters.

new_node = Node(x)
Creates a new node with the given value x.

if head is None:
Checks if the linked list is empty (i.e., head is None).

return new_node
If the list is empty, the new node becomes the head of the list.

current = head
Initializes a variable current to the head of the list. This will be used to traverse the list.

while current.next:
Loops until the last node in the list (i.e., the node where current.next is None).

current = current.next
Moves to the next node in the list.

current.next = new_node
Links the last node to the new node, effectively inserting it at the end of the list.

return head
Returns the modified head of the list (which remains the same unless the list was empty).

Example Usage
head = Node(1)
Creates the head of the linked list with the value 1.

head.next = Node(2)
Adds a node with value 2 after the head.

head.next.next = Node(3)
Adds a node with value 3 after the node with value 2.

head.next.next.next = Node(4)
Adds a node with value 4 after the node with value 3.

head.next.next.next.next = Node(5)
Adds a node with value 5 after the node with value 4.

solution = Solution()
Creates an instance of the Solution class.

head = solution.insertAtEnd(head, 6)
Inserts a new node with value 6 at the end of the linked list.

Printing the Linked List
current = head
Initializes current to the head of the list to begin printing.

while current:
Loops through the list until the end is reached (current becomes None).

print(current.data, end=" -> " if current.next else "")
Prints the value of the current node followed by -> if there is a next node, or nothing if it's the last node.

current = current.next
Moves to the next node in the list.


Here’s a line-by-line explanation of the code:

Class Definitions
class Node:
Defines a class Node to represent a node in a singly linked list. Each node contains:

data: the value of the node.
next: a reference to the next node in the list.
def __init__(self, data):
Initializes a new node with the given data. By default, the next reference is set to None.

Solution Class
class Solution:
Defines a Solution class that contains methods for manipulating the linked list.

def insertAtEnd(self, head, x):
This method inserts a new node with value x at the end of the linked list. 
It takes the current head of the list and the new value x as parameters.

new_node = Node(x)
Creates a new node with the given value x.

if head is None:
Checks if the linked list is empty (i.e., head is None).

return new_node
If the list is empty, the new node becomes the head of the list.

current = head
Initializes a variable current to the head of the list. This will be used to traverse the list.

while current.next:
Loops until the last node in the list (i.e., the node where current.next is None).

current = current.next
Moves to the next node in the list.

current.next = new_node
Links the last node to the new node, effectively inserting it at the end of the list.

return head
Returns the modified head of the list (which remains the same unless the list was empty).

Example Usage
head = Node(1)
Creates the head of the linked list with the value 1.

head.next = Node(2)
Adds a node with value 2 after the head.

head.next.next = Node(3)
Adds a node with value 3 after the node with value 2.

head.next.next.next = Node(4)
Adds a node with value 4 after the node with value 3.

head.next.next.next.next = Node(5)
Adds a node with value 5 after the node with value 4.

solution = Solution()
Creates an instance of the Solution class.

head = solution.insertAtEnd(head, 6)
Inserts a new node with value 6 at the end of the linked list.

Printing the Linked List
current = head
Initializes current to the head of the list to begin printing.

while current:
Loops through the list until the end is reached (current becomes None).

print(current.data, end=" -> " if current.next else "")
Prints the value of the current node followed by -> if there is a next node, or nothing if it's the last node.

current = current.next
Moves to the next node in the list.

Output
For the input linked list 1 -> 2 -> 3 -> 4 -> 5, after inserting 6 at the end, the output will be:
'''