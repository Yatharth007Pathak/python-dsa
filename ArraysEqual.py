"""
Given two arrays arr1 and arr2 of equal size, the task is to find whether the given arrays are equal. 
Two arrays are said to be equal if both contain the same set of elements, arrangements (or permutations) of elements may be different though.
Note: If there are repetitions, then counts of repeated elements must also be the same for two arrays to be equal.

Examples:

Input: arr1[] = [1, 2, 5, 4, 0], arr2[] = [2, 4, 5, 0, 1]
Output: true
Explanation: Both the array can be rearranged to [0,1,2,4,5]

Input: arr1[] = [1, 2, 5], arr2[] = [2, 4, 15]
Output: false
Explanation: arr1[] and arr2[] have only one common value.
"""

from collections import Counter

class Solution:
    # Function to check if two arrays are equal or not.
    def check(self, arr1, arr2) -> bool:
        # If lengths differ, they can't be equal
        if len(arr1) != len(arr2):
            return False
        # Use Counter to count occurrences of each element in both arrays
        return Counter(arr1) == Counter(arr2)

# Example usage
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    arr1 = [1, 2, 5, 4, 0]
    arr2 = [2, 4, 5, 0, 1]
    print(solution.check(arr1, arr2))  # Output: True

    # Test case 2
    arr1 = [1, 2, 5]
    arr2 = [2, 4, 15]
    print(solution.check(arr1, arr2))  # Output: False

'''
Here's a line-by-line breakdown of the code that checks if two arrays are equal:

Import the Counter class from the collections module: Counter is a dictionary subclass used for counting hashable objects. 
It makes it easy to count occurrences of elements in the arrays.

Define the Solution class: This class contains the method check, which determines if two arrays are equal.

Define the check method: This method takes in two arrays (arr1 and arr2) and returns a boolean value indicating whether the arrays are equal.

Check if the lengths of the arrays differ:
If the lengths of arr1 and arr2 are not the same, they cannot be equal.
If they differ, return False.

Use Counter to count occurrences of each element in both arrays:
The Counter class from the collections module creates a frequency dictionary for each array, counting how many times each element appears.
If the two Counter objects are equal, it means both arrays contain the same elements with the same frequencies.

Return the result of the comparison: If both Counter objects are equal, return True; otherwise, return False.

Example Usage and Output
Input for Test Case 1:
arr1 = [1, 2, 5, 4, 0]
arr2 = [2, 4, 5, 0, 1]

Output: True

Explanation: Both arrays contain the same elements (1, 2, 4, 5, 0) in different orders, so they are considered equal.

Input for Test Case 2:
arr1 = [1, 2, 5]
arr2 = [2, 4, 15]

Output: False

Explanation: The arrays have different elements; hence, they are not equal.
'''