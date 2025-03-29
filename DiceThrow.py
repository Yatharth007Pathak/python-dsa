"""
Given n dice each with m faces. Find the number of ways to get sum x which is the summation of values on each face when all the dice are thrown.

Example:

Input: m = 6, n = 3, x = 12
Output: 25
Explanation: There are 25 total ways to get the Sum 12 using 3 dices with faces from 1 to 6.

Input: m = 2, n = 3, x = 6
Output: 1
Explanation: There is only 1 way to get the Sum 6 using 3 dices with faces from 1 to 2. All the dices will have to land on 2.
"""

class Solution:
    def noOfWays(self, m, n, x):
        # dp[i][j] will be the number of ways to get sum j using i dice
        dp = [[0] * (x + 1) for _ in range(n + 1)]
        
        # Base case: There's 1 way to make sum 0 with 0 dice
        dp[0][0] = 1
        
        # Fill the dp table
        for i in range(1, n + 1):  # For each dice
            for j in range(1, x + 1):  # For each possible sum
                # Add the number of ways for each face of the dice (from 1 to m)
                dp[i][j] = sum(dp[i - 1][j - k] for k in range(1, m + 1) if j - k >= 0)
        
        # The answer is the number of ways to get sum x with n dice
        return dp[n][x]

# Example usage
solution = Solution()
print(solution.noOfWays(6, 3, 12))  # Output: 25
print(solution.noOfWays(2, 3, 6))   # Output: 1

'''
The solution to this problem uses dynamic programming (DP) to compute the number of ways to get a given sum x using n dice, 
where each die has m faces.

Approach Explanation:

DP Table Setup:
dp[i][j] represents the number of ways to obtain a sum j using exactly i dice.
Initialize the table as dp[i][j] = 0 for all i and j.

Base Case:
There's exactly 1 way to get sum 0 using 0 dice: no dice are rolled, so dp[0][0] = 1.

Filling the DP Table:
For each die (i ranging from 1 to n), and for each possible sum (j from 1 to x), calculate the number of ways to get sum j using i dice.
For each sum j, consider all possible outcomes for the current die (from 1 to m), 
and add the ways to get the remaining sum (j - k) using i - 1 dice, where k is the value of the die.

Final Answer:
The number of ways to obtain the sum x using exactly n dice is stored in dp[n][x].
Time complexity: O(n*x*m), where n is the number of dice, x is the sum, and m is the number of faces on each die.
Space complexity: O(n*x), for storing the DP table.
'''