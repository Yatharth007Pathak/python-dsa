"""
Given a binary string S. The task is to count the number of substrings that start and end with 1. 
For example, if the input string is “00100101”, then there are three substrings “1001”, “100101” and “101”.

Example 1:
Input: N = 4, S = 1111
Output: 6
Explanation: There are 6 substrings from the given string. They are 11, 11, 11, 111, 111, 1111.

Example 2:
Input: N = 5, S = 01101
Output: 3
Explanation: There 3 substrings from the given string. They are 11, 101, 1101.
"""

class Solution:
    def binarySubstring(self, n, s):
        # Count the number of 1's in the string
        count_ones = s.count('1')
        # Calculate the number of substrings using the formula
        return (count_ones * (count_ones - 1)) // 2

# Example usage
solution = Solution()
print(solution.binarySubstring(4, "1111"))  # Output: 6
print(solution.binarySubstring(5, "01101"))  # Output: 3

'''
Here's a detailed plain-text breakdown of the code:

class Solution:
Defines a class named Solution containing the method binarySubstring.

def binarySubstring(self, n, s):
A method to calculate the number of substrings in the binary string s that start and end with the character '1'.

count_ones = s.count('1')
Uses the count method to calculate the total number of '1' characters in the string s.
Each '1' in the string can potentially pair with another '1' to form a substring that starts and ends with '1'.

return (count_ones * (count_ones - 1)) // 2
The formula (n*(n-1))/2 calculates the number of unique pairs of '1' characters, where n is the count of '1' in the string.
Each pair of '1' corresponds to a substring that starts and ends with '1'.

solution = Solution()
Creates an instance of the Solution class.

print(solution.binarySubstring(4, "1111"))
Calls binarySubstring with the string "1111" and prints the result.
Input: "1111".
Count of '1': 4.
Substrings:
'11' (from first and second '1'),
'11' (from first and third '1'),
'11' (from first and fourth '1'),
'11' (from second and third '1'),
'11' (from second and fourth '1'),
'11' (from third and fourth '1').
Total: 6
Output: 6.

print(solution.binarySubstring(5, "01101"))
Calls binarySubstring with the string "01101" and prints the result.
Input: "01101".
Count of '1': 3.
Substrings:
'11' (from second and third '1'),
'11' (from second and fourth '1'),
'11' (from third and fourth '1').
Total: 3
Output: 3.
'''

