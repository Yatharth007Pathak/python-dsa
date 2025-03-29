"""
Given a string str, find the longest palindromic substring in str. Substring of string str: str[ i . . . . j ] where 0 ≤ i ≤ j < len(str). 
Return the longest palindromic substring of str.

Palindrome string: A string that reads the same backward. More formally, str is a palindrome if reverse(str) = str. 
In case of conflict, return the substring which occurs first ( with the least starting index).

Examples :

Input: str = "aaaabbaa"
Output: aabbaa
Explanation: The longest Palindromic substring is "aabbaa".

Input: str = "abc"
Output: a
Explanation: "a", "b" and "c" are the longest palindromes with same length. The result is the one with the least starting index.
"""

class Solution:
    def longestPalin(self, S: str) -> str:
        # Function to expand around center and check for palindrome
        def expandAroundCenter(left: int, right: int) -> str:
            # Expand as long as the characters at left and right are the same
            while left >= 0 and right < len(S) and S[left] == S[right]:
                left -= 1
                right += 1
            # Return the longest palindrome found
            return S[left + 1:right]
        
        # Base case: If the string is empty or has only one character
        if len(S) <= 1:
            return S
        
        longest_palindrome = ""
        
        for i in range(len(S)):
            # Odd length palindromes (single character center)
            palindrome1 = expandAroundCenter(i, i)
            # Even length palindromes (between two characters center)
            palindrome2 = expandAroundCenter(i, i + 1)
            
            # Choose the longer palindrome between palindrome1 and palindrome2
            longer_palindrome = palindrome1 if len(palindrome1) > len(palindrome2) else palindrome2
            
            # Update the longest palindrome if we found a longer one
            if len(longer_palindrome) > len(longest_palindrome):
                longest_palindrome = longer_palindrome
        
        return longest_palindrome
