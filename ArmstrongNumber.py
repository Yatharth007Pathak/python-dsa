"""
You are given a 3-digit number n, Find whether it is an Armstrong number or not.

An Armstrong number of three digits is a number such that the sum of the cubes of its digits is equal to the number itself. 
371 is an Armstrong number since 33 + 73 + 13 = 371. 

Note: Return true if it is an Armstrong number else return false.

Examples

Input: n = 153
Output: true
Explanation: 153 is an Armstrong number since 1^3 + 5^3 + 3^3 = 153. 

Input: n = 372
Output: false
Explanation: 372 is not an Armstrong number since 3^3 + 7^3 + 2^3 = 378. 

Input: n = 100
Output: false
Explanation: 100 is not an Armstrong number since 1^3 + 0^3 + 0^3 = 1. 
"""

class Solution:
    def armstrongNumber(self, n):
        # Convert the number to a string to access each digit
        digits = str(n)
        
        # Calculate the sum of cubes of its digits
        sum_of_cubes = sum(int(digit) ** 3 for digit in digits)
        
        # Check if the sum of cubes is equal to the original number
        return sum_of_cubes == n

sol = Solution()

# Example 1
print(sol.armstrongNumber(153))  # Output: True

# Example 2
print(sol.armstrongNumber(372))  # Output: False

# Example 3
print(sol.armstrongNumber(100))  # Output: False

'''
Here's a line-by-line explanation of the code:

class Solution:
Declares a class named Solution containing the method to check if a number is an Armstrong number.

def armstrongNumber(self, n):
Defines the method armstrongNumber, which takes an integer n as input and checks whether it is an Armstrong number.

digits = str(n)
Converts the integer n into a string so each digit can be accessed individually. For example, 153 becomes "153".

sum_of_cubes = sum(int(digit) ** 3 for digit in digits)
Iterates through each digit in the string representation of n. Converts each digit back to an integer.
Raises the integer to the power of 3 (cube of the digit). Computes the sum of these cubes.

return sum_of_cubes == n
Compares the sum_of_cubes with the original number n.
If equal, returns True (Armstrong number). Otherwise, returns False.
'''
