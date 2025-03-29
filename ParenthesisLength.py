"""
Given a string S consisting of opening and closing parenthesis '(' and ')'. Find length of the longest valid parenthesis substring.
Note: The length of the smallest valid substring ( ) is 2.

Example 1:
Input: S = "(()("
Output: 2
Explanation: The longest valid substring is "()". Length = 2.

Example 2:
Input: S = "()(())("
Output: 6
Explanation: The longest valid substring is "()(())". Length = 6.

Example 3:
Input: str = )()())
Output: 4
Explanation: The longest valid substring is "()()". Length = 4.
"""

class Solution:
    def maxLength(self, S):
        def longest_valid_length(s):
            max_len = 0
            open_count = 0
            close_count = 0

            # Left to Right Pass
            for char in s:
                if char == '(':
                    open_count += 1
                else:  # char == ')'
                    close_count += 1

                if open_count == close_count:
                    max_len = max(max_len, 2 * close_count)
                elif close_count > open_count:
                    open_count = close_count = 0

            return max_len
        
        # First pass from left to right
        length1 = longest_valid_length(S)
        
        # Second pass from right to left
        reversed_S = S[::-1]
        length2 = longest_valid_length(reversed_S)
        
        # The result is the maximum of both pass lengths
        return max(length1, length2)

# Example usage:
ob = Solution()

# Test case 1
S = "(()("
print(ob.maxLength(S))  # Output: 2

# Test case 2
S = "()(())("
print(ob.maxLength(S))  # Output: 6

# Test case 3
S = ")()())"
print(ob.maxLength(S))  # Output: 4

'''
Let's break down each line of code in the provided solution:

class Solution:
This line defines a class named Solution. In this case, it's used to encapsulate the solution method.

def maxLength(self, S):
This line defines a method maxLength within the Solution class. It takes a string S as input, which represents a string of parentheses.

def longest_valid_length(s):
This nested function calculates the length of the longest valid parentheses substring within the string s. 
It uses a counting approach to track the number of open and close parentheses.

max_len = 0
Initializes max_len to zero. This variable will store the length of the longest valid parentheses substring found so far.

open_count = 0
Initializes open_count to zero. This variable counts the number of open parentheses encountered.

close_count = 0
Initializes close_count to zero. This variable counts the number of close parentheses encountered.

# Left to Right Pass
This comment indicates that the following code block performs a pass from left to right through the string.

for char in s:
This loop iterates over each character in the string s.

if char == '(':
Checks if the current character is an open parenthesis.

open_count += 1
If the character is an open parenthesis, increment open_count.

else: # char == ')'
If the character is not an open parenthesis, it must be a close parenthesis.

close_count += 1
Increment close_count for a close parenthesis.

if open_count == close_count:
Checks if the number of open and close parentheses are equal.

max_len = max(max_len, 2 * close_count)
Updates max_len with the maximum of the current max_len or twice the number of close parentheses 
(since each close parenthesis corresponds to an open parenthesis).

elif close_count > open_count:
If the number of close parentheses exceeds the number of open parentheses, the current substring is invalid.

open_count = close_count = 0
Reset both open_count and close_count to zero, as the current substring is no longer valid.

return max_len
Returns the length of the longest valid parentheses substring found during this pass.

length1 = longest_valid_length(S)
Calls longest_valid_length for the original string S to find the length of the longest valid parentheses substring from left to right.

reversed_S = S[::-1]
Reverses the string S to perform a pass from right to left.

length2 = longest_valid_length(reversed_S)
Calls longest_valid_length for the reversed string to find the length of the longest valid parentheses substring from right to left.

return max(length1, length2)
Returns the maximum value between the lengths found from the two passes. 
This ensures that the longest valid substring is captured regardless of its position in the original string.

Example Usage
Test case 1: S = "(()("
Expected output: 2
Explanation: The longest valid substring is "()", which has length 2.

Test case 2: S = "()(())("
Expected output: 6
Explanation: The longest valid substring is "()(())", which has length 6.

Test case 3: S = ")()())"
Expected output: 4
Explanation: The longest valid substring is "()()", which has length 4.
'''