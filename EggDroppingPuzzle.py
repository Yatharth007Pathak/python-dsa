"""
You are given n identical eggs and you have access to a k-floored building from 1 to k.

There exists a floor f where 0 <= f <= k such that any egg dropped from a floor higher than f will break, 
and any egg dropped from or below floor f will not break.
There are  few rules given below. 

An egg that survives a fall can be used again.
A broken egg must be discarded.
The effect of a fall is the same for all eggs.
If the egg doesn't break at a certain floor, it will not break at any floor below.
If the egg breaks on a certain floor, it will break on any floor above.
Return the minimum number of moves you need to determine the value of f with certainty.

Examples:

Input: n = 1, k = 2
Output: 2
Explanation: Drop the egg from floor 1. If it breaks, we know that f = 0. Otherwise, drop the egg from floor 2. 
If it breaks, we know that f = 1.  If it does not break, then we know f = 2. 
Hence, we need at minimum 2 moves to determine with certainty what the value of f is.

Input: n = 10, k = 5
Output: 3
Explanation: Drop the egg from floor 2. If it breaks, test floor 1 with a remaining egg. 
If it doesn't break, drop from floor 4. If it breaks, test floor 3. 
If it still doesn't break, we know the critical floor is 5.Hence, with a minimum of 3 moves, we can find the critical floor.

Input: n = 2, k = 10
Output: 4
Explanation: Drop the egg from floor 4. If it breaks, we only need to test floors 1 to 3 with the remaining egg. 
If it doesn't break, drop the egg from floor 7. If it breaks, we only need to test floors 5 and 6. 
If it doesn't break again, drop the egg from floor 9. If it breaks, test floor 8. If it still doesn't break, we know the critical floor is 10. 
Hence, with a minimum of 4 moves, we can determine the critical floor.
"""

class Solution:
    def eggDrop(self, n, k):
        # Initialize dp table where dp[i][j] represents the minimum moves with i eggs and j floors
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        
        # Base cases: 1 egg scenario and 0 floors
        for j in range(1, k + 1):
            dp[1][j] = j  # With 1 egg, j moves are needed for j floors
        
        # Fill the table for more than 1 egg
        for i in range(2, n + 1):  # i eggs
            for j in range(1, k + 1):  # j floors
                dp[i][j] = float('inf')
                # Calculate minimum moves by choosing optimal floor x
                for x in range(1, j + 1):
                    moves = 1 + max(dp[i-1][x-1], dp[i][j-x])
                    dp[i][j] = min(dp[i][j], moves)

        # Return the result stored in dp[n][k]
        return dp[n][k]

# Example usage
solution = Solution()
print(solution.eggDrop(1, 2))  # Output: 2
print(solution.eggDrop(10, 5))  # Output: 3
print(solution.eggDrop(2, 10))  # Output: 4

'''
Here's a line-by-line breakdown of the code:

class Solution:
Defines a class named Solution.

def eggDrop(self, n, k):
Defines a method within the Solution class called eggDrop. It takes in three parameters: 
self (the instance of the class), n (the number of eggs), and k (the number of floors).

dp = [[0] * (k + 1) for _ in range(n + 1)]
Initializes a 2D list dp with dimensions (n + 1) x (k + 1) filled with zeros. 
Here, dp[i][j] will store the minimum moves needed with i eggs and j floors.

for j in range(1, k + 1):
Starts a loop to handle the base case where only one egg is available.

dp[1][j] = j
For the base case where only one egg is available, assigns j moves for j floors 
(we need to drop the egg from each floor one by one to find the critical floor).

for i in range(2, n + 1):
Starts an outer loop over the number of eggs, beginning with 2, to fill in dp for scenarios with more than one egg.

for j in range(1, k + 1):
Starts an inner loop over the number of floors to determine the minimum moves needed for each (i, j) combination.

dp[i][j] = float('inf')
Sets dp[i][j] to infinity to initialize the minimum search process for i eggs and j floors.

for x in range(1, j + 1):
Starts another loop to simulate dropping the egg from each floor x from 1 to j. 
This loop evaluates all possible floors to find the minimum moves for the worst-case scenario.

moves = 1 + max(dp[i-1][x-1], dp[i][j-x])
Calculates the number of moves required if the egg is dropped from floor x. 
It adds 1 move for the current drop, and takes the maximum of two cases:

If the egg breaks (dp[i-1][x-1]), meaning we have i-1 eggs and x-1 floors left to test.
If the egg doesn’t break (dp[i][j-x]), meaning we still have i eggs and j-x floors left to test. 
This max accounts for the worst-case scenario, as we need the highest of both cases.
dp[i][j] = min(dp[i][j], moves)
Updates dp[i][j] with the minimum moves found so far for i eggs and j floors.

return dp[n][k]
Returns the minimum number of moves needed with n eggs and k floors, stored in dp[n][k].

Example Usage:
solution = Solution()
Creates an instance of the Solution class named solution.

print(solution.eggDrop(1, 2)) # Output: 2
Calls eggDrop with 1 egg and 2 floors. The output 2 is printed, representing the minimum moves required.

print(solution.eggDrop(10, 5)) # Output: 3
Calls eggDrop with 10 eggs and 5 floors. The output 3 is printed.

print(solution.eggDrop(2, 10)) # Output: 4
Calls eggDrop with 2 eggs and 10 floors. The output 4 is printed.

Complexity Analysis
Time Complexity: O(n*k^2) because for each pair (i, j), we are iterating through all floors up to j.
Space Complexity: O(n*k) for the DP table.
'''