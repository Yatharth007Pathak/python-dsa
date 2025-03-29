"""
Given an array arr[] containing non-negative integers, the task is to divide it into two sets set1 and set2 such that the 
absolute difference between their sums is minimum and find the minimum difference.

Examples:

Input: arr[] = [1, 6, 11, 5]
Output: 1
Explanation: Subset1 = {1, 5, 6}, sum of Subset1 = 12         Subset2 = {11}, sum of Subset2 = 11 
Hence, minimum difference is 1.  

Input: arr[] = [1, 4]
Output: 3
Explanation: Subset1 = {1}, sum of Subset1 = 1          Subset2 = {4}, sum of Subset2 = 4
Hence, minimum difference is 3.

Input: arr[] = [1]
Output: 1
Explanation: Subset1 = {1}, sum of Subset1 = 1           Subset2 = {}, sum of Subset2 = 0
Hence, minimum difference is 1.
"""

class Solution:
    def minDifference(self, arr):
        total_sum = sum(arr)
        n = len(arr)
        target = total_sum // 2

        # Step 1: Initialize DP array
        dp = [False] * (target + 1)
        dp[0] = True  # Subset sum of 0 is always possible

        # Step 2: Fill DP array
        for num in arr:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]

        # Step 3: Find the maximum subset sum <= total_sum / 2
        for s in range(target, -1, -1):
            if dp[s]:
                subset_sum = s
                break

        # Step 4: Compute and return the minimum difference
        return abs(total_sum - 2 * subset_sum)

# Example Usage
sol = Solution()
print(sol.minDifference([1, 6, 11, 5]))  # Output: 1
print(sol.minDifference([1, 4]))        # Output: 3
print(sol.minDifference([1]))           # Output: 1

'''
Here's a breakdown of the code, line by line:

class Solution:
Defines a class called Solution that contains the method minDifference.

def minDifference(self, arr):
Defines the method minDifference, which takes a list arr as input and returns 
the minimum difference between the sums of two subsets of the array.

total_sum = sum(arr)
Calculates the total sum of the elements in the input list arr.

n = len(arr)
Computes the number of elements in the list arr and stores it in n.

target = total_sum // 2
Defines target as half of the total_sum. This is the sum we aim to approach using one subset, 
because if we can achieve a subset sum close to half the total sum, the difference between the two subsets will be minimized.

dp = [False] * (target + 1)
Initializes a boolean array dp of size target + 1. dp[j] will indicate whether a 
subset sum of j is achievable using the elements in the array.

dp[0] = True
Sets dp[0] to True because a subset sum of 0 is always possible (by selecting no elements).

for num in arr:
Loops over each element num in the array arr.

for j in range(target, num - 1, -1):
For each num, it iterates backward from target down to num. This backward iteration ensures that the 
current num is only used once in the subset sum.

dp[j] = dp[j] or dp[j - num]
Updates dp[j] to True if either dp[j] is already True (indicating that the sum j is achievable without using num), 
or dp[j - num] is True (indicating that j - num is achievable, so j can be formed by adding num).

for s in range(target, -1, -1):
Starts from target and iterates backward down to 0 to find the largest achievable subset sum that is less than or equal to target.

if dp[s]:
Checks if dp[s] is True, meaning that a subset sum of s is achievable.

subset_sum = s
If dp[s] is True, it assigns subset_sum to s, which is the largest achievable subset sum that is less than or equal to target.

break
Once the largest achievable subset sum is found, the loop breaks.

return abs(total_sum - 2 * subset_sum)
The minimum difference between the two subset sums is given by the formula abs(total_sum - 2 * subset_sum). 
This is because if one subset has sum subset_sum, the other subset must have the sum total_sum - subset_sum. 
The absolute difference is returned.

sol = Solution()
Creates an instance of the Solution class.

print(sol.minDifference([1, 6, 11, 5])) # Output: 1
Calls the minDifference method with the array [1, 6, 11, 5]. The output is 1 because the closest subset sums are 11 and 12, 
and their difference is 1.

print(sol.minDifference([1, 4])) # Output: 3
Calls the method with the array [1, 4]. The output is 3 because the closest subset sums are 1 and 4, and their difference is 3.

print(sol.minDifference([1])) # Output: 1
Calls the method with the array [1]. The output is 1 because the only subset has sum 1, 
and the other subset has sum 0, so the difference is 1.
'''