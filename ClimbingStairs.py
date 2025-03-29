"""
There are n stairs, a person standing at the bottom wants to reach the top. The person can climb either 1 stair or 2 stairs at a time. 
Count the number of ways, the person can reach the top (order does matter).

Examples:

Input: n = 4
Output: 5
Explanation: You can reach 4th stair in 5 ways. 
Way 1: Climb 2 stairs at a time. 
Way 2: Climb 1 stair at a time.
Way 3: Climb 2 stairs, then 1 stair and then 1 stair.
Way 4: Climb 1 stair, then 2 stairs then 1 stair.
Way 5: Climb 1 stair, then 1 stair and then 2 stairs.

Input: n = 10
Output: 89 
Explanation: There are 89 ways to reach the 10th stair.
"""

class Solution:
    # Function to count number of ways to reach the nth stair.
    def countWays(self, n):
        # Base cases
        if n == 0:
            return 1
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        
        # DP array to store the number of ways to reach each stair
        dp = [0] * (n + 1)
        dp[0], dp[1], dp[2] = 1, 1, 2
        
        # Fill the dp array based on the recursive relation
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]

solution = Solution()

# Test case 1
n1 = 4
print(solution.countWays(n1))

# Test case 2
n2 = 10
print(solution.countWays(n2))

# Additional Test Cases
# Test case 3
n3 = 0
print(solution.countWays(n3))

# Test case 4
n4 = 1
print(solution.countWays(n4))

# Test case 5
n5 = 5
print(solution.countWays(n5))

'''
Explanation of countWays Function:
This function uses dynamic programming to find the number of distinct ways 
to reach the nth stair when you can take either 1 or 2 steps at a time.

Base Cases:
if n == 0: return 1 - There is only one way to stay at the ground level (do nothing).
elif n == 1: return 1 - There is only one way to reach the first stair (a single 1-step).
elif n == 2: return 2 - There are two ways to reach the second stair: take two 1-steps or one 2-step.

Initialize DP Array:
dp = [0] * (n + 1) - Creates a list dp with n+1 elements initialized to 0. 
This array will store the number of ways to reach each stair up to n.
dp[0], dp[1], dp[2] = 1, 1, 2 - Sets the base values as described in the base cases.

Fill the DP Array Using the Recursive Relation:
for i in range(3, n + 1): dp[i] = dp[i - 1] + dp[i - 2]
This loop populates the dp array from the 3rd stair to the nth stair.
The number of ways to reach the ith stair is the sum of the ways to reach the (i-1)th and (i-2)th stairs 
(since you can reach i by taking either a 1-step from i-1 or a 2-step from i-2).

Return the Result:
return dp[n] - Returns the value at dp[n], which holds the number of ways to reach the nth stair.

Test Cases:
Test Case 1: n = 4
Expected output: 5 (Ways: [1+1+1+1], [1+1+2], [1+2+1], [2+1+1], [2+2]).

Test Case 2: n = 10
Expected output: 89

Test Case 3: n = 0
Expected output: 1 (Only one way to stay on the ground).

Test Case 4: n = 1
Expected output: 1

Test Case 5: n = 5
Expected output: 8 (Ways: [1+1+1+1+1], [1+1+1+2], [1+1+2+1], [1+2+1+1], [2+1+1+1], [1+2+2], [2+1+2], [2+2+1]).
'''