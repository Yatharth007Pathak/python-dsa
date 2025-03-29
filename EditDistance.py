"""
Given two strings str1 and str2. Return the minimum number of operations required to convert str1 to str2.
The possible operations are permitted:

Insert a character at any position of the string.
Remove any character from the string.
Replace any character from the string with any other character.

Examples:

Input: str1 = "geek", srt2 = "gesek"
Output: 1
Explanation: One operation is required, inserting 's' between two 'e'.

Input : str1 = "gfg", str2 = "gfg"
Output: 0
Explanation: Both strings are same.
"""

class Solution:
    def editDistance(self, str1, str2):
        n = len(str1)
        m = len(str2)
        
        # Create a DP table
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        
        # Base cases
        for j in range(m + 1):
            dp[0][j] = j  # If str1 is empty, we need to insert all characters of str2
            
        for i in range(n + 1):
            dp[i][0] = i  # If str2 is empty, we need to remove all characters of str1
        
        # Fill the DP table
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if str1[i - 1] == str2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]  # No operation needed
                else:
                    dp[i][j] = min(
                        dp[i][j - 1],     # Insert
                        dp[i - 1][j],     # Remove
                        dp[i - 1][j - 1]  # Replace
                    ) + 1
        
        return dp[n][m]  # The last cell contains the result

# Example usage:
solution = Solution()
print(solution.editDistance("geek", "gesek"))  # Output: 1
print(solution.editDistance("gfg", "gfg"))      # Output: 0

'''
The editDistance function you implemented calculates the minimum number of operations required to convert one string into another. 
These operations can include insertion, deletion, or replacement of characters. 
The algorithm uses dynamic programming to efficiently compute this value. Here's a detailed breakdown of how the code works:

class Solution:
Defines a class Solution that contains the editDistance method.

def editDistance(self, str1, str2):
This method takes two strings as input, str1 and str2.

n = len(str1):
Calculates the length of str1 and stores it in n.

m = len(str2):
Calculates the length of str2 and stores it in m.

dp = [[0] * (m + 1) for _ in range(n + 1)]:
Initializes a 2D list dp with dimensions (n + 1) x (m + 1) to store the edit distances. 
Each cell will hold the minimum edit distance for substrings of str1 and str2.

Base Cases
for j in range(m + 1):
Sets up the base case for converting an empty str1 to str2.

dp[0][j] = j:
If str1 is empty, we need to insert all characters of str2. Thus, the cost is equal to the length of str2.
for i in range(n + 1):
Sets up the base case for converting str1 to an empty str2.

dp[i][0] = i:
If str2 is empty, we need to remove all characters of str1. Thus, the cost is equal to the length of str1.
Filling the DP Table
for i in range(1, n + 1):
Iterates through each character of str1.

for j in range(1, m + 1):
Iterates through each character of str2.

if str1[i - 1] == str2[j - 1]:
Checks if the current characters of str1 and str2 match.

dp[i][j] = dp[i - 1][j - 1]:
If the characters are the same, the edit distance remains the same as it was for the previous characters of both strings.

else:
If the characters do not match, we calculate the minimum edit distance considering the three possible operations:
Insert: dp[i][j - 1]
Remove: dp[i - 1][j]
Replace: dp[i - 1][j - 1]

dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1:
Takes the minimum of the three options and adds 1 for the operation performed.

Return Result

return dp[n][m]:
Returns the value in the bottom-right cell of the dp table, which contains the minimum edit distance for converting str1 to str2.

solution = Solution()
print(solution.editDistance("geek", "gesek"))  # Output: 1
print(solution.editDistance("gfg", "gfg"))      # Output: 0

Output Explanation
For the first example, converting "geek" to "gesek" requires one operation (inserting 's'), resulting in an output of 1.
For the second example, both strings are identical, requiring zero operations, resulting in an output of 0.

Complexity Analysis
Time Complexity: O(n * m), where n is the length of str1 and m is the length of str2.
Space Complexity: O(n * m) for the dp table.
'''