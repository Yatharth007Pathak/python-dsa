"""
Given a string S, check if it is palindrome or not.

Example:
Input: S = "abba"
Output: 1
Explanation: S is a palindrome
"""

class Solution:
    def isPalindrome(self, S):
        # Check if the string is equal to its reverse
        if S == S[::-1]:
            return 1  # Return 1 if it's a palindrome
        else:
            return 0  # Return 0 if it's not a palindrome

solution = Solution()
print(solution.isPalindrome("radar"))  # Output: 1
print(solution.isPalindrome("hello"))  # Output: 0

'''
Here's a breakdown of the code:

class Solution:
Defines a class named Solution. This class contains methods that solve specific problems.

def isPalindrome(self, S):
Defines a method named isPalindrome within the Solution class. The method takes a single argument S, which is a string. 
The goal is to check whether the string is a palindrome.

if S == S[::-1]:
This line checks if the string S is equal to its reverse.
S[::-1] creates a reversed version of the string S. The slicing syntax [::-1] means 
"step backwards through the string," effectively reversing it.
If S is equal to its reverse, the string is a palindrome.

return 1 
If the string is a palindrome (i.e., S is equal to S[::-1]), the method returns 1.

else:
This else clause handles the case where the string is not a palindrome.

return 0 
If the string is not a palindrome, the method returns 0.

solution = Solution()
Creates an instance of the Solution class.

print(solution.isPalindrome("radar")) # Output: 1
Calls the isPalindrome method with the string "radar". Since "radar" is a palindrome, the method returns 1, and 1 is printed as the output.

print(solution.isPalindrome("hello")) # Output: 0
Calls the isPalindrome method with the string "hello". Since "hello" is not a palindrome, the method returns 0, and 0 is printed as the output.
'''