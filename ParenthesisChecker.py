"""
Given an expression string x. Examine whether the pairs and the orders of {,},(,),[,] are correct in exp.
For example, the function should return 'true' for exp = [()]{}{[()()]()} and 'false' for exp = [(]).

Note: The driver code prints "balanced" if function return true, otherwise it prints "not balanced".

Examples :

Input: {([])}
Output: true
Explanation: { ( [ ] ) }. Same colored brackets can form balanced pairs, with 0 number of unbalanced bracket.

Input: ()
Output: true
Explanation: (). Same bracket can form balanced pairs,and here only 1 type of bracket is present and in balanced way.

Input: ([]
Output: false
Explanation: ([]. Here square bracket is balanced but the small bracket is not balanced and Hence , the output will be unbalanced.
"""

class Solution:
    
    # Function to check if brackets are balanced or not.
    def ispar(self, x):
        stack = []
        # Dictionary to map closing brackets to opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        
        for char in x:
            # If the character is an opening bracket, push it onto the stack
            if char in bracket_map.values():
                stack.append(char)
            # If the character is a closing bracket
            elif char in bracket_map:
                # Check if stack is empty or the top element is not the matching opening bracket
                if not stack or stack[-1] != bracket_map[char]:
                    return False
                # Pop the matching opening bracket
                stack.pop()
        
        # If stack is empty, all brackets are balanced
        return len(stack) == 0

# Test code
solution = Solution()
test_cases = ["{([])}", "()", "([]", "[()]{[()()]()}"]

for case in test_cases:
    if solution.ispar(case):
        print("balanced")
    else:
        print("not balanced")

'''
Stack: The stack helps keep track of opening brackets.
Bracket Map: A dictionary (bracket_map) maps closing brackets to their corresponding opening brackets.
Loop: When an opening bracket is found, it's pushed onto the stack. When a closing bracket is found, we check if the stack is empty or if 
the top of the stack matches the corresponding opening bracket. If they match, the opening bracket is popped from the stack.
Result: If the stack is empty at the end of the iteration, it means all brackets were balanced.


here is a pointwise explanation for each line of the given code:

class Solution:
Defines a class named Solution.

# Function to check if brackets are balanced or not.
Adds a comment describing the purpose of the function ispar.

def ispar(self, x):
Defines a function named ispar which takes an argument x (the string of brackets to be checked).

stack = []
Initializes an empty list named stack to keep track of opening brackets.

bracket_map = {')': '(', '}': '{', ']': '['}
Defines a dictionary bracket_map that maps each closing bracket to its corresponding opening bracket.

for char in x:
Starts a for loop to iterate over each character in the string x.

if char in bracket_map.values():
Checks if the character char is one of the opening brackets ('(', '{', '[').

stack.append(char)
If the character is an opening bracket, it is added to the stack.

elif char in bracket_map:
Checks if the character char is a closing bracket (')', '}', ']').

if not stack or stack[-1] != bracket_map[char]:
Checks if the stack is empty or if the top element of the stack is not the matching opening bracket for the current closing bracket.

return False
If either condition is true, it returns False, indicating that the brackets are not balanced.

stack.pop()
If the matching opening bracket is found, removes the top element from the stack.

return len(stack) == 0
At the end of the loop, checks if the stack is empty. Returns True if empty (indicating all brackets are balanced), otherwise returns False.

# Test code
Adds a comment indicating the start of test code.

solution = Solution()
Creates an instance of the Solution class.

test_cases = ["{([])}", "()", "([]", "[()]{[()()]()}"]
Defines a list test_cases containing several strings to test the ispar function.

for case in test_cases:
Starts a for loop to iterate over each test case in test_cases.

if solution.ispar(case):
Calls the ispar function for the current test case. Checks if the return value is True.

print("balanced")
If the brackets are balanced (ispar returns True), prints "balanced".

else:
If the brackets are not balanced (ispar returns False), executes the next statement.

print("not balanced")
Prints "not balanced" if the brackets are not balanced.
'''