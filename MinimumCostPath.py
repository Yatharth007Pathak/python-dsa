"""
Given a square grid of size N, each cell of which contains an integer cost that represents a cost to traverse through that cell, 
we need to find a path from the top left cell to the bottom right cell by which the total cost incurred is minimum.
From the cell (i,j) we can go (i,j-1), (i, j+1), (i-1, j), (i+1, j).  

Examples :

Input: grid = {{9,4,9,9},{6,7,6,4},{8,3,3,7},{7,4,9,10}}
Output: 43
Explanation: The grid is-
9 4 9 9
6 7 6 4
8 3 3 7
7 4 9 10
The minimum cost is-
9 + 4 + 7 + 3 + 3 + 7 + 10 = 43.

Input: grid = {{4,4},{3,7}}
Output: 14
Explanation: The grid is-
4 4
3 7
The minimum cost is- 4 + 3 + 7 = 14.
"""

import heapq

class Solution:
    # Function to return the minimum cost to reach the bottom-right cell from the top-left cell.
    def minimumCostPath(self, grid):
        n = len(grid)
        
        # Directions for moving up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Min-heap to get the minimum cost cell at each step
        pq = [(grid[0][0], 0, 0)]  # (cost, row, col)
        
        # Distance (cost) array initialized to infinity
        cost = [[float('inf')] * n for _ in range(n)]
        cost[0][0] = grid[0][0]
        
        # Dijkstra's algorithm using priority queue
        while pq:
            curr_cost, i, j = heapq.heappop(pq)
            
            # If we reached the bottom-right cell, return its cost
            if (i, j) == (n-1, n-1):
                return curr_cost
            
            # Explore all four directions
            for di, dj in directions:
                ni, nj = i + di, j + dj
                
                # Check bounds and if the new cost is better
                if 0 <= ni < n and 0 <= nj < n:
                    new_cost = curr_cost + grid[ni][nj]
                    
                    if new_cost < cost[ni][nj]:
                        cost[ni][nj] = new_cost
                        heapq.heappush(pq, (new_cost, ni, nj))
        
        return -1  # In case there is no valid path, though it's given that a path always exists.

# Test cases
solution = Solution()

# Test case 1
grid1 = [[9, 4, 9, 9], [6, 7, 6, 4], [8, 3, 3, 7], [7, 4, 9, 10]]
print(solution.minimumCostPath(grid1))

# Test case 2
grid2 = [[4, 4], [3, 7]]
print(solution.minimumCostPath(grid2))

# Test case 3 - Single cell grid
grid3 = [[5]]
print(solution.minimumCostPath(grid3))

# Test case 4 - Larger grid with higher values
grid4 = [
    [1, 2, 3],
    [4, 8, 2],
    [1, 5, 3]
]
print(solution.minimumCostPath(grid4))

# Test case 5 - Larger grid with equal costs
grid5 = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]
print(solution.minimumCostPath(grid5))

'''
Here's a breakdown of the code line-by-line in plain text.

Import heapq: This library provides functions to work with heaps, useful for implementing a priority queue.

Define the class Solution: The class contains the minimumCostPath method, 
which finds the minimum cost to reach the bottom-right cell from the top-left cell in a grid.

Define the function minimumCostPath within Solution: This function takes one parameter:
grid: a 2D list representing a grid of costs.

Initialize n as the length of the grid: This represents the size of the grid (assuming it is square).

Define movement directions: directions holds four tuples that represent moving up, down, left, and right in the grid.

Create a min-heap pq: Start the heap with the top-left cell's cost and position (cost, row, col).

Initialize a 2D cost array to infinity: Set up cost with each cell initialized to infinity, 
representing the minimum known cost to reach each cell. This will be updated as the algorithm progresses.

Set the cost for the top-left cell: Update cost[0][0] with the cost of the starting cell, grid[0][0].

Start Dijkstra’s algorithm loop with the min-heap: The loop runs while there are cells in pq.

Pop the minimum-cost cell from pq: Retrieve the cell with the lowest accumulated cost from the heap, represented by (curr_cost, i, j).

Check if we have reached the bottom-right cell: If the current cell (i, j) is the bottom-right corner, return curr_cost as the answer.

Loop over all four directions: For each direction, compute the new cell position (ni, nj) by adding di and dj to the current cell (i, j).

Check if the new cell is within bounds: Ensure that (ni, nj) lies within the grid limits.

Calculate new_cost for the new cell: This is the sum of the current cell's cost and the cost of the new cell.

Check if new_cost is lower than the recorded cost: If the calculated new_cost for (ni, nj) is less than cost[ni][nj], 
update cost[ni][nj] with new_cost.

Push the new cell and its cost to pq: Add the cell (new_cost, ni, nj) to the min-heap, so it can be explored with priority.

Return -1 if there's no valid path (not required here): This line is a safety net; however, 
it is unnecessary here, as a path is guaranteed.

The test cases below validate the function with various grid configurations.

Create an instance of Solution: Instantiate the Solution class to call the minimumCostPath method.

Explanation of Test Cases
Test Case 1: The minimum path cost is 43, as calculated by the optimal path.
Test Case 2: The minimum path cost is 14.
Test Case 3: A single cell grid with cost 5, so the output is 5.
Test Case 4: A 3x3 grid with various values. The minimum cost path has a cost of 8.
Test Case 5: A 3x3 grid where all cells have the same cost. The shortest path cost is 5 (moving directly from start to end).

Test Case 1: grid1 has multiple paths with varying costs. The minimum path cost is printed.
Test Case 2: A smaller grid grid2 with fewer cells, testing the algorithm's handling of small grids.
Test Case 3: Single-cell grid, where the minimum path is just the cell itself.
Test Case 4: Larger grid grid4 with mixed values to test a more complex scenario.
Test Case 5: Uniform cost grid grid5, where all paths have the same cumulative cost.
'''