"""
Given an array arr[] of integers, the task is to find the length of the Longest Strictly Increasing Subsequence (LIS).

A subsequence is considered strictly increasing if each element in the subsequence is strictly less than the next element.

Examples:

Input: arr[] = [5, 8, 3, 7, 9, 1]
Output: 3
Explanation: The longest strictly increasing subsequence could be [5, 7, 9], which has a length of 3.

Input: arr[] = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
Output: 6
Explanation: One of the possible longest strictly increasing subsequences is [0, 2, 6, 9, 13, 15], which has a length of 6.

Input: arr[] = [3, 10, 2, 1, 20]
Output: 3
Explanation: The longest strictly increasing subsequence could be [3, 10, 20], which has a length of 3.

Input: arr[] = [3, 2]
Output: 1
Explanation: Since there is no strictly increasing subsequence, the longest subsequence is any single element, thus the length is 1.
"""

import bisect

class Solution:
    def longestSubsequence(self, arr):
        # This will store the minimum possible tail values for increasing subsequences of different lengths
        tails = []
        
        for num in arr:
            # Use binary search to find the insertion point in tails
            index = bisect.bisect_left(tails, num)
            
            # If index is equal to the length of tails, it means num is greater than all elements in tails
            if index == len(tails):
                tails.append(num)
            else:
                # Otherwise, replace the element at the found index
                tails[index] = num
        
        # The length of tails array is the length of the longest increasing subsequence
        return len(tails)

# Example inputs
arr1 = [5, 8, 3, 7, 9, 1]
arr2 = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
arr3 = [3, 10, 2, 1, 20]
arr4 = [3, 2]

# Creating an instance of Solution
solution = Solution()

# Finding the length of the longest increasing subsequence
print(solution.longestSubsequence(arr1))  # Output: 3
print(solution.longestSubsequence(arr2))  # Output: 6
print(solution.longestSubsequence(arr3))  # Output: 3
print(solution.longestSubsequence(arr4))  # Output: 1

'''

Here's a line-by-line breakdown of the code:

Importing bisect:
import bisect imports the bisect module, which provides support for binary search operations in lists. 
This module will help efficiently find positions to insert elements in a sorted list.

Class Solution:
Defines a class called Solution, which contains methods for array-related problems.

Method longestSubsequence:
Defines a function called longestSubsequence that finds the length of the longest increasing subsequence (LIS) in a given array (arr).

Initializing tails Array:
tails = [] initializes an empty list called tails. This list will store the minimum possible tail values of increasing subsequences of 
different lengths. The length of this list at the end will give the LIS length.

Loop through Each Number in arr:
for num in arr: starts a loop to go through each number (num) in the array arr.

Finding Insertion Point Using Binary Search:
index = bisect.bisect_left(tails, num) uses binary search to find insertion point in tails where num would go to maintain an increasing order.
bisect_left finds the leftmost position in tails where num could be inserted without breaking the sorted order.

Inserting or Replacing in tails:
if index == len(tails): checks if index is equal to the current length of tails.
If true, it means num is greater than all elements in tails, so num can extend the increasing subsequence by being added to the end.
tails.append(num) appends num to tails.
else: If index is not equal to the length of tails, it means there is a larger or equal value already present at index.
tails[index] = num replaces the element at index in tails with num. This ensures tails always maintains the smallest possible values, 
which helps extend increasing subsequences more flexibly.

Returning the Result:
return len(tails) returns the length of tails, which represents the length of the longest increasing subsequence.

Example Arrays for Testing:
Defines several test cases (arr1, arr2, arr3, and arr4) with different sequences to test the function.

Creating an Instance of Solution:
solution = Solution() creates an instance of the Solution class to access its methods.

Finding and Printing the Length of the Longest Increasing Subsequence:
print(solution.longestSubsequence(arr1)) calls longestSubsequence with arr1 and prints the result, which is expected to be 3.
print(solution.longestSubsequence(arr2)) calls longestSubsequence with arr2 and prints the result, which is expected to be 6.
print(solution.longestSubsequence(arr3)) calls longestSubsequence with arr3 and prints the result, which is expected to be 3.
print(solution.longestSubsequence(arr4)) calls longestSubsequence with arr4 and prints the result, which is expected to be 1.
'''