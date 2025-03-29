"""
You are given a rectangular matrix, and your task is to return an array while traversing the matrix in spiral form.

Examples:

Input: mat[][] = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15,16]]
Output: [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]

Input: mat[][] = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
Output: [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]

Input: mat[][] = [[32, 44, 27, 23], [54, 28, 50, 62]]
Output: [32, 44, 27, 23, 62, 50, 28, 54]
"""

class Solution:
    def spirallyTraverse(self, mat):
        if not mat or not mat[0]:
            return []
        
        result = []
        top, bottom = 0, len(mat) - 1
        left, right = 0, len(mat[0]) - 1
        
        while top <= bottom and left <= right:
            # Traverse from left to right along the top boundary
            for i in range(left, right + 1):
                result.append(mat[top][i])
            top += 1
            
            # Traverse from top to bottom along the right boundary
            for i in range(top, bottom + 1):
                result.append(mat[i][right])
            right -= 1
            
            # Traverse from right to left along the bottom boundary
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(mat[bottom][i])
                bottom -= 1
            
            # Traverse from bottom to top along the left boundary
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(mat[i][left])
                left += 1
        
        return result

# Example usage:
solution = Solution()
print(solution.spirallyTraverse([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15,16]]))
# Output: [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]

print(solution.spirallyTraverse([[32, 44, 27, 23], [54, 28, 50, 62]]))
# Output: [32, 44, 27, 23, 62, 50, 28, 54]

'''
Here's a line-by-line breakdown of the code:

class Solution:
Defines a class named Solution containing a method to traverse a matrix in a spiral order.

def spirallyTraverse(self, mat):
Defines a method spirallyTraverse within the Solution class. 
It takes self (instance of the class) and mat (the matrix to traverse) as parameters.

if not mat or not mat[0]:
Checks if mat is empty or if it has no columns. This handles cases with an empty matrix or an empty row.

return []
Returns an empty list if the matrix is empty.

result = []
Initializes an empty list result to store the elements in spiral order.

top, bottom = 0, len(mat) - 1
Sets the top boundary to the first row and bottom boundary to the last row of the matrix.

left, right = 0, len(mat[0]) - 1
Sets the left boundary to the first column and right boundary to the last column of the matrix.

while top <= bottom and left <= right:
Enters a loop that continues as long as top is less than or equal to bottom and left is less than or equal to right. 
This ensures the traversal remains within the matrix boundaries.

for i in range(left, right + 1):
Traverses from the left to the right boundary along the top row.

result.append(mat[top][i])
Appends each element in the top row to result.

top += 1
Moves the top boundary down by one row after finishing the traversal along the top row.

for i in range(top, bottom + 1):
Traverses from the top to the bottom boundary along the right column.

result.append(mat[i][right])
Appends each element in the right column to result.

right -= 1
Moves the right boundary left by one column after finishing the traversal along the right column.

if top <= bottom:
Checks if the top boundary is still within bottom to ensure there are rows left to traverse at the bottom.

for i in range(right, left - 1, -1):
Traverses from the right to the left boundary along the bottom row.

result.append(mat[bottom][i])
Appends each element in the bottom row to result.

bottom -= 1
Moves the bottom boundary up by one row after finishing the traversal along the bottom row.

if left <= right:
Checks if the left boundary is still within right to ensure there are columns left to traverse at the left.

for i in range(bottom, top - 1, -1):
Traverses from the bottom to the top boundary along the left column.

result.append(mat[i][left])
Appends each element in the left column to result.

left += 1
Moves the left boundary right by one column after finishing the traversal along the left column.

return result
Returns result, which now contains the matrix elements in spiral order.

Example Usage:
solution = Solution()
Creates an instance of the Solution class named solution.

print(solution.spirallyTraverse([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15,16]]))
Calls spirallyTraverse on a 4x4 matrix and prints the result. The expected output is [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10].

print(solution.spirallyTraverse([[32, 44, 27, 23], [54, 28, 50, 62]]))
Calls spirallyTraverse on a 2x4 matrix and prints the result. The expected output is [32, 44, 27, 23, 62, 50, 28, 54].

Complexity Analysis
Time Complexity: O(m*n), where m is the number of rows and n is the number of columns, as each element is visited once.
Space Complexity: O(1), if we ignore the output list; otherwise, O(m*n) for storing the traversal result.
'''