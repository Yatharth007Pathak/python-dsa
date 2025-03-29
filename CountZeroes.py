"""
Given an array arr of only 0's and 1's. The array is sorted in such a manner that all the 1's are placed first 
and then they are followed by all the 0's. Find the count of all the 0's.

Examples:

Input: arr[] = [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0]
Output: 3
Explanation: There are 3 0's in the given array.

Input: arr[] = [0, 0, 0, 0, 0]
Output: 5
Explanation: There are 5 0's in the array.
"""

class Solution:
    def countZeroes(self, arr):
        # Initialize start and end for binary search
        start, end = 0, len(arr) - 1
        
        # Variable to store the index of the first occurrence of 0
        first_zero_index = -1
        
        # Perform binary search to find the first occurrence of 0
        while start <= end:
            mid = (start + end) // 2
            # If we found a 0, check if it's the first one
            if arr[mid] == 0:
                first_zero_index = mid
                end = mid - 1  # Move left to find the first zero
            else:
                start = mid + 1  # Move right to skip the 1's

        # If no zeros are found, return 0
        if first_zero_index == -1:
            return 0
        
        # The number of zeros is the length of the array minus the index of the first 0
        return len(arr) - first_zero_index

# Example usage
sol = Solution()
print(sol.countZeroes([1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0]))  # Output: 3
print(sol.countZeroes([0, 0, 0, 0, 0]))  # Output: 5


'''
The countZeroes method uses binary search to efficiently find the first occurrence of 0 in a sorted binary array (with 1s followed by 0s). 
It then calculates the total number of zeros by subtracting the index of the first zero from the length of the array. 
If no zeros are found, the method returns 0


Code Breakdown

class Solution:
Defines a class Solution that encapsulates the method countZeroes.

def countZeroes(self, arr):
This defines the method countZeroes, which takes a list arr as input and returns the count of zeros in the list.

start, end = 0, len(arr) - 1
Initializes two variables start and end for binary search:
start: points to the beginning of the array (0).
end: points to the last element of the array (len(arr) - 1).

first_zero_index = -1
Initializes a variable first_zero_index to store the index of the first occurrence of 0. If no zeros are found, it will remain -1.

while start <= end:
A while loop that performs a binary search as long as start is less than or equal to end.

mid = (start + end) // 2
Calculates the middle index mid of the current subarray being searched.

if arr[mid] == 0:
Checks if the middle element is 0.
If it is 0, it means we need to check if this is the first occurrence of 0.

first_zero_index = mid
Updates first_zero_index to store the index of the current 0.

end = mid - 1
Moves the end pointer to the left (mid - 1) to continue searching for the first occurrence of 0 on the left side of the array.

else:
If the middle element is 1, it means we haven't encountered any 0s yet, so:

start = mid + 1
Moves the start pointer to the right (mid + 1) to search the right half of the array for zeros.

if first_zero_index == -1:
After the loop, if first_zero_index is still -1, it means no zeros were found in the array.

return 0
If no zeros are found, the function returns 0.

return len(arr) - first_zero_index
If zeros were found, the function returns the number of zeros, which is the total length of the array minus the index of the first zero (len(arr) - first_zero_index).

sol = Solution()
Creates an instance of the Solution class.

print(sol.countZeroes([1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0])) # Output: 3
Calls the countZeroes method with the array [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0].
The output is 3 because the first 0 appears at index 9, and there are 3 zeros in total (12 - 9 = 3).

print(sol.countZeroes([0, 0, 0, 0, 0])) # Output: 5
Calls the countZeroes method with the array [0, 0, 0, 0, 0].
The output is 5 because the first 0 appears at index 0, and there are 5 zeros in total (5 - 0 = 5).
'''