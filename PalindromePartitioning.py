"""
Given a string s, a partitioning of the string is a palindrome partitioning if every sub-string of the partition is a palindrome. 
Determine the fewest cuts needed for palindrome partitioning of the given string.

Examples:

Input: s = "ababbbabbababa"
Output: 3
Explaination: After 3 partitioning substrings are "a", "babbbab", "b", "ababa".

Input: s = "aaabba"
Output: 1
Explaination: The substrings after 1 partitioning are "aa" and "abba".

Input: s = "aaa"
Output: 0
Explaination: No partitioning is required.
"""

class Solution:
    def palindromicPartition(self, s: str) -> int:
        n = len(s)
        # Step 1: Precompute palindrome information
        is_palindrome = [[False] * n for _ in range(n)]
        
        for i in range(n):
            is_palindrome[i][i] = True  # Single character is a palindrome
        
        for length in range(2, n + 1):  # Check substrings of increasing length
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    if length == 2:
                        is_palindrome[i][j] = True
                    else:
                        is_palindrome[i][j] = is_palindrome[i + 1][j - 1]
        
        # Step 2: DP to compute minimum cuts
        dp = [0] * n
        for i in range(n - 1, -1, -1):
            if is_palindrome[i][n - 1]:  # No cuts needed
                dp[i] = 0
            else:
                min_cuts = float('inf')
                for j in range(i, n):
                    if is_palindrome[i][j]:
                        min_cuts = min(min_cuts, 1 + dp[j + 1])
                dp[i] = min_cuts
        
        return dp[0]

# Example Usage
sol = Solution()
print(sol.palindromicPartition("ababbbabbababa"))  # Output: 3
print(sol.palindromicPartition("aaabba"))         # Output: 1
print(sol.palindromicPartition("aaa"))            # Output: 0

'''
Here's a step-by-step breakdown of the code:

class Solution:
Defines a class called Solution which contains the method palindromicPartition. 
This method solves the problem of finding the minimum number of cuts required to partition a string into palindromic substrings.

def palindromicPartition(self, s: str) -> int:
Defines the method palindromicPartition, which takes a string s as input and returns an integer, 
representing the minimum number of cuts required to partition the string into palindromic substrings.

n = len(s)
Computes the length n of the input string s.

is_palindrome = [[False] * n for _ in range(n)]
Creates a 2D list is_palindrome of size n x n, initialized with False. This list will store whether a substring s[i:j] is a palindrome. 
is_palindrome[i][j] will be True if the substring from index i to j is a palindrome.

for i in range(n):
Loops through each index i from 0 to n-1.

is_palindrome[i][i] = True
Sets is_palindrome[i][i] to True because any single character is always a palindrome.

for length in range(2, n + 1):
Starts a loop to check all substrings of increasing lengths from 2 to n.

for i in range(n - length + 1):
For each length of substring, it starts at index i and checks up to n - length + 1 so that the substring s[i:i+length] is within bounds.

j = i + length - 1
Calculates the end index j of the current substring of length length.

if s[i] == s[j]:
Checks if the characters at indices i and j are equal. For a substring to be a palindrome, the characters at both ends must match.

if length == 2:
If the length of the current substring is 2, the substring is a palindrome if and only if the two characters are equal. 
Therefore, is_palindrome[i][j] = True.

else:
If the length is greater than 2, the current substring is a palindrome if the characters at both ends 
are equal and the inner substring s[i+1:j-1] is also a palindrome. This is checked by is_palindrome[i + 1][j - 1].

dp = [0] * n
Creates a list dp of size n, initialized with zeros. This list will store the minimum 
cuts needed to partition the string from index i to the end.

for i in range(n - 1, -1, -1):
Starts a loop to fill the dp list from the right (from index n-1 to 0).

if is_palindrome[i][n - 1]:
Checks if the substring s[i:n] is a palindrome. If it is, no cuts are needed, and dp[i] = 0.

else:
If the substring s[i:n] is not a palindrome, it initializes a variable min_cuts to infinity.

for j in range(i, n):
Starts a loop over all possible j values (from i to n-1) to check for palindromic substrings starting from i.

if is_palindrome[i][j]:
If the substring s[i:j+1] is a palindrome, it updates min_cuts by considering one cut for the 
palindromic substring and adding the minimum cuts required for the remaining string s[j+1:n], which is stored in dp[j+1].

dp[i] = min_cuts
Assigns the minimum cuts required for the substring starting at index i to dp[i].

return dp[0]
After filling the dp array, the minimum number of cuts for the entire string is stored in dp[0]. This value is returned.

Example Usage:
sol = Solution()
Creates an instance of the Solution class called sol.

print(sol.palindromicPartition("ababbbabbababa")) # Output: 3
Calls the palindromicPartition method with the input string "ababbbabbababa" and prints the output, which is 3. 
This means 3 cuts are required to partition the string into palindromic substrings.

print(sol.palindromicPartition("aaabba")) # Output: 1
Calls the method with the input "aaabba", which requires 1 cut to form palindromic substrings, and prints 1.

print(sol.palindromicPartition("aaa")) # Output: 0
Calls the method with the input "aaa", which is already a palindrome, so no cuts are required, and it prints 0.
'''