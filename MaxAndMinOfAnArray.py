"""
Given an array arr. Your task is to find the minimum and maximum elements in the array.

Note: Return an array that contains two elements the first one will be a minimum element and the second will be a maximum of an array.

Examples:

Input: arr = [3, 2, 1, 56, 10000, 167]
Output: 1 10000
Explanation: minimum and maximum elements of array are 1 and 10000.

Input: arr = [1, 345, 234, 21, 56789]
Output: 1 56789
Explanation: minimum and maximum element of array are 1 and 56789.

Input: arr = [56789]
Output: 56789 56789
Explanation: Since the array contains only one element so both min & max are same.
"""

class Solution:
    def get_min_max(self, arr):
        # Check if the array is not empty
        if not arr:
            return None  # Return None if array is empty
        
        # Initialize min and max values
        min_val = min(arr)
        max_val = max(arr)
        
        # Return them as a list
        return [min_val, max_val]

sol = Solution()
print(sol.get_min_max([3, 2, 1, 56, 10000, 167]))  # Output: [1, 10000]
print(sol.get_min_max([1, 345, 234, 21, 56789]))   # Output: [1, 56789]
print(sol.get_min_max([56789]))                    # Output: [56789, 56789]

'''
Here's a line-by-line breakdown of the get_min_max function:

Define the Solution class: This class contains the get_min_max method, which returns the minimum and maximum values in an array.

Define the get_min_max method: This method accepts an array arr as input.

Check if the array is empty:
if not arr: checks if arr is empty. If so, return None to indicate that there is no minimum or maximum in an empty array.

Initialize min_val and max_val:
min_val = min(arr) finds the smallest element in arr.
max_val = max(arr) finds the largest element in arr.

Return the result as a list:
return [min_val, max_val] returns a list containing the minimum and maximum values.
Example Usage and Output

Test Case 1:
Input: [3, 2, 1, 56, 10000, 167]
Output: [1, 10000]
Explanation: The smallest element is 1, and the largest is 10000.

Test Case 2:
Input: [1, 345, 234, 21, 56789]
Output: [1, 56789]
Explanation: The smallest element is 1, and the largest is 56789.

Test Case 3:
Input: [56789]
Output: [56789, 56789]
Explanation: With only one element in the array, it is both the minimum and maximum.
'''