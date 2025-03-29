"""
Given an array arr[] and an integer k where k is smaller than the size of the array, 
the task is to find the kth smallest element in the given array.

Follow up: Don't solve it using the inbuilt sort function.

Examples :

Input: arr[] = [7, 10, 4, 3, 20, 15], k = 3
Output:  7
Explanation: 3rd smallest element in the given array is 7.

Input: arr[] = [2, 3, 1, 20, 15], k = 4 
Output: 15
Explanation: 4th smallest element in the given array is 15.
"""

import random

class Solution:
    def partition(self, arr, low, high):
        # Choose a random pivot and move it to the end
        pivot_index = random.randint(low, high)
        arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

        pivot = arr[high]
        i = low - 1  # Index of smaller element

        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quickselect(self, arr, low, high, k):
        if low <= high:
            # Find the partitioning index
            pi = self.partition(arr, low, high)

            # If partitioning index is the k-th position, return the element
            if pi == k:
                return arr[pi]
            # If the k-th element is smaller than the partitioning index, recurse on the left
            elif pi > k:
                return self.quickselect(arr, low, pi - 1, k)
            # Else recurse on the right
            else:
                return self.quickselect(arr, pi + 1, high, k)
        
        return None

    def kthSmallest(self, arr, k):
        # Adjust k to 0-indexed value
        return self.quickselect(arr, 0, len(arr) - 1, k - 1)

# Example usage:
solution = Solution()
print(solution.kthSmallest([7, 10, 4, 3, 20, 15], 3))  # Output: 7
print(solution.kthSmallest([2, 3, 1, 20, 15], 4))      # Output: 15

'''
Let's break down this code line by line:

import random
This imports the random module, which will be used to select a random pivot for the partition function.

class Solution:
This defines a class named Solution which contains methods to find the k-th smallest element in an array using the Quickselect algorithm.

def partition(self, arr, low, high):
This defines the partition method, which is used to partition the array based on a pivot. It takes three parameters: 
the array arr, the lower index low, and the higher index high.

pivot_index = random.randint(low, high)
A random pivot index is selected between the low and high indices to ensure better performance in randomized Quickselect.

arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
The randomly chosen pivot element is swapped with the element at the high index to move the pivot to the end of the array.

pivot = arr[high]
The pivot variable is set to the value at the high index, which is now the chosen pivot.

i = low - 1
The variable i is initialized to one position before the low index. It will track the position where smaller elements should be placed.

for j in range(low, high):
This starts a loop that iterates over the array from the low index to the high - 1 index.

if arr[j] <= pivot:
This checks if the current element arr[j] is less than or equal to the pivot. If it is, the code inside the block will run.

i += 1
If the element is smaller or equal to the pivot, i is incremented, 
moving the position to the right where the next smaller element will be placed.

arr[i], arr[j] = arr[j], arr[i]
The current element arr[j] is swapped with the element at arr[i], ensuring that all smaller elements are placed to the left of the pivot.

arr[i + 1], arr[high] = arr[high], arr[i + 1]
After the loop, the pivot (currently at high) is swapped with the element at i + 1, placing the pivot in its correct position.

return i + 1
The function returns the index i + 1, which is the position of the pivot after partitioning.

def quickselect(self, arr, low, high, k):
This defines the quickselect method, which is a recursive function used to find the k-th smallest element in the array. 
It takes four parameters: the array arr, the lower index low, the higher index high, and the k-th element index k.

if low <= high:
This checks if the current range of the array is valid. If low is greater than high, the recursion ends.

pi = self.partition(arr, low, high)
This calls the partition method to partition the array and get the position of the pivot pi.

if pi == k:
If the pivot position pi is equal to k, it means the pivot is the k-th smallest element. The method returns arr[pi].

elif pi > k:
If the pivot position is greater than k, the method recursively calls quickselect on the left part of the array (from low to pi - 1).

else:
If the pivot position is less than k, the method recursively calls quickselect on the right part of the array (from pi + 1 to high).

return None
If the array is invalid (i.e., low > high), the method returns None.

def kthSmallest(self, arr, k):
This defines the kthSmallest method, which is a wrapper function that adjusts the k-th index to be zero-indexed. 
It calls the quickselect method.

return self.quickselect(arr, 0, len(arr) - 1, k - 1)
This calls quickselect with the entire array (from index 0 to len(arr) - 1) 
and passes k - 1 as the k-th index (since arrays are zero-indexed).

solution = Solution()
This creates an instance of the Solution class and stores it in the variable solution.

print(solution.kthSmallest([7, 10, 4, 3, 20, 15], 3))
This calls the kthSmallest method to find the 3rd smallest element in the array [7, 10, 4, 3, 20, 15]. The output is 7.

print(solution.kthSmallest([2, 3, 1, 20, 15], 4))
This calls the kthSmallest method to find the 4th smallest element in the array [2, 3, 1, 20, 15]. The output is 15.
'''