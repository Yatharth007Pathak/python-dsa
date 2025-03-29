"""
Given an array arr of distinct elements, the task is to return an array of all elements except the two greatest elements in sorted order.

Examples:

Input: arr[] = [2, 8, 7, 1, 5]
Output: [1, 2, 5] 
Explanation: Here we return an array contains 1 , 2, 5 and we leave two greatest elements 5 & 7. 

Input: arr[] = [7, -2, 3, 4, 9, -1]
Output: [-2, -1, 3, 4]
Explanation: Here we return an array contains -2 , -1, 3, 4 and we leave two greatest elements 7 & 9. 
"""

class Solution:
    def findElements(self, arr):
        # Sort the array
        arr.sort()
        # Return the array except the last two elements
        return arr[:-2]

# Example usage:
sol = Solution()
print(sol.findElements([2, 8, 7, 1, 5]))  # Output: [1, 2, 5]
print(sol.findElements([7, -2, 3, 4, 9, -1]))  # Output: [-2, -1, 3, 4]

'''
Here's a pointwise breakdown of the code:

Class Definition: The class Solution is defined using the class keyword, which is a blueprint for creating objects.

Method Definition: Inside the class, a method findElements is defined that takes self 
(a reference to the instance of the class) and arr (an array passed as a parameter) as inputs.

Sorting the Array: The method uses arr.sort() to sort the array in non-decreasing order. This modifies the original array.

Returning a Sliced Array: The method returns the array excluding the last two elements, using arr[:-2]. 
The slice [:-2] means it includes all elements from the start up to (but not including) the last two.

Example Usage: An instance sol of the Solution class is created. 
The method findElements is called on this instance with the arrays [2, 8, 7, 1, 5] and [7, -2, 3, 4, 9, -1], 
which returns the sorted arrays with the last two elements removed.

The first call outputs [1, 2, 5], and the second call outputs [-2, -1, 3, 4].
'''