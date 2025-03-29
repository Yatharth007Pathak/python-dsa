"""
Given two integers a and b, write a function lcmAndGcd() to compute their LCM and GCD. 
The function takes two integers a and b as input and returns a list containing their LCM and GCD.

Input: a = 5 , b = 10
Output: 10 5
Explanation: LCM of 5 and 10 is 10, while their GCD is 5.

Input: a = 14 , b = 8
Output: 56 2
Explanation: LCM of 14 and 8 is 56, while their GCD is 2
"""

import math

class Solution:
    def lcmAndGcd(self, A, B):
        # GCD calculation using math.gcd()
        gcd_value = math.gcd(A, B)
        # LCM calculation using the formula: LCM(a, b) = abs(a * b) // GCD(a, b)
        lcm_value = abs(A * B) // gcd_value
        return [lcm_value, gcd_value]

# Example 1
a, b = 5, 10
sol = Solution()
print(f"Input: a = {a}, b = {b}")
result = sol.lcmAndGcd(a, b)
print(f"Output: {result[0]} {result[1]}")

# Example 2
a, b = 14, 8
print(f"\nInput: a = {a}, b = {b}")
result = sol.lcmAndGcd(a, b)
print(f"Output: {result[0]} {result[1]}")


'''
Here's a breakdown of the code:

Import math module: The math module is imported, specifically for using the built-in math.gcd() function to calculate the GCD.

Define class Solution: A class named Solution is defined, containing a method to compute both the LCM and GCD.

Define lcmAndGcd method: Inside the class, the method lcmAndGcd(self, A, B) is defined, 
where A and B are the two input numbers for which the LCM and GCD are calculated.

Calculate GCD: The GCD of A and B is calculated using the math.gcd(A, B) function, and the result is stored in the variable gcd_value.

Calculate LCM: The LCM is calculated using the formula: abs(A * B) // gcd_value

The abs() function ensures the result is non-negative, and the division is done using // to return an integer value. 
The result is stored in lcm_value.

Return LCM and GCD: The method returns both the LCM and GCD as a list [lcm_value, gcd_value].

Example 1 (a = 5, b = 10): The numbers 5 and 10 are assigned to a and b. 
An object sol of class Solution is created, and lcmAndGcd(a, b) is called. 
The result is printed as "Output: 10 5", where 10 is the LCM and 5 is the GCD.

Example 2 (a = 14, b = 8): Another set of numbers 14 and 8 are assigned to a and b. 
The method is called again, and the result is printed as "Output: 56 2", where 56 is the LCM and 2 is the GCD.
'''