"""
Given a positive integer n, find the nth fibonacci number. Since the answer can be very large, return the answer modulo 1000000007.

Note: for the reference of this question take first fibonacci number to be 1.

Example:
Input: n = 2
Output: 1 
Explanation: 1 is the 2nd number of fibonacci series.
"""

MOD = 1000000007

class Solution:
    def nthFibonacci(self, n: int) -> int:
        if n == 1:
            return 1
        
        a, b = 1, 1
        for _ in range(2, n):
            a, b = b, (a + b) % MOD
        
        return b

# Example usage:
n = 7
solution = Solution()
print(solution.nthFibonacci(n))  # Output: 13

'''

Here's a breakdown of the code:

MOD = 1000000007
Defines a constant MOD with the value 1000000007. This is a large prime number used to prevent integer overflow by taking results modulo MOD.

class Solution:
Defines a class named Solution. This class contains methods to solve specific problems.

def nthFibonacci(self, n: int) -> int:
Defines a method named nthFibonacci within the Solution class. 
This method takes an integer n and returns the nth Fibonacci number modulo MOD.

if n == 1:
Checks if n is 1. This is a base case because the first Fibonacci number is 1.

return 1
Returns 1 if n is 1.

a, b = 1, 1
Initializes two variables a and b to 1. These represent the first two Fibonacci numbers.

for _ in range(2, n):
Starts a loop that iterates from 2 to n - 1. This loop calculates Fibonacci numbers iteratively, 
skipping the first two numbers as they are already initialized.

a, b = b, (a + b) % MOD
Updates a and b for each iteration:
a is assigned the value of b (the previous Fibonacci number).
b is updated to (a + b) % MOD (the current Fibonacci number modulo MOD).
The % operator calculates the remainder. 
When used in the context of modular arithmetic, it ensures that the result remains within a certain range, specifically from 0 to MOD-1.

return b
After completing the loop, returns b, which holds the value of the nth Fibonacci number modulo MOD.

n = 7
Defines n as 7, the position of the Fibonacci number to compute.

solution = Solution()
Creates an instance of the Solution class.

print(solution.nthFibonacci(n)) # Output: 13
Calls the nthFibonacci method with n = 7. The method calculates the 7th Fibonacci number and prints 13.
'''