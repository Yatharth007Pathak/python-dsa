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
    # Function to find the longest palindromic substring.
    def longestPalin(self, S):
        # Function to expand around the center and return the longest palindrome substring
        def expandAroundCenter(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the palindrome substring found by expanding
            return s[left + 1:right]

        if not S or len(S) == 1:
            return S
        
        longest_palindrome = ""
        
        for i in range(len(S)):
            # Odd-length palindromes (single character center)
            palin1 = expandAroundCenter(S, i, i)
            # Even-length palindromes (two consecutive characters as center)
            palin2 = expandAroundCenter(S, i, i + 1)
            
            # Update the longest palindrome found so far
            if len(palin1) > len(longest_palindrome):
                longest_palindrome = palin1
            if len(palin2) > len(longest_palindrome):
                longest_palindrome = palin2
        
        return longest_palindrome

solution = Solution()
print(solution.longestPalin("aaaabbaa"))  # Output: "aabbaa"
print(solution.longestPalin("abc"))       # Output: "a"
