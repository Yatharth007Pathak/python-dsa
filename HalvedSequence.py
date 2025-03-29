"""
Given two values N and M. Give the value when N is halved M-1 times.

Example 1:
Input: N = 100, M = 4
Output: 12
Explaination: The sequence of numbers is 
100, 50, 25, 12.

Example 2:
Input: N = 10, M = 5
Output: 0
Explaination: The sequence is 10, 5, 2, 1 and 0.
"""

class Solution:
    def halveNTimes(self, N, M):
        # Halve N M-1 times
        for _ in range(M-1):
            N = N // 2
        return N

# Example usage:
solution = Solution()
print(solution.halveNTimes(100, 4))  # Output: 12
print(solution.halveNTimes(10, 5))   # Output: 0

'''
Here's a breakdown of how it works:

Define class Solution: A class named Solution is defined with a method halveNTimes to perform the halving operation on N.

Define halveNTimes method: The method halveNTimes(self, N, M) takes two input parameters:

N: The number that will be halved.
M: The total number of times to perform halving (i.e., M-1 iterations).
Halving process:

The method contains a loop that runs M-1 times.
In each iteration, the value of N is halved using integer division (N = N // 2). 
This ensures that the result remains an integer even when halving produces a fractional value.

Return final result: After halving N M-1 times, the final value of N is returned.


'''