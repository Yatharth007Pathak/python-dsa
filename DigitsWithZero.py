"""
Given a number d, representing the number of digits of a number. 
Find the total count of positive integers which have at-least one zero in them and consist d or less digits.
In general, for n digits, there are 9 * 10^(n-1) numbers.

Example 1:
Input: d = 2
Output: 9 
Explanation: There are total 9 positive integers which have at-least one zero in them and consist 2 or less digits.

Example 2:
Input: d = 3
Output: 180
Explanation: There are total 180 positive integers which have at-least one zero in them and consist 3 or less digits.
"""

class Solution:
    def findCountUpto(self, d):
        # Total count of numbers with at most d digits
        total_count = 0
        # Count of numbers with no zeros with at most d digits
        non_zero_count = 0
        
        for i in range(1, d + 1):
            # Total numbers with i digits (9 * 10^(i-1))
            total_count += 9 * (10 ** (i - 1))
            # Non-zero numbers with i digits (9^i)
            non_zero_count += 9 ** i
        
        # Numbers with at least one zero is the difference
        return total_count - non_zero_count

# Example usage:
solution = Solution()
print(solution.findCountUpto(2))  # Output: 9
print(solution.findCountUpto(3))  # Output: 180

'''
Here's a breakdown of how the code works:

Define class Solution: A class named Solution is defined, 
which contains the method findCountUpto to calculate the count of numbers with at least one zero up to d digits.

Define findCountUpto method: The method findCountUpto(self, d) takes d as input, which represents the number of digits to consider.

Initialize counters:
total_count = 0: This will store the total number of integers with at most d digits.
non_zero_count = 0: This will store the total number of integers with at most d digits, but without any zeros.

Loop to calculate counts:
The loop runs from 1 to d to calculate the count for each number of digits (from 1 digit to d digits).
Total numbers with i digits: For each i digits, the formula 9 * (10 ** (i - 1)) is used. 
This gives the total number of i-digit numbers. The reasoning is that:
For 1-digit numbers: there are 9 possible numbers (1 to 9).
For 2-digit numbers: there are 9 choices for the first digit (1 to 9) and 10 choices for the second digit (0 to 9), giving a total of 9 * 10.
For i digits, the formula generalizes as 9 * 10^(i - 1).
Non-zero numbers with i digits: The formula 9 ** i is used for numbers without any zeros. 
For each digit place, there are 9 choices (1 to 9) for each position, resulting in 9^i non-zero numbers.

Difference gives numbers with zeros: 
The total count of numbers with at least one zero is the difference between the total numbers and the non-zero numbers. 
This value is returned by the method.

Example usage:

Example 1 (d = 2): The total number of 1-digit and 2-digit numbers is calculated, and so is the count of numbers without zeros. 
The output is 9, which represents the count of numbers with at least one zero.
Example 2 (d = 3): The total number of 1-digit, 2-digit, and 3-digit numbers is calculated, as well as the non-zero numbers. 
The output is 180, which represents the count of numbers with at least one zero up to 3 digits.
'''