"""
The task is to complete the insert() function which is used to implement Insertion Sort.

Examples:

Input: n = 5, arr[] = { 4, 1, 3, 9, 7}
Output: 1 3 4 7 9

Input: n = 10, arr[] = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1}
Output: 1 2 3 4 5 6 7 8 9 10

Insertion Sort
Concept: Builds the final sorted array one item at a time by picking each element and inserting 
it into its correct position within the already sorted portion of the list.
Pros: Efficient for small or nearly sorted datasets with an average time complexity of O(n²).
Cons: Slower for large datasets compared to advanced algorithms.
"""

class Solution:
    def insert(self, alist, index, n):
        # The element to be inserted
        key = alist[index]
        
        # Move elements of alist[0..index-1], that are greater than key,
        # to one position ahead of their current position
        j = index - 1
        while j >= 0 and alist[j] > key:
            alist[j + 1] = alist[j]
            j -= 1
        
        # Place the key at its correct position
        alist[j + 1] = key

    def insertionSort(self, alist, n):
        # Traverse through 1 to n (start from 1 because a single element is trivially sorted)
        for i in range(1, n):
            self.insert(alist, i, n)

# Example usage:
sol = Solution()

# Example 1:
arr1 = [4, 1, 3, 9, 7]
n1 = len(arr1)
sol.insertionSort(arr1, n1)
print(arr1)  # Output: [1, 3, 4, 7, 9]

# Example 2:
arr2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
n2 = len(arr2)
sol.insertionSort(arr2, n2)
print(arr2)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

'''
Here's a detailed breakdown of the Insertion Sort code:

class Solution:
Defines a class named Solution, which will contain sorting methods.

def insert(self, alist, index, n):
Defines a method insert within the Solution class. It takes alist (the list to be sorted), 
index (the index of the element to be inserted), and n (the size of the list).

# The element to be inserted
A comment explaining that the next line will extract the element to be inserted into the correct position.

key = alist[index]
Stores the element at index in the variable key.

# Move elements of alist[0..index-1], that are greater than key,
A comment indicating that the following code will shift elements that are greater than key to the right.

# to one position ahead of their current position
A continuation of the previous comment specifying that elements will be shifted to the right.

j = index - 1
Initializes j to index - 1. This variable is used to iterate through the elements that need to be compared and shifted.

while j >= 0 and alist[j] > key:
Starts a while loop that continues as long as j is non-negative and the element at alist[j] is greater than key.

alist[j + 1] = alist[j]
Moves the element alist[j] one position to the right.

j -= 1
Decreases j by 1 to check the next element in the previous position.

# Place the key at its correct position
A comment explaining that the next line will place key in its correct position.

alist[j + 1] = key
Places key in the correct position in the list.

def insertionSort(self, alist, n):
Defines the insertionSort method, which sorts the list alist with size n using insertion sort.

# Traverse through 1 to n (start from 1 because a single element is trivially sorted)
A comment explaining that the loop starts from index 1, as the element at index 0 is considered trivially sorted.

for i in range(1, n):
Starts a for loop that iterates from 1 to n - 1. Each iteration sorts the element at index i.

self.insert(alist, i, n)
Calls the insert method to place the element at index i in its correct position in the sorted part of the list.

# Example usage:
A comment introducing examples of how to use the insertionSort method.

sol = Solution()
Creates an instance of the Solution class named sol.

# Example 1:
A comment introducing the first example.

arr1 = [4, 1, 3, 9, 7]
Initializes arr1 with a sample list of integers.

n1 = len(arr1)
Sets n1 to the length of arr1.

sol.insertionSort(arr1, n1)
Calls the insertionSort method on sol to sort arr1.

print(arr1) # Output: [1, 3, 4, 7, 9]
Prints the sorted list arr1 after calling insertionSort.

# Example 2:
A comment introducing the second example.

arr2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
Initializes arr2 with another sample list of integers, this time in descending order.

n2 = len(arr2)
Sets n2 to the length of arr2.

sol.insertionSort(arr2, n2)
Calls the insertionSort method on sol to sort arr2.

print(arr2) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Prints the sorted list arr2 after calling insertionSort.
'''