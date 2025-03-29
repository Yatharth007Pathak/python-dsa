"""
Given an array arr of size n-1 that contains distinct integers in the range of 1 to n (inclusive), find the missing element. 
The array is a permutation of size n with one element missing. Return the missing element.

Example:

Input: n = 5, arr[] = [1,2,3,5]
Output: 4
Explanation : All the numbers from 1 to 5 are present except 4.

Input: n = 8, arr[] = [8, 2, 4, 5, 3, 7, 1]
Output: 6
Explanation: All the numbers from 1 to 8 are present except 6.

Input: n = 2, arr[] = [1]
Output: 2
Explanation: Only 1 is present so the missing element is 2.
"""

class Solution:
    # Note that the size of the array is n-1
    def missingNumber(self, n, arr):
        # Calculate the sum of first n natural numbers
        total_sum = n * (n + 1) // 2
        
        # Calculate the sum of elements in the given array
        arr_sum = sum(arr)
        
        # The missing number is the difference between the two sums
        missing_number = total_sum - arr_sum
        
        return missing_number
    
# Example usage:
arr = [1,2,3,5]
n = 5
sol = Solution()
print(sol.missingNumber(n, arr))

'''
Here's a detailed breakdown of the code:

class Solution:
This line defines a new class named Solution. It will contain methods related to solving specific problems.

def missingNumber(self, n, arr):
This line defines a method missingNumber within the Solution class. The method takes two parameters: 
n (the total number of elements including the missing one) and arr (the list of elements from which one number is missing).

total_sum = n * (n + 1) // 2
This line calculates the sum of the first n natural numbers

arr_sum = sum(arr)
This line calculates the sum of the elements present in the array arr. The sum() function adds up all the elements in the list.

missing_number = total_sum - arr_sum
This line computes the missing number by subtracting the sum of the elements in arr from the total sum of the first n natural numbers. 
The difference represents the missing number.

return missing_number
This line returns the computed missing number.

arr = [1,2,3,5]
This line initializes the array arr with the values [1, 2, 3, 5], which is missing the number 4.

n = 5
This line sets n to 5, indicating that the total number of elements (including the missing one) should be 5.

sol = Solution()
This line creates an instance of the Solution class and assigns it to the variable sol.

print(sol.missingNumber(n, arr))
This line calls the missingNumber method on the sol object, passing n and arr as arguments. 
It prints the result, which is the missing number (4) in this case.

Explanation of the Example Usage:
For arr = [1, 2, 3, 5] and n = 5, the total sum of numbers from 1 to 5 is 15.
The sum of the given array arr is 11.
The missing number is 15 - 11 = 4, which is returned by the method and printed.
'''