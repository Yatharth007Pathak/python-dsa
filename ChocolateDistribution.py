"""
Given an array A[ ] of positive integers of size N, where each value represents the number of chocolates in a packet. 
Each packet can have a variable number of chocolates. 
There are M students, the task is to distribute chocolate packets among M students such that :
1. Each student gets exactly one packet.
2. The difference between maximum number of chocolates given to a student and minimum number of chocolates given to a student is minimum.

Example 1:
Input:
N = 8, M = 5
A = {3, 4, 1, 9, 56, 7, 9, 12}
Output: 6
Explanation: The minimum difference between maximum chocolates and minimum chocolates is 9 - 3 = 6 
by choosing following M packets :{3, 4, 9, 7, 9}.

Example 2:
Input:
N = 7, M = 3
A = {7, 3, 2, 4, 9, 12, 56}
Output: 2
Explanation: The minimum difference between maximum chocolates and minimum chocolates is 4 - 2 = 2 by choosing following M packets :{3, 2, 4}.
"""

class Solution:
    def findMinDiff(self, A, N, M):
        # Edge case: If there are fewer packets than students, it's not possible to distribute
        if M > N:
            return -1
        
        # Sort the array or packets
        A.sort()
        
        # Initialize the minimum difference to a large number
        min_diff = float('inf')
        
        # Loop through the sorted array and find the minimum difference
        for i in range(N - M + 1):
            # Difference between the maximum and minimum in the current window of size M
            diff = A[i + M - 1] - A[i]
            if diff < min_diff:
                min_diff = diff
        
        return min_diff

# Example usage:
solution = Solution()
print(solution.findMinDiff([3, 4, 1, 9, 56, 7, 9, 12], 8, 5))  # Output: 6
print(solution.findMinDiff([7, 3, 2, 4, 9, 12, 56], 7, 3))   # Output: 2

'''
Code Breakdown-

class Solution:
Defines a class named Solution.

def findMinDiff(self, A, N, M):
Defines a method findMinDiff which takes three parameters:
A: a list of integers representing the packet sizes.
N: the total number of packets.
M: the number of students.

if M > N:
This checks if the number of students M is greater than the number of packets N. If true:

return -1: 
Returns -1 because it's not possible to distribute packets if there are more students than packets.

A.sort()
Sorts the list A in ascending order. 
Sorting is crucial for finding the smallest difference between the largest and smallest packets in any subset of size M.

min_diff = float('inf')
Initializes min_diff to a very large number (infinity) to ensure that any real difference found will be smaller.

for i in range(N - M + 1):
This loop iterates through the sorted array, considering every possible subset of size M. 
The loop runs from 0 to N - M, which ensures that we only consider valid subsets that have exactly M packets.

diff = A[i + M - 1] - A[i]
Calculates the difference between the largest and smallest packets in the current subset. 
The largest packet in the subset is A[i + M - 1] and the smallest is A[i].

if diff < min_diff:
If the calculated difference is smaller than the current min_diff, update min_diff to this new value.

return min_diff
After the loop, min_diff will hold the minimum difference found between the largest and smallest packets in any subset of size M. 
This value is returned as the result.

Example Usage:
Test Case 1: findMinDiff([3, 4, 1, 9, 56, 7, 9, 12], 8, 5)
Steps:
Sorting: [1, 3, 4, 7, 9, 9, 12, 56]
Subsets of size 5:
[1, 3, 4, 7, 9] → Difference: 9 - 1 = 8
[3, 4, 7, 9, 9] → Difference: 9 - 3 = 6
[4, 7, 9, 9, 12] → Difference: 12 - 4 = 8
[7, 9, 9, 12, 56] → Difference: 56 - 7 = 49
Minimum Difference: 6 (from subset [3, 4, 7, 9, 9])

Test Case 2: findMinDiff([7, 3, 2, 4, 9, 12, 56], 7, 3)
Steps:
Sorting: [2, 3, 4, 7, 9, 12, 56]
Subsets of size 3:
[2, 3, 4] → Difference: 4 - 2 = 2
[3, 4, 7] → Difference: 7 - 3 = 4
[4, 7, 9] → Difference: 9 - 4 = 5
[7, 9, 12] → Difference: 12 - 7 = 5
[9, 12, 56] → Difference: 56 - 9 = 47
Minimum Difference: 2 (from subset [2, 3, 4])
'''