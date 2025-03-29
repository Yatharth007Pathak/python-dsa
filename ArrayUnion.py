"""
Given two arrays arr1[] and arr2[], the task is to find the number of elements in the union between these two arrays.
The Union of the two arrays can be defined as the set containing distinct elements from both arrays. 
If there are repetitions, then only one element occurrence should be there in the union.

Note: Elements are not necessarily distinct.

Examples

Input: arr1[] = [1, 2, 3, 4, 5], arr2[] = [1, 2, 3]
Output: 5
Explanation: 1, 2, 3, 4 and 5 are the elements which comes in the union setof both arrays. So count is 5.

Input: arr1[] = [85, 25, 1, 32, 54, 6], arr2[] = [85, 2] 
Output: 7
Explanation: 85, 25, 1, 32, 54, 6, and 2 are the elements which comes in the union set of both arrays. So count is 7.

Input: arr1[] = [1, 2, 1, 1, 2], arr2[] = [2, 2, 1, 2, 1] 
Output: 2
Explanation: We need to consider only distinct. So count is 2.
"""

class Solution:
    def doUnion(self, arr1, arr2):
        # Convert both arrays to sets to get distinct elements
        set1 = set(arr1)
        set2 = set(arr2)
        
        # Union of two sets
        union_set = set1.union(set2)
        
        # Return the number of elements in the union
        return len(union_set)

# Example usage:
solution = Solution()

arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 3]
print(solution.doUnion(arr1, arr2))  # Output: 5

arr1 = [85, 25, 1, 32, 54, 6]
arr2 = [85, 2]
print(solution.doUnion(arr1, arr2))  # Output: 7

arr1 = [1, 2, 1, 1, 2]
arr2 = [2, 2, 1, 2, 1]
print(solution.doUnion(arr1, arr2))  # Output: 2

'''
Here's a breakdown of the code, line by line:

class Solution:
A class named Solution is defined to encapsulate the method for finding the union of two arrays.

def doUnion(self, arr1, arr2):
Defines the method doUnion inside the Solution class.
It takes three arguments: self (the instance of the class), arr1 (the first array), and arr2 (the second array).

set1 = set(arr1)
Converts arr1 into a set set1. This removes any duplicates and keeps only distinct elements.

set2 = set(arr2)
Converts arr2 into a set set2. Similarly, it removes duplicates and retains only unique elements.

union_set = set1.union(set2)
Finds the union of set1 and set2, which gives all unique elements that are present in either arr1 or arr2 (or both). 
The result is stored in union_set.

return len(union_set)
Returns the length of the union_set, which gives the number of unique elements after performing the union operation.

solution = Solution()
Creates an instance of the Solution class.

arr1 = [1, 2, 3, 4, 5]
Defines the first array arr1.

arr2 = [1, 2, 3]
Defines the second array arr2.

print(solution.doUnion(arr1, arr2))
Calls the doUnion method and prints the result, which in this case would be 5 
(since the union of [1, 2, 3, 4, 5] and [1, 2, 3] is {1, 2, 3, 4, 5}).

arr1 = [85, 25, 1, 32, 54, 6]
Defines another array arr1.

arr2 = [85, 2]
Defines another array arr2.

print(solution.doUnion(arr1, arr2))
Calls doUnion on these arrays. The union is {1, 2, 6, 25, 32, 54, 85}, so the output is 7.

arr1 = [1, 2, 1, 1, 2]
Defines another array with duplicate elements.

arr2 = [2, 2, 1, 2, 1]
Defines another array with duplicate elements.

print(solution.doUnion(arr1, arr2))
Calls doUnion on these arrays. The union is {1, 2}, so the output is 2.

Key Notes:
The use of set automatically removes duplicates, which makes this approach simple and efficient for finding the union of two arrays.
'''