"""
You are given a 2D array consisting of only 1's and 0's, where each row is sorted in non-decreasing order. 
You need to find and return the index of the first row that has the most number of 1s. If no such row exists, return -1.
Note: 0-based indexing is followed.

Examples:

Input: arr[][] = [[0, 1, 1, 1],
               [0, 0, 1, 1],
               [1, 1, 1, 1],
               [0, 0, 0, 0]]
Output: 2
Explanation: Row 2 contains 4 1's.

Input: arr[][] = [[0, 0], 
               [1, 1]]
Output: 1
Explanation: Row 1 contains 2 1's.
"""

class Solution:
    # Function to find the index of the row with the maximum number of 1s
    def rowWithMax1s(self, arr):
        # Initialize variables to keep track of the row index with max 1s and the count of 1s
        max_1s_count = 0
        row_index = -1
        
        # Loop through each row in the array
        for i in range(len(arr)):
            # Count the number of 1s in the current row
            count_1s = sum(arr[i])
            
            # Update the row index if this row has more 1s than previously recorded
            if count_1s > max_1s_count:
                max_1s_count = count_1s
                row_index = i
                
        return row_index

# Example inputs
arr1 = [[0, 1, 1, 1],
        [0, 0, 1, 1],
        [1, 1, 1, 1],
        [0, 0, 0, 0]]

arr2 = [[0, 0],
        [1, 1]]

# Creating an instance of Solution
solution = Solution()

# Finding the index of the row with the most 1s
print(solution.rowWithMax1s(arr1))  # Output: 2
print(solution.rowWithMax1s(arr2))  # Output: 1

'''
Here's a line-by-line breakdown of the code:

Class Solution:
Defines a class called Solution, which contains methods for solving matrix-related problems.

Method rowWithMax1s:
Defines a function called rowWithMax1s to find the index of the row with the maximum number of 1s in a given 2D array (arr).

Initial Setup in rowWithMax1s:
max_1s_count = 0 initializes max_1s_count to zero. This variable will store the highest count of 1s found in any row so far.
row_index = -1 initializes row_index to -1 to indicate that no row with 1s has been found yet.

Loop through Each Row:
for i in range(len(arr)): starts a loop to go through each row in the array arr. Here, i is the index of the current row.

Counting the Number of 1s in the Current Row:
count_1s = sum(arr[i]) calculates the sum of the elements in the current row (arr[i]). 
Since the elements are 0s and 1s, this sum gives the total number of 1s in the row.

Updating the Row with the Maximum Number of 1s:
if count_1s > max_1s_count: checks if the count of 1s in the current row is greater than max_1s_count.
If true, max_1s_count = count_1s updates max_1s_count to the count of 1s in this row.
row_index = i updates row_index to the current row index i as it has the highest count of 1s found so far.

Return the Result:
return row_index returns the index of the row with the most 1s. If no row has any 1s, it returns -1.

Example Arrays for Testing:
arr1 and arr2 define two test cases. Each is a 2D array (list of lists) with 0s and 1s.

Creating an Instance of Solution:
solution = Solution() creates an instance of the Solution class to access its methods.

Finding and Printing the Row with the Most 1s:
print(solution.rowWithMax1s(arr1)) calls the rowWithMax1s function with arr1 and prints the result, 
which is expected to be 2 (the third row has the most 1s).
print(solution.rowWithMax1s(arr2)) calls the rowWithMax1s function with arr2 and prints the result, 
which is expected to be 1 (the second row has the most 1s).
'''