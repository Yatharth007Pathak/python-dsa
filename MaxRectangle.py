"""
Given a binary matrix mat[][] of size n * m. Find the maximum area of a rectangle formed only of 1s in the given matrix.

Examples:

Input: mat[][] = [[0, 1, 1, 0],
                [1, 1, 1, 1],
                [1, 1, 1, 1],
                [1, 1, 0, 0]]
Output: 8
Explanation: The largest rectangle with only 1's is from (1, 0) to (2, 3) which is
[1, 1, 1, 1]
[1, 1, 1, 1]
and area is 4 *2 = 8.

Input: mat[][] = [[0, 1, 1],
                [1, 1, 1],
                [0, 1, 1]]
Output: 6
Explanation: The largest rectangle with only 1's is from (0, 1) to (2, 2) which is
[1, 1]
[1, 1]
[1, 1]
"""

class Solution:
    def maxArea(self, mat):
        if not mat or not mat[0]:
            return 0
        
        n, m = len(mat), len(mat[0])
        
        # Function to compute the largest area in a histogram
        def largestHistogramArea(heights):
            stack = []
            max_area = 0
            n = len(heights)
            
            for i in range(n + 1):
                # Add a zero at the end for convenience
                current_height = heights[i] if i < n else 0
                while stack and heights[stack[-1]] > current_height:
                    h = heights[stack.pop()]
                    w = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(i)
            
            return max_area
        
        # Initialize the height array for the histogram
        height = [0] * m
        max_rectangle_area = 0
        
        for i in range(n):
            for j in range(m):
                # Update the height if the cell is 1, reset it to 0 otherwise
                height[j] = height[j] + 1 if mat[i][j] == 1 else 0
            
            # Compute the largest rectangle area for this row's histogram
            max_rectangle_area = max(max_rectangle_area, largestHistogramArea(height))
        
        return max_rectangle_area

# Examples
solution = Solution()

mat1 = [[0, 1, 1, 0],
        [1, 1, 1, 1],
        [1, 1, 1, 1],
        [1, 1, 0, 0]]

mat2 = [[0, 1, 1],
        [1, 1, 1],
        [0, 1, 1]]

print(solution.maxArea(mat1))  # Output: 8
print(solution.maxArea(mat2))  # Output: 6

'''
Here's a plain-text line-by-line breakdown of the code:

Function Overview

class Solution:
Defines a class Solution that contains the method maxArea.

def maxArea(self, mat):
Defines the maxArea method to compute the largest rectangle of 1s in a binary matrix.

if not mat or not mat[0]:
Checks if the matrix is empty or has no rows/columns. Returns 0 if true.

return 0
Returns 0 because no area can exist in an empty matrix.

n, m = len(mat), len(mat[0])
Stores the number of rows (n) and columns (m) of the matrix.

Helper Function to Find the Largest Area in a Histogram

def largestHistogramArea(heights):
Defines a helper function to compute the largest rectangular area in a histogram.

stack = []
Initializes an empty stack to store indices of the histogram bars.

max_area = 0
Initializes max_area to keep track of the largest rectangle area.

n = len(heights)
Stores the length of the heights array.

for i in range(n + 1):
Loops through the histogram, including one extra iteration to handle trailing elements.

current_height = heights[i] if i < n else 0
Sets current_height to the current bar's height or 0 for the extra iteration.

while stack and heights[stack[-1]] > current_height:
Pops elements from the stack while the top of the stack represents a bar taller than current_height.

h = heights[stack.pop()]
Stores the height of the bar being popped.

w = i if not stack else i - stack[-1] - 1
Computes the width of the rectangle formed by the popped bar.

If the stack is empty, the width spans the entire histogram up to i.
Otherwise, the width is the distance between the current index (i) and the next smaller bar in the stack.
max_area = max(max_area, h * w)
Updates max_area by calculating the rectangle's area (h * w).

stack.append(i)
Pushes the current index onto the stack.

return max_area
Returns the largest area found in the histogram.

Main Function Logic
height = [0] * m
Initializes a list height of size m to store the histogram heights for each column.

max_rectangle_area = 0
Initializes max_rectangle_area to track the largest rectangle found.

for i in range(n):
Loops through each row of the matrix.

for j in range(m):
Loops through each column of the current row.

height[j] = height[j] + 1 if mat[i][j] == 1 else 0
Updates the histogram height for each column:

If the current cell is 1, increments the height.
Otherwise, resets the height to 0.
max_rectangle_area = max(max_rectangle_area, largestHistogramArea(height))
Calculates the maximum rectangle area for the updated histogram using the helper function and updates max_rectangle_area.

return max_rectangle_area
Returns the largest rectangle area found in the matrix.

Test Cases

solution = Solution()
Creates an instance of the Solution class.

mat1 = [[0, 1, 1, 0], ... ]
Defines a binary matrix mat1 with a mix of 1s and 0s.

mat2 = [[0, 1, 1], ... ]
Defines another binary matrix mat2.

print(solution.maxArea(mat1))
Calls maxArea with mat1 and prints the result. Output: 8.

print(solution.maxArea(mat2))
Calls maxArea with mat2 and prints the result. Output: 6.
'''