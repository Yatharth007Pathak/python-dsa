"""
Given two strings, txt and pat, find the count of distinct occurrences of pat as a subsequence in txt.

Note: It is guaranteed that the output will fit within 31 bits.

Examples:

Input: txt = "banana" , pat = "ban"
Output: 3
Explanation: There are 3 sub-sequences:[ban], [ba n], [b an].

Input: txt = "geeksforgeeks" , pat = "ge"
Output: 6
Explanation: There are 6 sub-sequences:[ge], [ge], [g e], [g e] [g e] and [g e].

Input: txt = "aabbcc" , pat = "abc"
Output: 8
Explanation: There are 8 distinct subsequences: [a b c], [a b c], [a b c], [a b c], [a b c], [a b c], [a b c], [a b c].
"""

class Solution:
    def sequenceCount(self, txt: str, pat: str) -> int:
        m, n = len(txt), len(pat)
        
        # Initialize dp array with zeros
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Base case initialization
        for i in range(m + 1):
            dp[i][0] = 1  # Empty pat can be matched with any substring of txt
        
        # Fill dp array
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # If characters match, add both possibilities
                if txt[i - 1] == pat[j - 1]:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        # Result is the number of ways to form pat in txt
        return dp[m][n]

# Example usage
sol = Solution()
print(sol.sequenceCount("banana", "ban"))  # Output: 3
print(sol.sequenceCount("geeksforgeeks", "ge"))  # Output: 6
print(sol.sequenceCount("aabbcc", "abc"))  # Output: 8

'''
Here's a line-by-line breakdown of the code for counting the number of times a pattern sequence appears in a text using dynamic programming.

Define the Solution class: This class will contain the sequenceCount method, which performs the sequence counting.

Define the sequenceCount method: This method takes in a txt (the main text string) and a pat 
(the pattern string) as inputs and returns the count of distinct subsequences of txt that match pat.

Calculate lengths of txt and pat: Store the lengths of txt in m and pat in n.

Initialize a 2D list dp with zeros: Create a dp table of size (m + 1) x (n + 1), initialized to zero. 
Here, dp[i][j] will hold the number of ways to match the first j characters of pat with the first i characters of txt.

Base case initialization: For all i from 0 to m, set dp[i][0] to 1, 
representing that an empty pattern can be matched with any substring of txt in exactly one way (by choosing no characters).

Start filling the dp table: Use two nested loops to fill the table:
i loop from 1 to m: Represents the length of txt considered.
j loop from 1 to n: Represents the length of pat considered.

Check if characters match (txt[i-1] == pat[j-1]): If they match, there are two options:
Count subsequences that include this character match: dp[i-1][j-1].
Count subsequences that exclude this character: dp[i-1][j].
Sum these values to update dp[i][j].

If characters do not match: Only consider the subsequences that exclude the character from txt, updating dp[i][j] to dp[i-1][j].

Return the final result in dp[m][n]: This value contains the number of ways to form pat in txt as a subsequence.

Example Test Cases
The code includes test cases that showcase the function's ability to count distinct subsequences:

txt = "banana" and pat = "ban" returns 3.
txt = "geeksforgeeks" and pat = "ge" returns 6.
txt = "aabbcc" and pat = "abc" returns 8.

This approach effectively uses dynamic programming to solve the problem in O(m * n) time complexity.
'''