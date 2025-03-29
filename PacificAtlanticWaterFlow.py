"""
You are given a matrix mat[][] of dimensions n x m, where mat[i][j] represents the height of a cell in a rectangular grid island. 
The Pacific Ocean touches the island's left and top borders, and the Atlantic Ocean touches the island's right and bottom borders. 
Rainwater can flow from a cell to its neighbouring cells in the directions North, South, East, and West, 
but only if the neighbouring cell has a height less than or equal to the current cell's height.

The task is to determine all coordinates (x, y) such that water can flow from the cell (x, y) to both the 
Pacific Ocean and the Atlantic Ocean. 
Water can flow from any adjacent cell directly into an ocean.

Examples:

Input: mat[][] = [[1, 2, 2, 3, 5],
                [3, 2, 3, 4, 4],
                [2, 4, 5, 3, 1],
                [6, 7, 1, 4, 5],
                [5, 1, 1, 2, 4]]
Output: 7
Explanation: In the given matrix, there are 7 coordinates through which the water can flow to both the lakes. 
They are  (0, 4), (1, 3), (1, 4), (2, 2), (3, 0), (3, 1), and (4, 0).

Input: arr[][] = [[2, 2], 
               [2, 2]]
Output: 4
Explanation: In the following example, all cells allow water to flow to both the lakes.
"""

from collections import deque

class Solution:
    def countCoordinates(self, mat):
        if not mat or not mat[0]:
            return 0
        
        n, m = len(mat), len(mat[0])
        pacific = [[False for _ in range(m)] for _ in range(n)]
        atlantic = [[False for _ in range(m)] for _ in range(n)]
        
        def dfs(x, y, ocean):
            ocean[x][y] = True
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m and not ocean[nx][ny] and mat[nx][ny] >= mat[x][y]:
                    dfs(nx, ny, ocean)
        
        # Perform DFS from Pacific and Atlantic borders
        for i in range(n):
            dfs(i, 0, pacific)  # Pacific left column
            dfs(i, m - 1, atlantic)  # Atlantic right column
        for j in range(m):
            dfs(0, j, pacific)  # Pacific top row
            dfs(n - 1, j, atlantic)  # Atlantic bottom row
        
        # Count cells reachable by both oceans
        count = 0
        for i in range(n):
            for j in range(m):
                if pacific[i][j] and atlantic[i][j]:
                    count += 1
        
        return count

sol = Solution()

mat = [[1, 2, 2, 3, 5],
       [3, 2, 3, 4, 4],
       [2, 4, 5, 3, 1],
       [6, 7, 1, 4, 5],
       [5, 1, 1, 2, 4]]
print(sol.countCoordinates(mat))  # Output: 7

mat = [[2, 2], 
       [2, 2]]
print(sol.countCoordinates(mat))  # Output: 4

'''
Line-by-Line Explanation

from collections import deque
Imports deque from the collections module. However, deque is not used in this code, so this line is redundant.

class Solution:
Defines a class named Solution.

def countCoordinates(self, mat):
Defines a method countCoordinates that takes a 2D grid mat as input and calculates the 
number of coordinates that can flow water to both the Pacific and Atlantic oceans.

if not mat or not mat[0]:
Checks if the input mat is empty or if the first row is empty. If so, there is no valid input, so the function returns 0.

return 0
Returns 0 if the input matrix is invalid.

n, m = len(mat), len(mat[0])
Stores the number of rows (n) and columns (m) in the matrix mat.

pacific = [[False for _ in range(m)] for _ in range(n)]
Creates a 2D boolean matrix pacific of size n x m, initialized to False. This matrix tracks whether a cell can flow water to the Pacific Ocean.

atlantic = [[False for _ in range(m)] for _ in range(n)]
Similarly, creates a 2D boolean matrix atlantic to track whether a cell can flow water to the Atlantic Ocean.

Depth-First Search (DFS) Function
def dfs(x, y, ocean):
Defines a helper function dfs that performs a depth-first search to mark all reachable cells from a starting cell (x, y).

ocean[x][y] = True
Marks the current cell (x, y) as reachable in the ocean matrix.

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
Defines the possible directions of movement: up, down, left, and right.

for dx, dy in directions:
Iterates over all possible directions.

nx, ny = x + dx, y + dy
Calculates the coordinates of the next cell (nx, ny).

if 0 <= nx < n and 0 <= ny < m and not ocean[nx][ny] and mat[nx][ny] >= mat[x][y]:
Checks if the next cell (nx, ny) is within bounds, has not been visited, and has a height greater than or equal to the current cell (x, y).

dfs(nx, ny, ocean)
Recursively performs a DFS from the next cell (nx, ny).

DFS from Pacific and Atlantic Borders
for i in range(n):
Loops over all rows to initiate DFS from the Pacific (left column) and Atlantic (right column) borders.

dfs(i, 0, pacific)
Performs DFS from the Pacific left column.

dfs(i, m - 1, atlantic)
Performs DFS from the Atlantic right column.

for j in range(m):
Loops over all columns to initiate DFS from the Pacific (top row) and Atlantic (bottom row) borders.

dfs(0, j, pacific)
Performs DFS from the Pacific top row.

dfs(n - 1, j, atlantic)
Performs DFS from the Atlantic bottom row.

Count Coordinates Reachable by Both Oceans
count = 0
Initializes a variable count to store the number of cells reachable by both oceans.

for i in range(n):
Iterates over all rows.

for j in range(m):
Iterates over all columns.

if pacific[i][j] and atlantic[i][j]:
Checks if the cell (i, j) is reachable by both the Pacific and Atlantic oceans.

count += 1
Increments the count if the condition is satisfied.

return count
Returns the final count of cells reachable by both oceans.

Example Usage

sol = Solution()
Creates an instance of the Solution class.

mat = [[1, 2, 2, 3, 5], ...]
Defines a matrix mat as the input.

print(sol.countCoordinates(mat))
Prints the number of cells in mat reachable by both oceans. The output is 7.

mat = [[2, 2], [2, 2]]
Defines another matrix mat as input.

print(sol.countCoordinates(mat))
Prints the output for the second test case, which is 4.

Explanation of Outputs
In the first example, 7 cells can flow water to both the Pacific and Atlantic oceans.
In the second example, all 4 cells can flow water to both oceans due to uniform height.
'''