"""
Find the number of unique words consisting of lowercase alphabets only of length N that can be formed with at-most K contiguous vowels. 

Example 1:
Input: N = 2, K = 0
Output: 441
Explanation: Total of 441 unique words are possible of length 2 that will have K( =0) 
vowels together, e.g. "bc", "cd", "df", etc are valid words while "ab" (with 1 vowel) is not a valid word.

Example 2:
Input: N = 1, K = 1
Output: 26
Explanation: All the english alphabets including vowels and consonants; as atmost K( =1) vowel can be taken.
"""

class Solution:
    def kvowelwords(self, N, K):
        # Define the number of vowels and consonants
        vowels = {'a', 'e', 'i', 'o', 'u'}
        total_alphabets = 26
        consonants = total_alphabets - len(vowels)

        # Initialize a dp array
        dp = [[0] * (K + 1) for _ in range(N + 1)]
        mod = 10**9 + 7

        # Base case: If length is 0, there's one empty string
        dp[0][0] = 1

        # Fill the dp array
        for i in range(1, N + 1):
            for j in range(K + 1):
                # Add words ending with a consonant
                dp[i][0] = (dp[i][0] + dp[i - 1][j] * consonants) % mod
                
                # Add words ending with a vowel (only if j > 0)
                if j > 0:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - 1] * len(vowels)) % mod

        # Calculate the total number of words
        result = 0
        for j in range(K + 1):
            result = (result + dp[N][j]) % mod

        return result

solution = Solution()
print(solution.kvowelwords(2, 0))  # Output: 441
print(solution.kvowelwords(1, 1))  # Output: 26
print(solution.kvowelwords(3, 1))  # Output depends on constraints

'''
Here's the detailed breakdown:

class Solution:
A class named Solution encapsulates the solution method.

def kvowelwords(self, N, K):
A function to compute the desired result, where: N: Total length of the words. K: Maximum allowed consecutive vowels.

vowels = {'a', 'e', 'i', 'o', 'u'}
A set containing the vowels in the English alphabet.

total_alphabets = 26
Total number of letters in the English alphabet.

consonants = total_alphabets - len(vowels)
Number of consonants, calculated as 26 - 5 = 21.

dp = [[0] * (K + 1) for _ in range(N + 1)]
A 2D DP table:
dp[i][j] represents the number of valid words of length i with at most j consecutive vowels.

mod = 10**9 + 7
A large prime modulus is used to prevent overflow and ensure results fit within standard integer sizes.

dp[0][0] = 1
Base case: For length 0, there's exactly one empty string.

Outer loop for i in range(1, N + 1):
Iterate through word lengths from 1 to N.

Inner loop for j in range(K + 1):
Iterate through possible counts of consecutive vowels, o to K.

dp[i][0] = (dp[i][0] + dp[i - 1][j] * consonants) % mod
Add words of length i- 1 with j consecutive vowels, extended by a consonant.
This ensures the count of consecutive vowels resets to 0.

if j > 0:
Words of length i ending in a vowel are valid only if j>0.

dp[i][j] = (dp[i][j] + dp[i - 1][j - 1] * len(vowels)) % mod
Add words of length i - 1 with j - 1 consecutive vowels, extended by another vowel.

result = 0
Initialize the result to zero.

for j in range(K + 1):
Sum up all valid words of length N that have at most K consecutive vowels.

result = (result + dp[N][j]) % mod
Accumulate results for all j and take modulus.

return result
The final result is the total count of valid words.

print(solution.kvowelwords(2, 0)) # Output: 441
For words of length 2 with no consecutive vowels:
21 * 21 = 441.

print(solution.kvowelwords(1, 1)) # Output: 26
For words of length 1 with at most 1 consecutive vowel:
21 consonants + 5 vowels = 26.

print(solution.kvowelwords(3, 1))
Computes valid words for length 3 and at most 1 consecutive vowel based on the DP table.
'''