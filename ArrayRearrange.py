"""
You are given an array of size N. Rearrange the given array in-place such that all negative numbers occur before all non-negative numbers.
(Maintain the order of all -ve and non-negative numbers as given in the original array).

Example 1:
Input: N = 4, Arr[] = {-3, 3, -2, 2}
Output: -3 -2 3 2
Explanation: In the given array, negative numbers are -3, -2 and non-negative numbers are 3, 2. 

Example 2:
Input: N = 4, Arr[] = {-3, 1, 0, -2}
Output: -3 -2 1 0
Explanation: In the given array, negative numbers are -3, -2 and non-negative numbers are 1, 0.
"""

from typing import List

class Solution:
    def Rearrange(self, n: int, arr: List[int]) -> None:
        """
        Rearrange the array in-place so that all negative numbers appear before non-negative numbers,
        while maintaining their relative order.
        
        :param n: int - Size of the array
        :param arr: List[int] - The array to be rearranged
        :return: None (The input array is modified in-place)
        """
        # Create two lists: one for negative and one for non-negative numbers
        negative = [num for num in arr if num < 0]
        non_negative = [num for num in arr if num >= 0]
        
        # Combine the two lists and modify the original array in-place
        arr[:] = negative + non_negative


# Example Usage
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    arr1 = [-3, 3, -2, 2]
    solution.Rearrange(len(arr1), arr1)
    print(arr1)  # Output: [-3, -2, 3, 2]
    
    # Example 2
    arr2 = [-3, 1, 0, -2]
    solution.Rearrange(len(arr2), arr2)
    print(arr2)  # Output: [-3, -2, 1, 0]

'''
Explanation of the Code
The goal is to rearrange the input array so that all negative numbers appear before non-negative numbers, 
maintaining the relative order of both groups.

class Solution:
This class contains the method Rearrange to perform the required task.

Method: Rearrange
def Rearrange(self, n: int, arr: List[int]) -> None:
Rearranges the array in-place without returning anything.

Parameters:
n: The size of the array (integer).
arr: The list of integers to be rearranged.

Step 1: Separate Negative and Non-Negative Numbers
negative = [num for num in arr if num < 0]
Creates a list of all negative numbers in the array using a list comprehension.

non_negative = [num for num in arr if num >= 0]
Creates a list of all non-negative numbers in the array using a list comprehension.

Step 2: Combine and Modify the Original Array
arr[:] = negative + non_negative
Combines the two lists (negative and non_negative) into a single list.
The [:] ensures the operation modifies the original array in-place.

Example 1: Input [-3, 3, -2, 2]
Separate Numbers:
negative = [-3, -2]
non_negative = [3, 2]
Combine:
arr[:] = [-3, -2] + [3, 2]
Result: [-3, -2, 3, 2]

Example 2: Input [-3, 1, 0, -2]
Separate Numbers:
negative = [-3, -2]
non_negative = [1, 0]
Combine:
arr[:] = [-3, -2] + [1, 0]
Result: [-3, -2, 1, 0]
'''