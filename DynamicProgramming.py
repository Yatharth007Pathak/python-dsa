"""
Given a street of N houses (a row of houses), each house having K amount of money kept inside; 
now there is a thief who is going to steal this money but he has a constraint/rule that he cannot steal/rob two adjacent houses. 
Find the maximum money he can rob.

Example 1:
Input: N = 5 , K = 10
Output: 30
Explanation: The Robber can rob from the first, third and fifth houses which will result in 30. 

Example 2:
Input: N = 2 , K = 12
Output: 12
Explanation: The Robber can only rob from the first or second which will result in 12.
"""

class Solution:
    def maximizeMoney(self, N, K):
        if N == 0:
            return 0
        if N == 1:
            return K
        
        # Initialize dp array
        dp = [0] * N
        dp[0] = K
        dp[1] = max(K, K)
        
        for i in range(2, N):
            dp[i] = max(dp[i-1], dp[i-2] + K)
        
        return dp[N-1]

sol = Solution()
print(sol.maximizeMoney(5, 10))  # Output: 30
print(sol.maximizeMoney(2, 12))  # Output: 12

'''

To solve the problem where a thief cannot rob two adjacent houses but wants to maximize the money stolen, 
you can use a dynamic programming approach.

Explanation:

Base Cases:
If there are no houses (N == 0), the maximum money is 0.
If there is only one house (N == 1), the thief can only rob that house, so the maximum money is K.

DP Array Initialization:
dp[0] is K because with one house, the maximum money is K.
dp[1] is max(K, K) because with two houses, the maximum money is the maximum of robbing either house.

DP Transition:
For each house from index 2 to N-1, update dp[i] to be the maximum of either skipping the house or robbing it 
(considering the previous non-adjacent house).

Return Result:
The result is stored in dp[N-1], which gives the maximum money robbed from all N houses.


Code Breakdown:
class Solution:
This defines a class named Solution, which contains the method maximizeMoney.

def maximizeMoney(self, N, K):
This defines the method maximizeMoney, which takes two parameters: 
N (the number of days) and K (the amount of money that can be earned each day).

if N == 0:
This checks if N is 0, which means there are no days to collect money. In this case, the function returns 0.

if N == 1:
This checks if N is 1, meaning there is only one day to collect money. 
If so, the function returns K, the amount that can be collected in one day.

dp = [0] * N
Initializes a list dp of length N with all elements set to 0. 
This list will be used to store the maximum money that can be collected up to each day.

dp[0] = K
Sets the value for the first day (dp[0]) to K, as you can collect K on the first day.

dp[1] = max(K, K)
This line seems redundant because max(K, K) is always K. It sets the value for the second day (dp[1]) to K. 
This is effectively saying that the maximum money you can collect in two days is just K, 
which is misleading since you should be able to choose between not taking money on one of the days or taking it on both days. 
This might be a mistake in the code.

for i in range(2, N):
This loop iterates from day 2 to day N-1. The purpose is to fill the dp list with the maximum money that can be collected up to each day.

dp[i] = max(dp[i-1], dp[i-2] + K)
For each day i, the maximum money that can be collected is either:

The same as the previous day (dp[i-1]), which means not taking money on day i.
The money collected up to two days before plus K (dp[i-2] + K), which means taking money on day i.
return dp[N-1]
Returns the maximum money that can be collected by the end of day N-1.

Example Usage:
sol = Solution()
Creates an instance of the Solution class named sol.

print(sol.maximizeMoney(5, 10))

For N = 5 and K = 10, the function calculates:
dp[0] = 10 (1st day)
dp[1] = 10 (2nd day)
dp[2] = max(10, 10 + 10) = 20 (3rd day)
dp[3] = max(20, 10 + 10) = 20 (4th day)
dp[4] = max(20, 20 + 10) = 30 (5th day)
The output is 30.
print(sol.maximizeMoney(2, 12))

For N = 2 and K = 12, the function calculates:
dp[0] = 12 (1st day)
dp[1] = 12 (2nd day)
The output is 12, which indicates that in the context of this function's logic, taking the money on only one of the two days is optimal.
Summary:
'''
