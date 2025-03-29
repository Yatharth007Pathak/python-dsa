"""
Given a matrix mat[][] of size N x M, where every row and column is sorted in increasing order, and a number X is given. 
The task is to find whether element X is present in the matrix or not.


Example 1:
Input: N = 3, M = 3
mat[][] = 3 30 38 
         44 52 54 
         57 60 69
X = 62
Output: 0
Explanation: 62 is not present in the matrix, so output is 0

Example 2:
Input: N = 1, M = 6
mat[][] = 18 21 27 38 55 67
X = 55
Output: 1
Explanation: 55 is present in the matrix at 5th cell.
"""

class Solution:
    def matSearch(self, mat, N, M, X):
        # Start from the top-right corner of the matrix
        row, col = 0, M - 1
        
        while row < N and col >= 0:
            if mat[row][col] == X:
                return 1  # Element found
            elif mat[row][col] > X:
                col -= 1  # Move left
            else:
                row += 1  # Move down
        
        return 0  # Element not found

# Example usage
solution = Solution()

# Example 1
mat1 = [
    [3, 30, 38],
    [44, 52, 54],
    [57, 60, 69]
]
print(solution.matSearch(mat1, 3, 3, 62))  # Output: 0

# Example 2
mat2 = [
    [18, 21, 27, 38, 55, 67]
]
print(solution.matSearch(mat2, 1, 6, 55))  # Output: 1


'''
Explanation of the Code:

Class Definition:
class Solution:: This defines a class named Solution that contains the method for searching in the matrix.

Method Definition:
def matSearch(self, mat, N, M, X):: This method takes four parameters:
mat: The 2D matrix to search in.
N: The number of rows in the matrix.
M: The number of columns in the matrix.
X: The element to search for.

Starting Point:
row, col = 0, M - 1: Initializes the starting position at the top-right corner of the matrix.

Search Logic:
The while loop continues as long as the row index is within bounds (less than N) 
and the col index is also within bounds (greater than or equal to 0).

Condition 1: if mat[row][col] == X: If the current element is equal to X, it returns 1, indicating that the element is found.
Condition 2: elif mat[row][col] > X: If the current element is greater than X, it moves left by decrementing the col index (col -= 1).
Condition 3: else:  If the current element is less than X, it moves down by incrementing the row index (row += 1).
Element Not Found: If the loop exits without finding the element, it returns 0, indicating that the element is not present in the matrix.
'''