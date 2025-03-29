"""
Given an array arr of non-negative integers, return the maximum product of two numbers possible.

Example:

Input: arr[] = [1, 4, 3, 6, 7, 0] 
Output: 42
Explanation: 6 and 7 have the maximum product.
"""

class Solution:
    def maxProduct(self, arr):
        # Handle case when array has less than 2 elements
        if len(arr) < 2:
            return 0
        
        # Initialize the two largest numbers
        first_max = second_max = float('-inf')
        
        # Iterate through the array to find the two largest numbers
        for num in arr:
            if num > first_max:
                second_max = first_max
                first_max = num
            elif num > second_max:
                second_max = num
        
        # Return the product of the two largest numbers
        return first_max * second_max

# Example usage
sol = Solution()

# Test case 1
arr1 = [1, 4, 3, 6, 7, 0]
print(sol.maxProduct(arr1))  # Output: 42

# Test case 2
arr2 = [0, 2, 5, 9, 1]
print(sol.maxProduct(arr2))  # Output: 45

# Test case 3
arr3 = [5, 5]
print(sol.maxProduct(arr3))  # Output: 25

# Test case 4
arr4 = [1]
print(sol.maxProduct(arr4))  # Output: 0 (as the array has less than two elements)

'''
Code Breakdown:
class Solution:
This defines a class named Solution. The method maxProduct is encapsulated within this class.

def maxProduct(self, arr):
This defines the method maxProduct that takes an array arr as input. 
The self parameter refers to the instance of the class, allowing the method to access other methods and properties within the class.

if len(arr) < 2:
This checks if the array has fewer than 2 elements. 
If it does, it's impossible to find the product of two distinct numbers, so the method returns 0.

first_max = second_max = float('-inf')
This initializes two variables, first_max and second_max, to negative infinity. 
These variables will store the two largest distinct numbers from the array as the program iterates through it.

for num in arr:
This loop iterates through each element num in the array arr.

if num > first_max:
If the current number num is greater than the current first_max (the largest number found so far), then:

second_max = first_max: The previous largest number (stored in first_max) becomes the second largest (second_max).
first_max = num: The current number num becomes the new largest number.
elif num > second_max:
If the current number num is not larger than first_max but is larger than second_max, then:

second_max = num: The current number becomes the second largest number.
return first_max * second_max
After the loop finishes, the method returns the product of the two largest numbers (first_max and second_max).

Example Usage:
arr1 = [1, 4, 3, 6, 7, 0]

The two largest numbers are 6 and 7, and their product is 42.
Output: 42.
arr2 = [0, 2, 5, 9, 1]

The two largest numbers are 5 and 9, and their product is 45.
Output: 45.
arr3 = [5, 5]

The two largest numbers are both 5, and their product is 25.
Output: 25.
arr4 = [1]

Since the array has less than 2 elements, the method returns 0.
Output: 0.
'''