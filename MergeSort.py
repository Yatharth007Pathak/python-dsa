"""
Given an array arr[], its starting position l and its ending position r. Sort the array using the merge sort algorithm.

Examples:

Input: arr[] = [4, 1, 3, 9, 7]
Output: [1, 3, 4, 7, 9]

Input: arr[] = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""

class Solution:
    # Function to merge two halves arr[l...m] and arr[m+1...r]
    def merge(self, arr, l, m, r):
        # Create temp arrays to hold the two halves
        left = arr[l:m+1]
        right = arr[m+1:r+1]
        
        # Initialize pointers for left (i), right (j), and merged array (k)
        i, j, k = 0, 0, l
        
        # Merge the two halves into arr
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        # If there are remaining elements in left array, copy them
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        # If there are remaining elements in right array, copy them
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    # Recursive function to implement merge sort
    def mergeSort(self, arr, l, r):
        if l < r:
            # Find the middle point
            m = l + (r - l) // 2
            
            # Recursively sort first and second halves
            self.mergeSort(arr, l, m)
            self.mergeSort(arr, m + 1, r)
            
            # Merge the sorted halves
            self.merge(arr, l, m, r)

# Example Usage
sol = Solution()

# Test Case 1
arr1 = [4, 1, 3, 9, 7]
sol.mergeSort(arr1, 0, len(arr1) - 1)
print(arr1)  # Output: [1, 3, 4, 7, 9]

# Test Case 2
arr2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
sol.mergeSort(arr2, 0, len(arr2) - 1)
print(arr2)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

'''
Here's a breakdown of the code line by line:

class Solution:
The Solution class is defined to hold the functions for implementing the merge sort algorithm.

def merge(self, arr, l, m, r):
A function called merge is defined to merge two halves of an array arr. The parameters are:

arr: The array to merge.
l: The starting index of the left half.
m: The middle index, separating the two halves.
r: The ending index of the right half.
left = arr[l
+1]:
A temporary array left is created to hold the elements of the left half, which goes from index l to m (inclusive).

right = arr[m+1
+1]:
A temporary array right is created to hold the elements of the right half, which goes from index m+1 to r (inclusive).

i, j, k = 0, 0, l:
Three pointers are initialized:

i: Pointer for the left array, starts at 0.
j: Pointer for the right array, starts at 0.
k: Pointer for the original array arr, starts at l.
while i < len(left) and j < len(right):
A loop is initiated to merge the two halves as long as there are elements in both left and right.

if left[i] <= right[j]:
If the current element in left is smaller than or equal to the current element in right, 
the element from left is placed into the original array arr.

arr[k] = left[i]:
The current element from left is copied into arr.

i += 1:
The pointer i is incremented to move to the next element in the left array.

else:
If the current element in right is smaller than the element in left, the element from right is placed into arr.

arr[k] = right[j]:
The current element from right is copied into arr.

j += 1:
The pointer j is incremented to move to the next element in the right array.

k += 1:
The pointer k is incremented to move to the next position in arr.

while i < len(left):
After the main loop, this loop runs if there are any remaining elements in the left array.

arr[k] = left[i]:
The remaining elements from left are copied into arr.

i += 1:
The pointer i is incremented.

k += 1:
The pointer k is incremented.

while j < len(right):
This loop runs if there are any remaining elements in the right array.

arr[k] = right[j]:
The remaining elements from right are copied into arr.

j += 1:
The pointer j is incremented.

k += 1:
The pointer k is incremented.

def mergeSort(self, arr, l, r):
This is the main function to perform merge sort. It takes the array arr, the left index l, and the right index r as input.

if l < r:
The condition checks if there are more than one element in the portion of the array (i.e., when l is less than r).

m = l + (r - l) // 2:
The middle index m is calculated to divide the array into two halves.

self.mergeSort(arr, l, m):
The mergeSort function is called recursively to sort the left half of the array (from l to m).

self.mergeSort(arr, m + 1, r):
The mergeSort function is called recursively to sort the right half of the array (from m + 1 to r).

self.merge(arr, l, m, r):
Once both halves are sorted, the merge function is called to merge the two sorted halves.

Example Usage:

sol = Solution():
An instance of the Solution class is created.

arr1 = [4, 1, 3, 9, 7]:
A test array arr1 is initialized.

sol.mergeSort(arr1, 0, len(arr1) - 1):
The mergeSort function is called to sort arr1 from index 0 to the last index.

print(arr1):
The sorted array arr1 is printed, expected to be [1, 3, 4, 7, 9].

arr2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]:
Another test array arr2 is initialized.

sol.mergeSort(arr2, 0, len(arr2) - 1):
The mergeSort function is called to sort arr2 from index 0 to the last index.

print(arr2):
The sorted array arr2 is printed, expected to be [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
'''