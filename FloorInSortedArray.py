"""
Given a sorted array arr[] of size n without duplicates, and given a value x. 
Floor of x is defined as the largest element k in arr[] such that k is smaller than or equal to x. Find the index of k(0-based indexing).

Examples

Input: n = 7, x = 0 arr[] = {1,2,8,10,11,12,19}
Output: -1
Explanation: No element less than 0 is found. So output is "-1".

Input: n = 7, x = 5 arr[] = {1,2,8,10,11,12,19}
Output: 1
Explanation: Largest Number less than 5 is 2 (i.e k = 2), whose index is 1(0-based indexing).
"""

class Solution:
    
    def findFloor(self, A, N, X):
        # Initialize variables
        low, high = 0, N - 1
        floor_index = -1
        
        # Binary search to find the floor of X
        while low <= high:
            mid = (low + high) // 2
            
            # If the element at mid is less than or equal to X, it can be a potential floor
            if A[mid] <= X:
                floor_index = mid  # update the floor index
                low = mid + 1      # search in the right half to find a larger valid floor
            else:
                high = mid - 1     # search in the left half if the current element is greater than X
        
        return floor_index

# Example usage:
sol = Solution()
arr1 = [1, 2, 8, 10, 11, 12, 19]
x1 = 0
x2 = 5

print(sol.findFloor(arr1, len(arr1), x1))  # Output: -1
print(sol.findFloor(arr1, len(arr1), x2))  # Output: 1

'''
This method efficiently finds the floor of a given number X in a sorted array A using binary search. 
The floor is the largest element in the array that is less than or equal to X. If no such element exists, it returns -1.


Code Breakdown

class Solution:
Defines the Solution class, which contains the method findFloor.

def findFloor(self, A, N, X):
Defines the method findFloor. It takes the sorted array A, the size of the array N, and the number X whose floor is to be found.

low, high = 0, N - 1
Initializes two pointers: low starts at the beginning of the array (0), and high starts at the last index of the array (N - 1).

floor_index = -1
Initializes floor_index to -1. This will store the index of the largest element less than or equal to X. 
If no such element exists, it remains -1.

while low <= high:
The binary search loop continues as long as the low pointer does not cross the high pointer.

mid = (low + high) // 2
Calculates the middle index mid of the current search range.

if A[mid] <= X:
If the element at index mid is less than or equal to X, then this element can be a potential floor of X.

floor_index = mid
Updates floor_index to mid, since the current element is less than or equal to X.

low = mid + 1
Shifts the low pointer to mid + 1 to search in the right half of the array for a larger valid floor.

else:
If the element at mid is greater than X, it cannot be the floor, so:

high = mid - 1
Shifts the high pointer to mid - 1 to search in the left half of the array.

return floor_index
After the loop, returns the floor_index. 
If a floor was found, floor_index contains the index of the largest element less than or equal to X. Otherwise, it remains -1.

sol = Solution()
Creates an instance of the Solution class.

arr1 = [1, 2, 8, 10, 11, 12, 19]
Defines a sorted array arr1.

x1 = 0 and x2 = 5
Two test cases are defined: x1 = 0 (to check for a value smaller than all array elements) and x2 = 5 (to find the floor of 5).

print(sol.findFloor(arr1, len(arr1), x1)) # Output: -1
Since x1 = 0 is smaller than the smallest element in the array, the output is -1, indicating no floor exists.

print(sol.findFloor(arr1, len(arr1), x2)) # Output: 1
For x2 = 5, the floor is 2, which is at index 1. Hence, the output is 1.
'''