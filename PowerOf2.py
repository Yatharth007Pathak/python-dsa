"""
Given a non-negative integer n. The task is to check if it is a power of 2. 

Examples

Input: n = 8
Output: true
Explanation: 8 is equal to 2 raised to 3 (23 = 8).

Input: n = 98
Output: false
Explanation: 98 cannot be obtained by any power of 2.

Input: n = 1
Output: true
Explanation: (20 = 1).
"""

class Solution:
    # Function to check if the given number n is a power of two.
    def isPowerofTwo(self, n: int) -> bool:
        # 0 or negative numbers cannot be a power of 2
        if n <= 0:
            return False
        
        # A number is a power of 2 if n & (n-1) is 0
        return (n & (n - 1)) == 0

# Create an instance of the Solution class
solution = Solution()

# Test cases
numbers = [4, 5, 16, 0, -8, 64]

# Loop through test cases and print the results
for number in numbers:
    print(f"Is {number} a power of two? {solution.isPowerofTwo(number)}")

'''
Here's a breakdown of the given code:

class Solution: Defines a class called Solution, which contains the method for checking if a number is a power of two.

def isPowerofTwo(self, n: int) -> bool: Declares a function isPowerofTwo inside the class that takes an integer n as input 
and returns a boolean value (True or False).

if n <= 0: This checks if the number n is less than or equal to 0. 
If it is, the number cannot be a power of two because power-of-two numbers are always positive.

return False: If n is less than or equal to 0, the function returns False, meaning it is not a power of two.

return (n & (n - 1)) == 0: This line checks if n is a power of two by using a bitwise AND operation. 
The expression n & (n - 1) clears the lowest set bit of n. 
If the result is 0, it means n is a power of two, and the function returns True. Otherwise, it returns False.

solution = Solution(): Creates an instance of the Solution class.

numbers = [4, 5, 16, 0, -8, 64]: Initializes a list of numbers that will be tested to see if they are powers of two.

for number in numbers: Loops through each number in the numbers list.

print(f"Is {number} a power of two? {solution.isPowerofTwo(number)}"): For each number in the list, 
it prints whether the number is a power of two by calling the isPowerofTwo method on the solution object.
The output will display whether each number in the numbers list is a power of two.

Example:
For n = 8:

8 in binary is 1000, and 7 is 0111.
1000 & 0111 = 0000, which is 0. So, 8 is a power of 2, and the function will return True.
For n = 98:

98 in binary is 1100010, and 97 is 1100001.
1100010 & 1100001 = 1100000, which is not 0. So, 98 is not a power of 2, and the function will return False.
For n = 1:

1 in binary is 1, and 0 is 0.
1 & 0 = 0, so 1 is a power of 2, and the function will return True.
'''