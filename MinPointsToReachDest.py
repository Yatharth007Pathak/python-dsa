"""
Given a m*n grid with each cell consisting of a positive, negative, or zero integer. We can move across a cell only if we have positive points. 
Whenever we pass through a cell, points in that cell are added to our overall points, 
the task is to find minimum initial points to reach cell (m-1, n-1) from (0, 0) by following these certain set of rules :
1. From a cell (i, j) we can move to (i + 1, j) or (i, j + 1).
2. We cannot move from (i, j) if your overall points at (i, j) are <= 0.
3. We have to reach at (n-1, m-1) with minimum positive points i.e., > 0.

Example 1:
Input: m = 3, n = 3 
points = {{-2,-3,3}, 
          {-5,-10,1},
          {10,30,-5}} 
Output: 7 
Explanation: 7 is the minimum value to reach the destination with positive throughout the path. Below is the path. 
(0,0) -> (0,1) -> (0,2) -> (1, 2) -> (2, 2) We start from (0, 0) with 7, we reach (0, 1) with 5, (0, 2) with 2, 
(1, 2) with 5, (2, 2) with and finally we have 1 point (we needed greater than 0 points at the end).

Example 2:
Input: m = 3, n = 2
points = {{2,3},  
          {5,10},  
          {10,30}} 
Output: 1 
Explanation: Take any path, all of them are positive. So, required one point at the start
"""

class Solution:
    def minPoints(self, m, n, points):
        # Create a 2D DP array initialized with 0
        dp = [[0 for _ in range(n)] for _ in range(m)]

        # Base case: minimum points needed to reach the destination cell itself
        dp[m-1][n-1] = max(1, 1 - points[m-1][n-1])

        # Fill the last row from right to left
        for j in range(n-2, -1, -1):
            dp[m-1][j] = max(1, dp[m-1][j+1] - points[m-1][j])

        # Fill the last column from bottom to top
        for i in range(m-2, -1, -1):
            dp[i][n-1] = max(1, dp[i+1][n-1] - points[i][n-1])

        # Fill the rest of the DP table in reverse order
        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                min_points_on_exit = min(dp[i+1][j], dp[i][j+1])
                dp[i][j] = max(1, min_points_on_exit - points[i][j])

        # The starting point value in dp[0][0] gives the minimum initial points required
        return dp[0][0]

sol = Solution()
print(sol.minPoints(3, 3, [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]))  # Output: 7
print(sol.minPoints(3, 2, [[2, 3], [5, 10], [10, 30]]))                # Output: 1

'''
Here's a breakdown of each line of the code in simple terms:

class Solution:
Defines a class called Solution which groups the function to calculate the minimum points needed.

def minPoints(self, m, n, points):
Defines a method called minPoints within the Solution class. This method takes four parameters:

self: refers to the instance of the class.
m: number of rows in the grid.
n: number of columns in the grid.
points: a 2D list where each cell has a number, representing either a point gain or a point loss.
dp = [[0 for _ in range(n)] for _ in range(m)]
Initializes a 2D list (matrix) dp of dimensions m x n, filled with zeroes. 
This matrix will be used to keep track of the minimum points needed to reach each cell.

dp[m-1][n-1] = max(1, 1 - points[m-1][n-1])
Sets the minimum points needed to reach the destination cell (bottom-right corner of the grid). 
It takes the maximum between 1 and 1 - points[m-1][n-1] to ensure that the minimum value in dp is always at least 1.

for j in range(n-2, -1, -1):
Loops through the last row of the grid from right to left, starting at the second-last column (n-2) and moving left to column 0.

dp[m-1][j] = max(1, dp[m-1][j+1] - points[m-1][j])
For each cell in the last row, calculates the minimum points required by checking the cell to its right (dp[m-1][j+1]) 
and adjusting for the points in points[m-1][j]. Again, it ensures the result is at least 1.

for i in range(m-2, -1, -1):
Loops through the last column of the grid from bottom to top, starting at the second-last row (m-2) and moving up to row 0.

dp[i][n-1] = max(1, dp[i+1][n-1] - points[i][n-1])
For each cell in the last column, calculates the minimum points required by checking the cell directly below it (dp[i+1][n-1]). 
Ensures the result is at least 1.

for i in range(m-2, -1, -1):
Loops from the second-last row up to the first row to fill in the rest of the grid.

for j in range(n-2, -1, -1):
For each row, loops from the second-last column to the first column to fill in each cell from bottom-right to top-left.

min_points_on_exit = min(dp[i+1][j], dp[i][j+1])
Calculates the minimum points needed to exit the current cell by choosing the lesser value between moving right (dp[i][j+1]) 
or moving down (dp[i+1][j]).

dp[i][j] = max(1, min_points_on_exit - points[i][j])
Sets the minimum points needed for the current cell, making sure the result is at least 1.

return dp[0][0]
Returns the minimum initial points needed to reach the destination starting from the top-left cell (dp[0][0]).

sol = Solution()
Creates an instance of the Solution class called sol.

print(sol.minPoints(3, 3, [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]))
Calls the minPoints method with a 3x3 grid and prints the result, which should be 7 for this input.

print(sol.minPoints(3, 2, [[2, 3], [5, 10], [10, 30]]))
Calls the minPoints method with a 3x2 grid and prints the result, which should be 1 for this input.
'''