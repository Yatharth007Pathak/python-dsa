"""
Given a gold mine called M of (n x m) dimensions. Each field in this mine contains a positive integer which is the amount of gold in tons. 
Initially the miner can start from any row in the first column. From a given cell, the miner can move

to the cell diagonally up towards the right 
to the right
to the cell diagonally down towards the right

Find out maximum amount of gold which he can collect until he can no longer move.

Example 1:

Input: n = 3, m = 3
M = {{1, 3, 3},
     {2, 1, 4},
     {0, 6, 4}};
Output: 12
Explaination: The path is {(1,0) -> (2,1) -> (2,2)}.

Example 2:

Input: n = 4, m = 4
M = {{1, 3, 1, 5},
     {2, 2, 4, 1},
     {5, 0, 2, 3},
     {0, 6, 1, 2}};
Output: 16
Explaination: The path is {(2,0) -> (3,1) -> (2,2) -> (2,3)} or {(2,0) -> (1,1) -> (1,2) -> (0,3)}.
"""

class Solution:
    def maxGold(self, n, m, M):
        # Create a DP table initialized with zeros
        dp = [[0] * m for _ in range(n)]
        
        # Start from the last column and work backward
        for col in range(m - 1, -1, -1):
            for row in range(n):
                # If the miner goes right
                right = dp[row][col + 1] if col < m - 1 else 0
                
                # If the miner goes right-up
                right_up = dp[row - 1][col + 1] if row > 0 and col < m - 1 else 0
                
                # If the miner goes right-down
                right_down = dp[row + 1][col + 1] if row < n - 1 and col < m - 1 else 0
                
                # Calculate max gold for current cell
                dp[row][col] = M[row][col] + max(right, right_up, right_down)
        
        # The answer is the maximum gold collected from any row in the first column
        return max(dp[row][0] for row in range(n))

# Example Usage
solution = Solution()
n, m = 3, 3
M = [[1, 3, 3], [2, 1, 4], [0, 6, 4]]
print(solution.maxGold(n, m, M))  # Output: 12

n, m = 4, 4
M = [[1, 3, 1, 5], [2, 2, 4, 1], [5, 0, 2, 3], [0, 6, 1, 2]]
print(solution.maxGold(n, m, M))  # Output: 16

'''
Solution Explanation:

Dynamic Programming Table (DP):
Create a 2D dp table of the same dimensions as the grid M.
dp[row][col] stores the maximum gold that can be collected starting from cell (row, col) and moving to the right.

Initialization:
Start from the last column of the grid and work backward towards the first column.

Transition Formula:
For each cell (row, col), compute the maximum gold that can be collected considering all three possible moves:
Right: dp[row][col + 1]
Right-Up: dp[row - 1][col + 1] (if row > 0)
Right-Down: dp[row + 1][col + 1] (if row < n - 1)
Update dp[row][col] as: dp[row][col] = M[row][col] + max(right, right-up, right-down)

Final Answer:
The maximum gold collected will be the maximum value in the first column (dp[row][0] for all rows).

Code Walkthrough:
Input Grid: M = [[1, 3, 3], [2, 1, 4], [0, 6, 4]], n = 3, m = 3 (grid dimensions)

DP Table Construction:
Start from the last column and move left.
Update dp using the transition formula for each cell.

Output: For M = [[1, 3, 3], [2, 1, 4], [0, 6, 4]], the DP table will look like this:
[12, 8, 3]
[12, 8, 4]
[10, 10, 4]
The maximum gold collected is max(dp[row][0]) = 12.

Example Runs:
Input 1: n, m = 3, 3
M = [[1, 3, 3], [2, 1, 4], [0, 6, 4]]
Output: 12

Input 2: n, m = 4, 4
M = [[1, 3, 1, 5], [2, 2, 4, 1], [5, 0, 2, 3], [0, 6, 1, 2]]
Output: 16
'''