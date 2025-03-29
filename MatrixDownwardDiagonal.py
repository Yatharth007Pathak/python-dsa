"""
Give a N * N square matrix A, return all the elements of its anti-diagonals from top to bottom.

Example 1:

Input: 
N = 2
A = [[1, 2],
    [3, 4]]
Output:
1 2 3 4
order {1, 2, 3, 4}.

Example 2:
Input: 
N = 3 
A = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
Output: 
1 2 4 3 5 7 6 8 9
"""

def downwardDiagonal(N, A):
    result = []
    
    # Traverse diagonals starting from the first row (i = 0)
    for col in range(N):
        i = 0
        j = col
        while i < N and j >= 0:
            result.append(A[i][j])
            i += 1
            j -= 1
    
    # Traverse diagonals starting from the last column (j = N-1)
    for row in range(1, N):
        i = row
        j = N - 1
        while i < N and j >= 0:
            result.append(A[i][j])
            i += 1
            j -= 1
    
    return result

# Example usage
A1 = [[1, 2],
      [3, 4]]

A2 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]

print(downwardDiagonal(2, A1))  # Output: [1, 2, 3, 4]
print(downwardDiagonal(3, A2))  # Output: [1, 2, 4, 3, 5, 7, 6, 8, 9]

'''
Here's a pointwise breakdown of the code:

def downwardDiagonal(N, A):
Defines a function downwardDiagonal that takes two arguments: N (the size of the square matrix) and A (the matrix itself).

result = []
Initializes an empty list result to store the elements found in the downward diagonals.

for col in range(N):
Begins a loop to traverse diagonals starting from each column of the first row (i = 0).

i = 0
j = col
Sets i to 0 (starting row) and j to the current column value (col).

while i < N and j >= 0:
Inner while loop, Continues as long as i is within bounds of the matrix and j is non-negative.

result.append(A[i][j])
Appends the current element A[i][j] to the result list.

i += 1
j -= 1
Increments i to move down to the next row and decrements j to move left to the next column.

for row in range(1, N):
Starts a loop to traverse diagonals starting from each row of the last column (j = N-1), beginning from the second row.

i = row
j = N - 1
Diagonal traversal variables, Sets i to the current row value (row) and j to the last column index (N - 1).

while i < N and j >= 0:
Inner while loop, Continues as long as i is within bounds of the matrix and j is non-negative.

result.append(A[i][j])
Appends the current element A[i][j] to the result list.

i += 1
j -= 1
Increments i to move down to the next row and decrements j to move left to the next column.

return result
Returns the result list containing the elements of the downward diagonals.

A1 = [[1, 2], [3, 4]]
A2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Defines two example matrices A1 and A2.

print(downwardDiagonal(2, A1))
Calls downwardDiagonal with A1 and prints the result, which outputs [1, 2, 3, 4].

print(downwardDiagonal(3, A2))
Calls downwardDiagonal with A2 and prints the result, which outputs [1, 2, 4, 3, 5, 7, 6, 8, 9].


Let's break down the example step by step for both matrices provided to understand how we gather the elements of their anti-diagonals.

Matrix: (N = 2)
1  2
3  4

Step 1: Traverse diagonals starting from the first row

Starting from (0, 0):
Add A[0][0] = 1
Move to (1, -1), which is out of bounds.
Result so far: [1]

Starting from (0, 1):
Add A[0][1] = 2
Move to (1, 0), which is valid:
Add A[1][0] = 3
Move to (2, -1), which is out of bounds.
Result so far: [1, 2, 3]

Step 2: Traverse diagonals starting from the last column

Starting from (1, 1):
Add A[1][1] = 4
Move to (2, 0), which is out of bounds.
Final Result: [1, 2, 3, 4]


Matrix: (N = 3)
1  2  3
4  5  6
7  8  9

Step 1: Traverse diagonals starting from the first row

Starting from (0, 0):

Add A[0][0] = 1
Move to (1, -1), which is out of bounds.
Result so far: [1]

Starting from (0, 1):

Add A[0][1] = 2
Move to (1, 0):
Add A[1][0] = 4
Move to (2, -1), which is out of bounds.
Result so far: [1, 2, 4]

Starting from (0, 2):

Add A[0][2] = 3
Move to (1, 1):
Add A[1][1] = 5
Move to (2, 0):
Add A[2][0] = 7
Move to (3, -1), which is out of bounds.
Result so far: [1, 2, 4, 3, 5, 7]

Step 2: Traverse diagonals starting from the last column

Starting from (1, 2):

Add A[1][2] = 6
Move to (2, 1):
Add A[2][1] = 8
Move to (3, 0), which is out of bounds.
Result so far: [1, 2, 4, 3, 5, 7, 6, 8]

Starting from (2, 2):

Add A[2][2] = 9
Move to (3, 1), which is out of bounds.
Final Result: [1, 2, 4, 3, 5, 7, 6, 8, 9]
'''