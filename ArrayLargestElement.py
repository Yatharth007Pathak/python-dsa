"""
Given an array arr[]. The task is to find the largest element and return it.

Examples:

Input: arr = [1, 8, 7, 56, 90]
Output: 90
Explanation: The largest element of the given array is 90.

Input: arr = [5, 5, 5, 5]
Output: 5
Explanation: The largest element of the given array is 5.

Input: arr = [10]
Output: 10
Explanation: There is only one element which is the largest.
"""

from typing import List

class Solution:
    def largest(self, arr: List[int]) -> int:
        # Return the largest element in the array using the built-in max() function
        return max(arr)

sol = Solution()

# Example 1
print(sol.largest([1, 8, 7, 56, 90]))  # Output: 90

# Example 2
print(sol.largest([5, 5, 5, 5]))  # Output: 5

# Example 3
print(sol.largest([10]))  # Output: 10

'''
Here's a breakdown of the code:

from typing import List
Imports the List type hint from the typing module to specify that the method expects a list of integers as an argument.

class Solution:
Declares the Solution class, which contains methods for solving various problems.

def largest(self, arr: List[int]) -> int:
Defines the largest method, which takes a list of integers (arr) and returns the largest element from the list. 
The return type is specified as int.

return max(arr)
Uses Python's built-in max() function to find and return the largest element in the list arr.
The max() function scans through the list and returns the highest value.

Example 1:
Input: [1, 8, 7, 56, 90]
Execution: The max() function returns 90 as the largest number.
Output: 90

Example 2:
Input: [5, 5, 5, 5]
Execution: Since all elements are the same, the largest number is 5.
Output: 5

Example 3:
Input: [10]
Execution: There's only one element in the list, so it is the largest.
Output: 10
'''