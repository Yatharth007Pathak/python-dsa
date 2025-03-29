"""
Given a pair of strings of equal lengths, Geek wants to find the better string. The better string is the string having more number 
of distinct subsequences. If both the strings have equal count of distinct subsequence then return str1.

Example 1:
Input: str1 = "gfg", str2 = "ggg"
Output: "gfg"
Explanation: "gfg" have 6 distinct subsequences whereas "ggg" have 3 distinct subsequences. 

Example 2:
Input: str1 = "a", str2 = "b"
Output: "a"
Explanation: Both the strings have only 1 distinct subsequence. 
"""

class Solution:
    def countDistinctSubsequences(self, s):
        n = len(s)
        mod = 1000000007
        
        # To store the last occurrence of each character
        last_occurrence = {}
        
        # dp[i] represents the count of distinct subsequences up to index i
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: empty subsequence
        
        for i in range(1, n + 1):
            dp[i] = (2 * dp[i - 1]) % mod
            
            char = s[i - 1]
            if char in last_occurrence:
                # Subtract the count of subsequences before the last occurrence of the character
                dp[i] = (dp[i] - dp[last_occurrence[char] - 1] + mod) % mod
            
            last_occurrence[char] = i
        
        return dp[n]
    
    def betterString(self, str1, str2):
        count1 = self.countDistinctSubsequences(str1)
        count2 = self.countDistinctSubsequences(str2)
        
        if count1 > count2:
            return str1
        elif count2 > count1:
            return str2
        else:
            return str1

# Example Usage
solution = Solution()
print(solution.betterString("gfg", "ggg"))  # Output: "gfg"
print(solution.betterString("a", "b"))      # Output: "a"

'''
Here's a line-by-line breakdown of the code:

class Solution:
Defines a class named Solution containing two methods: countDistinctSubsequences and betterString.

def countDistinctSubsequences(self, s):
A method that calculates the number of distinct subsequences of a given string s.

n = len(s)
Stores the length of the string in n.

mod = 1000000007
A large prime number is used to ensure calculations stay within integer limits (modular arithmetic).

last_occurrence = {}
A dictionary to store the last occurrence of each character in the string.

dp = [0] * (n + 1)
Creates a dynamic programming array dp of size n + 1.
dp[i] stores the count of distinct subsequences up to the i-th character.

dp[0] = 1
Base case: The empty subsequence is considered one distinct subsequence.

for i in range(1, n + 1):
Iterates over the string from index 1 to n (inclusive).

dp[i] = (2 * dp[i - 1]) % mod
The total number of subsequences up to i is twice the total up to i-1 because 
each subsequence can either include or exclude the i-th character.

char = s[i - 1]
Gets the character at the current index (i-1 because dp is 1-based).

if char in last_occurrence:
Checks if the current character has appeared before.

dp[i] = (dp[i] - dp[last_occurrence[char] - 1] + mod) % mod
If the character has appeared before, subtract the count of subsequences before its last occurrence. 
This ensures we don't count duplicate subsequences created due to the repeated character.

last_occurrence[char] = i
Updates the last occurrence of the current character to the current index.

return dp[n]
Returns the total count of distinct subsequences for the entire string.

def betterString(self, str1, str2):
A method to compare two strings based on the count of their distinct subsequences.

count1 = self.countDistinctSubsequences(str1)
Calculates the number of distinct subsequences for str1.

count2 = self.countDistinctSubsequences(str2)
Calculates the number of distinct subsequences for str2.

if count1 > count2:
Compares the counts. If str1 has more distinct subsequences:

return str1
Returns str1.

elif count2 > count1:
If str2 has more distinct subsequences:

return str2
Returns str2.

else:
If both strings have the same count of distinct subsequences:

return str1
Returns str1 (ties are resolved in favor of str1).

solution = Solution()
Creates an instance of the Solution class.

print(solution.betterString("gfg", "ggg"))
Calls betterString with "gfg" and "ggg" and prints the result.
"gfg" has 7 distinct subsequences, while "ggg" has 4. Output: "gfg".

print(solution.betterString("a", "b"))
Calls betterString with "a" and "b" and prints the result.
Both strings have 2 distinct subsequences. Since counts are equal, the tie is resolved in favor of "a". Output: "a".

Example Outputs:

Input: "gfg", "ggg"
Output: "gfg"

Input: "a", "b"
Output: "a"
'''