"""
For an input year N, find whether the year is a leap or not. 
 
Example 1:
Input: N = 4
Output: 1
Explanation: 4 is not divisible by 100 and is divisible by 4 so its a leap year

Example 2:
Input: N = 2021
Output: 0
Explanation: 2021 is not divisible by 100 and is also not divisible by 4 so its not a leap year
"""

class Solution:
    def isLeap(self, N):
        # A leap year is divisible by 4, but not by 100, unless it is divisible by 400
        if (N % 4 == 0 and N % 100 != 0) or (N % 400 == 0):
            return 1  # Leap year
        else:
            return 0  # Not a leap year

# Example 1
N = 4
sol = Solution()
print(f"Input: N = {N}")
result = sol.isLeap(N)
print(f"Output: {result}")

# Example 2
N = 2021
print(f"\nInput: N = {N}")
result = sol.isLeap(N)
print(f"Output: {result}")

# Example 2
N = 2024
print(f"\nInput: N = {N}")
result = sol.isLeap(N)
print(f"Output: {result}")

'''
Here's the breakdown:

Define class Solution: A class named Solution is defined, which contains a method to check for leap years.

Define isLeap method: Inside the class, the method isLeap(self, N) is defined. The input parameter N is the year that needs to be checked.

Leap year condition:
The condition checks if N is divisible by 4 and not divisible by 100, using the expression N % 4 == 0 and N % 100 != 0. 
This handles most leap years.
Additionally, if the year is divisible by 400 (N % 400 == 0), it is also considered a leap year. 
This rule overrides the 100-year rule for centuries.
If either of these conditions is true, the method returns 1 (indicating a leap year), otherwise, it returns 0 (not a leap year).
Return values: The method returns 1 for a leap year and 0 for a non-leap year.

Example 1 (N = 4): The year 4 is checked, and since it is divisible by 4 and not 100, it is a leap year. The output is "Output: 1".

Example 2 (N = 2021): The year 2021 is checked, and since it is not divisible by 4, it is not a leap year. The output is "Output: 0".

Example 3 (N = 2024): The year 2024 is checked, and since it is divisible by 4 and not by 100, it is a leap year. The output is "Output: 1".
'''