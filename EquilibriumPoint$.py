"""
Given an array arr of non-negative numbers. The task is to find the first equilibrium point in an array. 
The equilibrium point in an array is an index (or position) such that the sum of all elements before that index 
is the same as the sum of elements after it.

Note: Return equilibrium point in 1-based indexing. Return -1 if no such point exists.

Example:

Input: arr[] = [1, 3, 5, 2, 2]
Output: 3 
Explanation: The equilibrium point is at position 3 as the sum of elements before it (1+3) = sum of elements after it (2+2). 

Input: arr[] = [0, 1, 0]
Output: 2
Explanation: Since sum all the elements before 1 and after 1 are same, so index 2 is equillibrium.

Input: arr[] = [1, 2, 3]
Output: -1
Explanation: There is no equilibrium point in the given array.
"""

def Solution(arr):
    # Total sum of the array
    total_sum = sum(arr)
        
    # Initialize left sum to 0
    left_sum = 0
        
    # Traverse through the array
    for i in range(len(arr)):
        # Update total sum by subtracting the current element
        total_sum -= arr[i]
            
        # Check if left sum equals the total sum
        if left_sum == total_sum:
            # Return the 1-based index
            return i + 1
            
        # Update left sum for the next iteration
        left_sum += arr[i]
        
    # If no equilibrium index is found, return -1
    return -1

# Example usage:
arr = [1, 3, 5, 2, 2]
sol = Solution(arr)
print(sol)  # Output: 3

'''
Here is a breakdown of the provided code:

def Solution(arr):
This line defines a function named Solution that takes one parameter, arr, 
which is the array of numbers in which you want to find the equilibrium point. 
However, in Python, it is better to avoid naming a function with a capital letter (as it is typically reserved for class names)
and using Solution for a function can be confusing, especially when it's intended to represent a class in other contexts.

Calculate Total Sum (total_sum = sum(arr)):
The sum(arr) function calculates the sum of all the elements in the array arr. 
This sum is stored in variable total_sum, which will be used to track the sum of elements to the right of the current index during iteration.

Initialize Left Sum (left_sum = 0):
A variable left_sum is initialized to 0. 
This variable will accumulate the sum of elements to the left of the current index as you iterate through the array.

Traverse the Array (for i in range(len(arr)):):
A for loop iterates through each index i of the array arr. The loop runs from 0 to len(arr) - 1, covering all elements.

Update Total Sum (total_sum -= arr[i]):
Inside the loop, the current element arr[i] is subtracted from total_sum. 
After this operation, total_sum represents the sum of elements to the right of the current index.

Check Equilibrium Condition (if left_sum == total_sum:):
The code checks if left_sum (sum of elements to the left of the current index) is equal to total_sum 
(sum of elements to the right of the current index). If they are equal, the current index i is the equilibrium point.

Return 1-based Index (return i + 1):
If the condition is met, the function returns the 1-based index by adding 1 to the current index i. 
This is because array indices in Python start at 0, but the problem might require a 1-based index.

Update Left Sum (left_sum += arr[i]):
If the current index i is not the equilibrium point, the current element arr[i] is added to left_sum. 
This prepares left_sum for the next iteration.

Return -1 if No Equilibrium Index Found (return -1):
If the loop completes without finding an equilibrium point, the function returns -1, 
indicating that no equilibrium point exists in the array.

Example Usage:
An example array arr = [1, 3, 5, 2, 2] is provided.
The function Solution(arr) is called, and the result is stored in sol.
The result is printed, which should output 3, indicating the equilibrium point is at index 2 (1-based index 3).
'''