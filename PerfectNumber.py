"""
Given a number N. Check if it is perfect or not. A number is perfect if sum of factorial of its digit is equal to the given number.

Examples:

Input: N = 23
Output: 0
Explanation: The sum of factorials of digits of 23 is 2! + 3! = 2 + 6 = 8 which is not equal to 23. Thus, answer is 0.

Example 2:
Input: N = 145
Output: 1
Explanation: The sum of factorials of digits of 145 is 1! + 4! + 5! = 1 + 24 + 120 = 145 which is equal to 145.Thus, answer is 1.
"""

class Solution:
    def isPerfect(self, N):
        from math import factorial

        # Calculate the sum of the factorials of the digits of N
        digit_factorial_sum = sum(factorial(int(digit)) for digit in str(N))

        # Check if the sum of the factorials equals the number
        return 1 if digit_factorial_sum == N else 0

# Examples
solution = Solution()
print(solution.isPerfect(23))  # Output: 0
print(solution.isPerfect(145))  # Output: 1

'''
Here's a line-by-line explanation:

class Solution:
Defines a class named Solution to group the function that checks if a number is "perfect."

def isPerfect(self, N):
Declares a method isPerfect inside the class. This method takes two parameters: 
self (refers to the class instance) and N (the input number to check).

from math import factorial
Imports the factorial function from Python's math module to calculate the factorial of digits.

digit_factorial_sum = sum(factorial(int(digit)) for digit in str(N))
Converts the number N into a string, iterates over its digits, converts each digit back to an integer, 
calculates its factorial using the factorial function, and sums up these factorials.

return 1 if digit_factorial_sum == N else 0
Checks if the sum of the factorials of the digits (digit_factorial_sum) equals the original number N.
Returns 1 if the condition is true (indicating N is a "perfect" number) and 0 otherwise.

solution = Solution()
Creates an instance of the Solution class.

print(solution.isPerfect(23))
Calls the isPerfect method with the number 23.
Explanation:
Digits of 23 are 2 and 3.
Factorials: 2!=2, 3!=6.
Sum of factorials = 2+6=8 
8 ≠ 23, so the output is 0.

print(solution.isPerfect(145))
Calls the isPerfect method with the number 145.
Explanation:
Digits of 145 are 1, 4, and 5.
Factorials: 1!=1, 4!=24, 5!=120.
Sum of factorials = 1+24+120=145.
145 = 145, so the output is 1.
'''