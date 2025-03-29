"""
Given a positive integer N, find if it can be expressed as x^y where y > 1 and x > 0 and x and y both are both integers.

Example 1:
Input: N = 8
Output: 1
Explanation: 8 can be expressed as 2^3.
"""

import math

class Solution:
    def checkPower(self, N):
        # If N is 1, it can be written as x^y (1^any power is 1)
        if N == 1:
            return 1
        
        # Iterate over possible values of y starting from 2
        for y in range(2, int(math.log(N, 2)) + 1):
            # Find the y-th root of N
            x = round(N ** (1.0 / y))
            # Check if x^y is equal to N
            if x ** y == N:
                return 1
        
        return 0

# Example usage:
solution = Solution()
print(solution.checkPower(8))  # Output: 1 (since 8 = 2^3)
print(solution.checkPower(10))  # Output: 0 (since 10 cannot be written as x^y for integers x and y)

'''
Here's a breakdown of how the code works:

Import math module: The math module is imported for using math.log(), which helps determine the upper limit of possible values for y.

Define class Solution: A class named Solution is defined, which contains the method checkPower to check if N can be expressed as x^y

Define checkPower method: The method checkPower(self, N) takes N as input, which is the number to be checked.

Check if N is 1: Since 1^y = 1 for any value of y, if N == 1, the method immediately returns 1, indicating that N can be written as x^y

Iterate over possible values of y:
The loop iterates over possible values of y starting from 2 up to log(N) (base 2). This is because if N can be written as x^y,
the value of y can't be larger than log(N) (base 2) (since 2^y grows exponentially).

The function int(math.log(N, 2)) + 1 determines the upper bound for y. For example, for N = 8, log2(8) equals 3.

Calculate the y-th root of N:
For each value of y, the y-th root of N is calculated as N ^ 1/y and x is rounded to the nearest integer.

Check if x^y equals N:
The code checks if x^y = N. If this condition holds, N can be written as x^y and the method returns 1.

Return 0 if no solution is found:
If no values of x and y satisfy x^y = N by the end of the loop, the method returns 0, indicating that N cannot be written as x^y

Example usage:
Example 1 (N = 8): The method checks if 8 can be written as x^y. Since 8 = 2^3, the method returns 1.

Example 2 (N = 10): The method checks if 10 can be written as x^y. Since no integer values of x and y satisfy x^y = 10, the method returns 0.
'''