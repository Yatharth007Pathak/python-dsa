"""
Given an array arr, write a program segregating even and odd numbers. 
The program should put all even numbers first in sorted order, and then odd numbers in sorted order.

Note:- You don't have to return the array, you have to modify it in-place.

Example:
Input: arr[] = [12, 34, 45, 9, 8, 90, 3]
Output: [8, 12, 34, 90, 3, 9, 45]
Explanation: Even numbers are 12, 34, 8 and 90. Rest are odd numbers.

Input: arr[] = [0, 1, 2, 3, 4]
Output: [0, 2, 4, 1, 3]
Explanation: 0 2 4 are even and 1 3 are odd numbers.
"""

class Solution:
    def segregateEvenOdd(self, arr):
        # Separate even and odd numbers
        even_nums = [num for num in arr if num % 2 == 0]
        odd_nums = [num for num in arr if num % 2 != 0]
        
        # Sort both lists
        even_nums.sort()
        odd_nums.sort()
        
        # Modify the array in-place
        arr[:] = even_nums + odd_nums

# Example usage:
sol = Solution()
arr1 = [12, 34, 45, 9, 8, 90, 3]
sol.segregateEvenOdd(arr1)
print(arr1)  # Output: [8, 12, 34, 90, 3, 9, 45]

arr2 = [0, 1, 2, 3, 4]
sol.segregateEvenOdd(arr2)
print(arr2)  # Output: [0, 2, 4, 1, 3]

'''
Here's a pointwise breakdown of the code:

The class Solution is defined with a method segregateEvenOdd.
Inside the method, two list comprehensions are used:
even_nums stores all even numbers from the input array arr by checking if num % 2 == 0.
odd_nums stores all odd numbers from arr by checking if num % 2 != 0.
Both even_nums and odd_nums are sorted in ascending order using the sort() method.
The input array arr is modified in-place by assigning it the concatenation of even_nums and odd_nums using arr[:], 
which replaces the original array's contents.
In the example usage:
The method is called on the array [12, 34, 45, 9, 8, 90, 3], which results in [8, 12, 34, 90, 3, 9, 45], 
with even numbers first, followed by odd numbers, both sorted.
For the array [0, 1, 2, 3, 4], it produces [0, 2, 4, 1, 3], where even numbers come first, followed by odd numbers.
'''