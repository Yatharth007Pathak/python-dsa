"""
Given an array of positive integers arr[]. Find the maximum sum subsequence of the given array such that the integers 
in the subsequence are sorted in strictly increasing order i.e. a strictly increasing subsequence. 

Examples:

Input: arr[] = [1, 101, 2, 3, 100]
Output: 106
Explanation: The maximum sum of a increasing sequence is obtained from [1, 2, 3, 100].

Input: arr[] = [4, 1, 2, 3]
Output: 6
Explanation: The maximum sum of a increasing sequence is obtained from {1, 2, 3}.
"""

class Solution:
    def maxSumIS(self, arr):
        n = len(arr)
        
        # Step 1: Initialize dp array where dp[i] represents the maximum sum  of increasing subsequence ending at index i
        dp = arr[:]  # Start with each element itself as the subsequence
        
        # Step 2: Build dp array
        for i in range(1, n):
            for j in range(i):
                if arr[j] < arr[i]:  # Check if it forms an increasing subsequence
                    dp[i] = max(dp[i], dp[j] + arr[i])
        
        # Step 3: The result is the maximum value in the dp array
        return max(dp)

# Example Usage
solution = Solution()
print(solution.maxSumIS([1, 101, 2, 3, 100]))  # Output: 106
print(solution.maxSumIS([4, 1, 2, 3]))         # Output: 6
print(solution.maxSumIS([10, 5, 4]))           # Output: 10

'''
Here's a line-by-line explanation of the code:

class Solution:
Declares a class named Solution. It will contain the method to calculate the maximum sum of an increasing subsequence.

def maxSumIS(self, arr):
Defines a method maxSumIS that takes a list of integers arr as input and calculates the maximum sum of an increasing subsequence.

n = len(arr)
Stores the length of the array arr in the variable n.

dp = arr[:]
Initializes the dp array as a copy of arr. The dp[i] value represents the maximum sum of an increasing subsequence ending at index i. 
Initially, each element itself is considered as its own subsequence.

for i in range(1, n):
Starts an outer loop iterating through indices from 1 to n-1. 
This loop processes each element in the array to determine its contribution to an increasing subsequence.

for j in range(i):
Starts an inner loop iterating through all previous indices from 0 to i-1. 
This loop checks if any element before i can contribute to an increasing subsequence ending at i.

if arr[j] < arr[i]:
Checks if the element at index j is less than the element at index i. This condition ensures that the subsequence remains increasing.

dp[i] = max(dp[i], dp[j] + arr[i])
Updates dp[i] with the maximum of its current value and the sum of dp[j] + arr[i]. 
This adds the current element arr[i] to the sum of the increasing subsequence ending at j.

return max(dp)
After processing all elements, returns the maximum value in the dp array. 
This value is the maximum sum of an increasing subsequence in the array.

Example Usage:

Example 1:
Input: arr = [1, 101, 2, 3, 100]
The increasing subsequence [1, 2, 3, 100] has the maximum sum 106.

Example 2:
Input: arr = [4, 1, 2, 3]
The increasing subsequence [1, 2, 3] has the maximum sum 6.

Example 3:
Input: arr = [10, 5, 4]
No increasing subsequence can be formed except the individual elements themselves. The maximum sum is the largest element, 10.
'''