"""
Let's play a game! Given a matrix mat[][] with n x m elements. Your task is to check that matrix is Super Similar or not. 
To perform this task you have to follow these Rules: 
Firstly all even index rows to be Rotated left and odd index rows to right, And Rotation is done X times(Index starting from zero). 
Secondly, After all the Rotations check if the initial and the final Matrix are same Return 1 else 0.


Example 1:
Input: n = 2, m = 2
mat = {{1, 2}, 
       {5, 6}}
x = 1
Output: 0
Explanation: Matrix after rotation:
mat = {{ 2, 1}
       { 6, 5}}
After one rotation mat is not same as the previous one.
 

Example 2:
Input: n = 2, m = 4
mat = {{1, 2, 1, 2}, 
       {2, 1, 2, 1}}
x = 2
Output: 1
Explanation: After two rotation mat is same as the previous one.
"""

class Solution:
    def isSuperSimilar(self, n, m, mat, x):
        # Function to rotate a row left by x positions
        def rotate_left(row, x):
            return row[x:] + row[:x]

        # Function to rotate a row right by x positions
        def rotate_right(row, x):
            return row[-x:] + row[:-x]

        # Create a copy of the matrix for rotation
        rotated_mat = [row[:] for row in mat]

        # Perform rotations on each row
        for i in range(n):
            if i % 2 == 0:  # Even index row
                rotated_mat[i] = rotate_left(rotated_mat[i], x % m)
            else:  # Odd index row
                rotated_mat[i] = rotate_right(rotated_mat[i], x % m)

        # Check if the rotated matrix is the same as the original
        return 1 if rotated_mat == mat else 0

solution = Solution()
print(solution.isSuperSimilar(2, 2, [[1, 2], [5, 6]], 1))  # Output: 0
print(solution.isSuperSimilar(2, 4, [[1, 2, 1, 2], [2, 1, 2, 1]], 2))  # Output: 1

'''
Here's a breakdown of the isSuperSimilar function, 
which checks if rotating rows in a matrix by a given number of positions results in a matrix that is identical to the original:

class Solution:
Defines the Solution class which contains the isSuperSimilar method.

def isSuperSimilar(self, n, m, mat, x):
Defines the isSuperSimilar method with parameters:
n: the number of rows in the matrix.
m: the number of columns in the matrix.
mat: the matrix, represented as a 2D list of integers.
x: the number of positions each row should be rotated.

def rotate_left(row, x):
Defines a helper function rotate_left to rotate a row left by x positions.

return row[x:] + row[:x]
Implements the left rotation by taking elements from position x onward (row[x:]) 
and appending the beginning of the row up to position x (row[:x]).

def rotate_right(row, x):
Defines another helper function rotate_right to rotate a row right by x positions.

return row[-x:] + row[:-x]
Implements the right rotation by taking the last x elements (row[-x:]) and appending the rest of the row (row[:-x]).

rotated_mat = [row[:] for row in mat]
Creates a copy of the matrix mat, named rotated_mat. This copy is used to apply the rotations without altering the original matrix.

for i in range(n):
A loop iterates through each row i of the matrix.

if i % 2 == 0:
Checks if the row index i is even. If true, the row will be rotated left.

rotated_mat[i] = rotate_left(rotated_mat[i], x % m)
Rotates the row i left by x % m positions (modulo m ensures the rotation count stays within bounds) and updates the rotated matrix.

else:
Executes for odd-indexed rows.

rotated_mat[i] = rotate_right(rotated_mat[i], x % m)
Rotates the row i right by x % m positions and updates the rotated matrix.

return 1 if rotated_mat == mat else 0
Compares rotated_mat with the original matrix mat. If they are identical, 
it returns 1 (indicating the matrix is "super similar" after rotation); otherwise, it returns 0.

solution = Solution()
Creates an instance of the Solution class.

print(solution.isSuperSimilar(2, 2, [[1, 2], [5, 6]], 1))
This call checks if rotating the matrix [[1, 2], [5, 6]] by 1 position yields a matrix identical to the original. 
The output is 0, meaning they are not identical after rotation.

print(solution.isSuperSimilar(2, 4, [[1, 2, 1, 2], [2, 1, 2, 1]], 2))
This call checks if rotating the matrix [[1, 2, 1, 2], [2, 1, 2, 1]] by 2 positions yields a matrix identical to the original. 
The output is 1, meaning they are identical after rotation.
'''