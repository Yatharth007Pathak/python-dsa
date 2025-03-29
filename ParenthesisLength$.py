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
        stack = [-1]
        max_length = 0
        
        for i, char in enumerate(S):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_length = max(max_length, i - stack[-1])
        
        return max_length

# Example usage:
if __name__ == "__main__":
    ob = Solution()
    
    # Test case 1
    S1 = "(()("
    print(f"Input: {S1}")
    print("Output:", ob.maxLength(S1))  # Output: 2
    
    # Test case 2
    S2 = "()(())("
    print(f"Input: {S2}")
    print("Output:", ob.maxLength(S2))  # Output: 6
    
    # Test case 3
    S3 = ")()())"
    print(f"Input: {S3}")
    print("Output:", ob.maxLength(S3))  # Output: 4

'''
Code Explanation

class Solution:
This line declares a class named Solution. The class will contain the method for solving the problem.

def maxLength(self, S):
This line defines a method maxLength within the Solution class. It takes a string S representing a sequence of parentheses.

stack = [-1]
Initializes a stack with a single element -1. This is used to handle the indices of parentheses and to manage the length calculations. 
The -1 acts as a base index for calculating lengths of valid substrings.

max_length = 0
Initializes max_length to zero. This variable will keep track of the maximum length of valid parentheses substring found.

for i, char in enumerate(S):
Iterates over the string S with enumerate, which provides both the index i and the character char at that index.

if char == '(':
Checks if the current character is an open parenthesis.

stack.append(i)
If the character is an open parenthesis, push its index i onto the stack.

else:
This block handles the case where the character is a close parenthesis.

stack.pop()
Pops the top index from the stack. This operation removes the most recent open parenthesis index,
which is matched by the current close parenthesis.

if not stack:
Checks if the stack is empty after the pop operation.

stack.append(i)
If the stack is empty, it means the current close parenthesis has no matching open parenthesis (or there are no unmatched open parentheses left)
Push the current index i onto the stack to act as a new base for further calculations.

else:
If the stack is not empty, it means there are unmatched open parentheses still on the stack.

max_length = max(max_length, i - stack[-1])
Calculate the length of the valid substring by subtracting the index at the top of the stack from the current index i. 
Update max_length with the maximum value between the current max_length and the calculated length.

return max_length
Returns the length of the longest valid parentheses substring found.

Example Usage
Test case 1: S1 = "(()("

Expected Output: 2
Explanation: The longest valid substring is "()", which has length 2.
Test case 2: S2 = "()(())("

Expected Output: 6
Explanation: The longest valid substring is "()(())", which has length 6.
Test case 3: S3 = ")()())"

Expected Output: 4
Explanation: The longest valid substring is "()()", which has length 4.
'''