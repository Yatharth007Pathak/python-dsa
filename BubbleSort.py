"""
Given an Integer n and a list arr. Sort the array using bubble sort algorithm.

Examples :

Input: n = 5, arr[] = {4, 1, 3, 9, 7}
Output: 1 3 4 7 9

Input: n = 10, arr[] = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1}
Output: 1 2 3 4 5 6 7 8 9 10

Bubble Sort 
Concept: Repeatedly steps through the list, compares adjacent items, and swaps them if they're in the wrong order. 
Each pass “bubbles” the largest unsorted element to its correct position.
Pros: Simple and intuitive.
Cons: Inefficient for large datasets with O(n²) time complexity.
"""

class Solution:
    def bubbleSort(self, arr, n):
        # Traverse through all array elements
        for i in range(n):
            # Flag to check if any swapping happened in this pass
            swapped = False
            
            # Last i elements are already in place
            for j in range(0, n - i - 1):
                # Traverse the array from 0 to n-i-1
                # Swap if the element found is greater than the next element
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    swapped = True
            
            # If no two elements were swapped by inner loop, then the array is sorted
            if not swapped:
                break

# Example usage:
sol = Solution()

# Input: n = 5, arr[] = {4, 1, 3, 9, 7}
arr = [4, 1, 3, 9, 7]
n = len(arr)
sol.bubbleSort(arr, n)
print(arr)  # Output: [1, 3, 4, 7, 9]

# Input: n = 10, arr[] = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1}
arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
n = len(arr)
sol.bubbleSort(arr, n)
print(arr)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

'''
Here's a breakdown of each line of the code:

class Solution:
Defines a class named Solution. Classes in Python are used to bundle data and functionality together.

def bubbleSort(self, arr, n):
Defines a method bubbleSort within the Solution class. It takes two parameters: 
arr (the array to be sorted) and n (the number of elements in the array).

# Traverse through all array elements
A comment indicating that the next loop will iterate through all elements of the array.

for i in range(n):
Starts a for loop that iterates n times. Each iteration represents one pass of the bubble sort algorithm.

# Flag to check if any swapping happened in this pass
A comment explaining that the swapped flag will track whether any elements were swapped during this pass.

swapped = False
Initializes a boolean variable swapped to False. This flag will be set to True if any elements are swapped in the current pass.

# Last i elements are already in place
A comment explaining that the last i elements of the array are already sorted after i passes.

for j in range(0, n - i - 1):
Starts an inner for loop to iterate through the array from the beginning up to the unsorted portion (n - i - 1). 
Each iteration compares adjacent elements.

# Traverse the array from 0 to n-i-1
A comment indicating that the loop traverses the array from the beginning up to n-i-1.

# Swap if the element found is greater than the next element
A comment explaining that the next line of code will swap elements if the current element is greater than the next one.

if arr[j] > arr[j + 1]:
Checks if the current element (arr[j]) is greater than the next element (arr[j + 1]).

arr[j], arr[j + 1] = arr[j + 1], arr[j]
Swaps the elements at positions j and j + 1 if the condition is true.

swapped = True
Sets the swapped flag to True, indicating that a swap has occurred.

# If no two elements were swapped by inner loop, then the array is sorted
A comment explaining that if no elements were swapped in a pass, the array is already sorted.

if not swapped:
Checks if the swapped flag is False. If no elements were swapped during the pass, the array is sorted.

break
Exits the outer loop early if the array is already sorted, optimizing performance.

# Example usage:
A comment indicating the beginning of example usage of the bubbleSort method.

sol = Solution()
Creates an instance of the Solution class named sol.

# Input: n = 5, arr[] = {4, 1, 3, 9, 7}
A comment indicating the first example input array and its size.

arr = [4, 1, 3, 9, 7]
Initializes the array arr with the example values.

n = len(arr)
Sets n to the length of the array, which is 5 in this case.

sol.bubbleSort(arr, n)
Calls the bubbleSort method on the sol instance, passing the array arr and its size n for sorting.

print(arr) # Output: [1, 3, 4, 7, 9]
Prints the sorted array after the bubbleSort method has been executed.

# Input: n = 10, arr[] = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1}
A comment indicating the second example input array and its size.

arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
Initializes the array arr with the example values in descending order.

n = len(arr)
Sets n to the length of the array, which is 10 in this case.

sol.bubbleSort(arr, n)
Calls the bubbleSort method on the sol instance, passing the array arr and its size n for sorting.

print(arr) # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Prints the sorted array after the bubbleSort method has been executed.
'''