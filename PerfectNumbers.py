"""
Given a number n, check if a number is perfect or not. A number is said to be perfect if sum of all its factors 
excluding the number itself is equal to the number. 

Examples:

Input: n = 6
Output: true 
Explanation: Factors of 6 are 1, 2, 3 and 6. Excluding 6 their sum is 6 which is equal to N itself. So, it's a Perfect Number.

Input: n = 10
Output: false
Explanation: Factors of 10 are 1, 2, 5 and 10. Excluding 10 their sum is 8 which is not equal to N itself. So, it's not a Perfect Number.

Input: n = 11
Output: false
Explanation: Factors of 11 are 1, 11. Excluding 11 their sum is 1 which is not equal to N itself. So, it's not a Perfect Number.
"""

class Solution:
    def isPerfectNumber(self, n):
        if n <= 1:
            return False  # Perfect numbers are greater than 1

        sum_of_factors = 0

        # Find factors of n and calculate their sum
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                sum_of_factors += i
                if i != 1 and i != n // i:  # Avoid adding n and duplicates
                    sum_of_factors += n // i

        # Check if the sum of factors excluding n is equal to n
        return sum_of_factors == n

# Examples
solution = Solution()
print(solution.isPerfectNumber(6))  # Output: True
print(solution.isPerfectNumber(10))  # Output: False
print(solution.isPerfectNumber(11))  # Output: False

'''
Here's a line-by-line explanation of the code:

class Solution:
Defines a class named Solution to group the function that checks for perfect numbers.

def isPerfectNumber(self, n):
Declares a method isPerfectNumber inside the class. It takes two parameters: 
self (refers to the class instance) and n (the number to check).

if n <= 1:
Checks if n is less than or equal to 1. Perfect numbers are greater than 1.

return False
Returns False if n is less than or equal to 1 because such numbers cannot be perfect.

sum_of_factors = 0
Initializes sum_of_factors to 0, which will store the sum of the proper divisors of n.

for i in range(1, int(n**0.5) + 1):
Loops through integers from 1 to the square root of n (inclusive). 
Factors of n occur in pairs, so checking up to the square root is sufficient.

if n % i == 0:
Checks if i is a divisor of n (i.e., n is divisible by i with no remainder).

sum_of_factors += i
Adds i to sum_of_factors because it is a divisor of n.

if i != 1 and i != n // i:
Ensures that the factor pair n // i is not added redundantly. Avoids adding n itself or duplicating the square root factor.

sum_of_factors += n // i
Adds the factor n // i to sum_of_factors.

return sum_of_factors == n
Checks if the sum of proper divisors (excluding n itself) equals n.
Returns True if the condition is satisfied, indicating n is a perfect number; otherwise, returns False.

solution = Solution()
Creates an instance of the Solution class.

print(solution.isPerfectNumber(6))
Calls the isPerfectNumber method with 6.
Explanation:
Divisors of 6: 1,2,3.
Sum of divisors = 1+2+3=6.
6=6, so the output is True.

print(solution.isPerfectNumber(10))
Calls the isPerfectNumber method with 10.
Explanation:
Divisors of 10: 1,2,5.
Sum of divisors = 1+2+5=8.
8≠10, so the output is False.

print(solution.isPerfectNumber(11))
Calls the isPerfectNumber method with 11.
Explanation:
Divisors of 11: 1
Sum of divisors = 1
1≠11, so the output is False.
'''