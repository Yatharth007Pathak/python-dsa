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

class Solution:
    # Function to find equilibrium point in the array.
    def equilibriumPoint(self, arr):
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
sol = Solution()
print(sol.equilibriumPoint(arr))  # Output: 3

'''
Let's break down each line of code in the provided Solution class and its equilibriumPoint method:

class Solution:
This defines a new class named Solution, which serves as a container for related functions or methods. 
In this case, the class will hold the equilibriumPoint method.

def equilibriumPoint(self, arr):
This line defines a method named equilibriumPoint within the Solution class. 
It takes two parameters: self, which refers to the instance of the class, and arr, 
which is the list of numbers in which we need to find the equilibrium point.

total_sum = sum(arr)
The sum(arr) function calculates the sum of all the elements in the array arr. 
This total sum is stored in the variable total_sum, which will be used to keep track of the sum of the elements 
to the right of the current index during iteration.

left_sum = 0
A variable left_sum is initialized to 0. 
This variable will keep track of the sum of the elements to the left of the current index as we traverse the array.

for i in range(len(arr)):
A for loop is used to iterate through each index i of the array arr. The loop runs from 0 to len(arr) - 1, covering all elements of the array.

total_sum -= arr[i]
Inside the loop, the current element arr[i] is subtracted from total_sum. 
This step updates total_sum to represent the sum of the elements to the right of the current index i.

if left_sum == total_sum:
The method then checks whether the left_sum (sum of elements to the left of i) is equal to the total_sum (sum of elements to the right of i). 
If they are equal, it means that the current index i is the equilibrium point.

return i + 1
If the equilibrium condition is met, the method returns the 1-based index of the equilibrium point by adding 1 to the current index i. 
This is because array indices in Python start at 0, but the problem might require a 1-based index.

left_sum += arr[i]
If the current index i is not the equilibrium point, the current element arr[i] is added to left_sum. 
This prepares left_sum for the next iteration.

return -1
If the loop completes without finding an equilibrium point, the method returns -1, indicating that no equilibrium point exists in the array.

Example Usage:
An example array arr = [1, 3, 5, 2, 2] is created.
An instance of the Solution class is created and stored in the variable sol.
The equilibriumPoint method is called on sol with arr as an argument, and the result is printed. 
In this case, the output would be 3, meaning the equilibrium point is at index 2 (1-based index 3).
'''