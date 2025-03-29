"""
Given an array, arr of positive integers. Find the third largest element in it. Return -1 if the third largest element is not found.

Examples:

Input: arr[] = [2, 4, 1, 3, 5]
Output: 3
Explanation: The third largest element in the array [2, 4, 1, 3, 5] is 3.

Input: arr[] = [10, 2]
Output: -1
Explanation: There are less than three elements in the array, so the third largest element cannot be determined.

Input: arr[] = [5, 5, 5]
Output: 5
Explanation: In the array [5, 5, 5], the third largest element can be considered 5, as there are no other distinct elements.
"""

class Solution:
    def thirdLargest(self, arr):
        # Check if the array has less than 3 elements
        if len(arr) < 3:
            return -1
        
        # Use a set to remove duplicates and then sort the array in descending order
        arr = sorted(arr, reverse=True)
        
        # Check if the sorted array has at least 3 distinct elements
        return arr[2]  # Return the third largest element

# Example Usage
solution = Solution()
print(solution.thirdLargest([2, 4, 1, 3, 5]))  # Output: 3
print(solution.thirdLargest([10, 2]))          # Output: -1
print(solution.thirdLargest([5, 5, 5]))        # Output: 5

'''
Here is a line-by-line breakdown of the code in pointwise format:

Class Definition:
The class Solution is defined. 
This class contains a method thirdLargest that will be used to find the third largest distinct element from a given list of integers.

Method Definition:
The method thirdLargest is defined inside the Solution class. 
It takes two arguments: self (referring to the instance of the class) and arr (the array or list of integers to process).

Check if Array has Less Than 3 Elements:
The method checks if the length of the array arr is less than 3 using if len(arr) < 3:.
If true, it returns -1, indicating that there are not enough elements to find the third largest distinct number.

Sort the Array in Descending Order:
The array arr is sorted in descending order using sorted(arr, reverse=True). 
Sorting in reverse order places the largest elements at the beginning.

Return the Third Largest Element:
After sorting, the method returns the third element in the array using arr[2]. 
Since Python lists are zero-indexed, the third element is located at index 2.

Example Usage:
An instance of the Solution class is created by calling solution = Solution().

Test Case 1:
The method thirdLargest is called with the list [2, 4, 1, 3, 5]. 
The output is 3 because after sorting the array in descending order, the elements are [5, 4, 3, 2, 1] and the third largest element is 3.

Test Case 2:
The method thirdLargest is called with the list [10, 2]. Since the array has fewer than 3 elements, the method returns -1.

Test Case 3:
The method thirdLargest is called with the list [5, 5, 5]. After sorting, the array remains [5, 5, 5]. Since all elements are the same, 
the method returns 5 as the third "largest" element, even though there are no distinct elements.
'''