"""
Given a non null integer matrix Grid of dimensions NxM.Calculate the sum of its elements.

Example 1:

Input: N=2,M=3, Grid= [[1,0,1], [-8,9,-2]]
Output: 1
Explanation: The sum of all elements of the matrix is (1+0+1-8+9-2)=1.

Example 2:
Input: N=3,M=5, Grid= [[1,0,1,0,1], [0,1,0,1,0], [-1,-1,-1,-1,-1]]
Output: 0
Explanation: The sum of all elements of the matrix are (1+0+1+0+1+0+1+0+1+0-1-1-1-1-1)=0.
"""

class Solution:
    def sumOfMatrix(self, N, M, Grid):
        # Initialize the sum to 0
        total_sum = 0
        
        # Iterate over each row
        for row in Grid:
            # Add up all elements in the current row to total_sum
            total_sum += sum(row)
        
        return total_sum

# Example Usage
solution = Solution()

# Test case 1
N = 2
M = 3
Grid = [[1, 0, 1], [-8, 9, -2]]
print(solution.sumOfMatrix(N, M, Grid))  # Output: 1

# Test case 2
N = 3
M = 5
Grid = [[1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [-1, -1, -1, -1, -1]]
print(solution.sumOfMatrix(N, M, Grid))  # Output: 0

'''
Here is the line-by-line breakdown of the code in pointwise format:

Class Definition:
The class Solution is defined. It contains a method sumOfMatrix that calculates the sum of all elements in a matrix.
Method Definition:
The method sumOfMatrix is defined inside the Solution class. It takes three arguments:
N: the number of rows in the matrix.
M: the number of columns in the matrix.
Grid: a 2D list representing the matrix.

Initialize the Total Sum:
A variable total_sum is initialized to 0. This variable will store the cumulative sum of all elements in the matrix.

Iterating Over Each Row:
A for loop iterates through each row in the matrix Grid. The variable row represents the current row in each iteration.

Sum of Each Row:
Inside the loop, sum(row) calculates the sum of all elements in the current row, and this value is added to total_sum.

Returning the Total Sum:
After iterating through all rows, the method returns total_sum, which now contains the sum of all elements in the matrix.

Example Usage:
An instance of the Solution class is created using solution = Solution().

Test Case 1:
The method sumOfMatrix is called with N = 2, M = 3, and Grid = [[1, 0, 1], [-8, 9, -2]].
The sum of the first row is 1 + 0 + 1 = 2.
The sum of the second row is -8 + 9 + -2 = -1.
The total sum is 2 + (-1) = 1.
The output is 1.

Test Case 2:
The method sumOfMatrix is called with N = 3, M = 5, and Grid = [[1, 0, 1, 0, 1], [0, 1, 0, 1, 0], [-1, -1, -1, -1, -1]].
The sum of the first row is 1 + 0 + 1 + 0 + 1 = 3.
The sum of the second row is 0 + 1 + 0 + 1 + 0 = 2.
The sum of the third row is -1 + -1 + -1 + -1 + -1 = -5.
The total sum is 3 + 2 + (-5) = 0.
The output is 0.
'''