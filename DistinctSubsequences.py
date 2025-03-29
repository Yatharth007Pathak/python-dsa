"""
Given a string consisting of lower case English alphabets, the task is to find the number of distinct subsequences of the string
Note: Answer can be very large, so, ouput will be answer modulo 109+7.

Example 1:
Input: s = "gfg"
Output: 7
Explanation: The seven distinct subsequences are "", "g", "f", "gf", "fg", "gg" and "gfg" .

Example 2:
Input: s = "ggg"
Output: 4
Explanation: The four distinct subsequences are "", "g", "gg", "ggg".
"""

class Solution:
    def distinctSubsequences(self, S):
        mod = 1000000007  # As the result can be very large, take modulo 10^9+7
        n = len(S)
        
        # dp[i] represents the number of distinct subsequences up to index i
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: the empty subsequence
        
        # Dictionary to store the last occurrence of each character
        last_occurrence = {}
        
        for i in range(1, n + 1):
            # Double the number of subsequences from the previous index
            dp[i] = (2 * dp[i - 1]) % mod
            
            char = S[i - 1]
            if char in last_occurrence:
                # Subtract the count of subsequences before the last occurrence
                dp[i] = (dp[i] - dp[last_occurrence[char] - 1] + mod) % mod
            
            # Update the last occurrence of the current character
            last_occurrence[char] = i
        
        # The result is stored in dp[n]
        return dp[n]

# Example usage
solution = Solution()
print(solution.distinctSubsequences("gfg"))  # Output: 7
print(solution.distinctSubsequences("ggg"))  # Output: 4

'''
Here's a plain-text breakdown of the code:

class Solution:
Defines a class named Solution that contains the method distinctSubsequences.

def distinctSubsequences(self, S):
A method to calculate the number of distinct subsequences of a given string S.

mod = 1000000007
A large prime number used to perform modular arithmetic and prevent integer overflow.

n = len(S)
Stores the length of the string S.

dp = [0] * (n + 1)
Creates a dynamic programming array dp of size n + 1.
dp[i] will store the number of distinct subsequences up to the i-th character of S.

dp[0] = 1
Base case: The empty subsequence is counted as one distinct subsequence.

last_occurrence = {}
Initializes an empty dictionary to store the last occurrence of each character in the string.

for i in range(1, n + 1):
Loops through the string from index 1 to n (inclusive).

dp[i] = (2 * dp[i - 1]) % mod
The total number of subsequences up to i is initially twice the total up to i-1.
This is because each subsequence up to i-1 can either include or exclude the i-th character.

char = S[i - 1]
Gets the character at the current index (i-1 because dp is 1-based).

if char in last_occurrence:
Checks if the current character has appeared before.

dp[i] = (dp[i] - dp[last_occurrence[char] - 1] + mod) % mod
If the character has appeared before:

Subtracts the count of subsequences that existed before the last occurrence of the character.
Adds mod to ensure the result is non-negative before taking modulo.

last_occurrence[char] = i
Updates the last occurrence of the current character to the current index.

return dp[n]
Returns the total number of distinct subsequences for the entire string, which is stored in dp[n].

solution = Solution()
Creates an instance of the Solution class.

print(solution.distinctSubsequences("gfg"))
Calls distinctSubsequences with "gfg" and prints the result.
Distinct subsequences: ["", "g", "f", "gf", "fg", "gfg"].
Output: 7.

print(solution.distinctSubsequences("ggg"))
Calls distinctSubsequences with "ggg" and prints the result.
Distinct subsequences: ["", "g", "gg", "ggg"].
Output: 4.

Example Outputs:

Input: "gfg"
Output: 7

Input: "ggg"
Output: 4
'''