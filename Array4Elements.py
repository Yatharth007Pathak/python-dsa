"""
Given an array A of N integers. 
You have to find whether a combination of four elements in the array whose sum is equal to a given value X exists or not.
 

Example 1:

Input: N = 6, A[] = {1, 5, 1, 0, 6, 0}, X = 7
Output: 1
Explantion: 1, 5, 1, 0 are the four elements which makes sum 7.
"""

def find4Numbers(A, n, X):
    # Sort the array to use two-pointer technique effectively
    A.sort()
    
    # Iterate through each element
    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            # Set two pointers for the remaining elements
            left, right = j + 1, n - 1

            # Now we need to find two numbers such that their sum equals X            
            while left < right:
                current_sum = A[i] + A[j] + A[left] + A[right]
                if current_sum == X:
                    return 1
                elif current_sum < X:
                    left += 1
                else:
                    right -= 1

    return 0

# Example usage
A = [1, 5, 1, 0, 6, 0]
N = len(A)
X = 7
print(find4Numbers(A, N, X))  # Output: 1

'''
Here's a pointwise breakdown for each line of the code:

def find4Numbers(A, n, X):
Defines a function called find4Numbers that takes three parameters: A (a list of integers), n (length of the list A), and X (the target sum).

A.sort()
Sorts the array A in non-decreasing order to facilitate using the two-pointer technique.

for i in range(n - 3):
Starts a loop to iterate through each element from index 0 to n - 4 to fix the first element.

for j in range(i + 1, n - 2):
Starts a nested loop to iterate through the elements from i + 1 to n - 3 to fix the second element.

left, right = j + 1, n - 1
Sets two pointers, left and right, to j + 1 and n - 1, respectively, to traverse the remaining part of the array.

while left < right:
Starts a while loop that continues as long as left is less than right.

current_sum = A[i] + A[j] + A[left] + A[right]
Calculates the sum of the four selected elements (A[i], A[j], A[left], A[right]).

if current_sum == X:
Checks if the sum of the four numbers is equal to X.

return 1
If the condition is true, returns 1 to indicate that four numbers with the given sum exist.

elif current_sum < X:
Checks if current_sum is less than X.

left += 1
If current_sum is less than X, increments left by 1 to increase the sum.

else:
Executes if current_sum is greater than X.

right -= 1
If current_sum is greater than X, decrements right by 1 to decrease the sum.

return 0
If the loop ends without finding a sum equal to X, returns 0 to indicate that no such four numbers exist.

A = [1, 5, 1, 0, 6, 0]

Defines the list A with integers.
N = len(A)
Calculates the length of the list A and assigns it to N.

X = 7
Sets the target sum value X to 7.

print(find4Numbers(A, N, X))
Calls the find4Numbers function with the list A, its length N, and the target sum X, and prints the result (1).
'''