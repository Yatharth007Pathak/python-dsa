"""
A celebrity is a person who is known to all but does not know anyone at a party. A party is being organized by some people. 
A square matrix mat is used to represent people at the party such that if an element of row i and column j is set to 1 it means ith person 
knows jth person. You need to return the index of the celebrity in the party, if the celebrity does not exist, return -1.

Note: Follow 0-based indexing.

Examples:

Input: mat[][] = [[0 1 0],
                [0 0 0], 
                [0 1 0]]
Output: 1
Explanation: 0th and 2nd person both know 1. Therefore, 1 is the celebrity.

Input: mat[][] = [[0 1],
                [1 0]]
Output: -1
Explanation: The two people at the party both know each other. None of them is a celebrity.
"""

class Solution:
    def celebrity(self, mat):
        n = len(mat)
        celebrity_candidate = 0
        
        # Step 1: Find the celebrity candidate
        for i in range(1, n):
            if mat[celebrity_candidate][i] == 1:
                # If the current candidate knows i, then the candidate can't be a celebrity
                celebrity_candidate = i
        
        # Step 2: Verify if the candidate is a celebrity
        for i in range(n):
            if i != celebrity_candidate:
                # Check if the candidate knows anyone or not everyone knows the candidate
                if mat[celebrity_candidate][i] == 1 or mat[i][celebrity_candidate] == 0:
                    return -1
        
        return celebrity_candidate

# Example Usage
sol = Solution()
mat1 = [[0, 1, 0],
        [0, 0, 0],
        [0, 1, 0]]
print(sol.celebrity(mat1))  # Output: 1

mat2 = [[0, 1],
        [1, 0]]
print(sol.celebrity(mat2))  # Output: -1

'''
Here's a line-by-line breakdown of the code:

class Solution:
A class named Solution is defined to encapsulate the solution to the problem of finding a celebrity.

def celebrity(self, mat):
This is a method inside the Solution class that takes a matrix mat as input. This matrix represents who knows whom. 
The method will determine if there is a celebrity in the group.

n = len(mat):
The variable n is set to the length of the matrix, which represents the number of people.

celebrity_candidate = 0:
Initially, the first person (index 0) is assumed to be the celebrity candidate.

for i in range(1, n):
A loop starts, iterating through the rest of the people (from 1 to n-1), to find a potential celebrity.

if mat[celebrity_candidate][i] == 1:
The condition checks if the current celebrity candidate knows person i.

celebrity_candidate = i:
If the celebrity candidate knows person i, the candidate cannot be a celebrity, so i becomes the new celebrity candidate.

for i in range(n):
After finding the candidate, another loop starts to verify if the chosen candidate is truly a celebrity by checking everyone.

if i != celebrity_candidate:
The condition ensures that the candidate is not compared to themselves.

if mat[celebrity_candidate][i] == 1 or mat[i][celebrity_candidate] == 0:
Two checks are performed:

If the celebrity candidate knows someone (mat[celebrity_candidate][i] == 1), they cannot be a celebrity.
If someone doesn’t know the candidate (mat[i][celebrity_candidate] == 0), the candidate cannot be a celebrity.
return -1:
If either condition fails, the function returns -1, indicating there is no celebrity.

return celebrity_candidate:
If all checks pass, the function returns the index of the celebrity candidate.

Example usage:

sol = Solution():
An instance of the Solution class is created.

mat1 = [[0, 1, 0], [0, 0, 0], [0, 1, 0]]
A matrix is defined where:
0 means the person doesn't know the other.
1 means the person knows the other.
The matrix is for a group of 3 people.
print(sol.celebrity(mat1)):
The celebrity method is called on mat1, and the result (1) is printed. This means person 1 is the celebrity.

mat2 = [[0, 1], [1, 0]]
Another matrix is defined for a group of 2 people.

print(sol.celebrity(mat2)):
The celebrity method is called on mat2, and the result (-1) is printed, indicating there is no celebrity.
'''