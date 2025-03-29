"""
Given an array, arr of integers, your task is to return the smallest and second smallest element in the array. 
If the smallest and second smallest do not exist, return -1.

Examples:

Input: arr[] = [2, 4, 3, 5, 6]
Output: 2 3 
Explanation: 2 and 3 are respectively the smallest and second smallest elements in the array.

Input: arr[] = [1, 1, 1]
Output: -1
Explanation: Only element is 1 which is smallest, so there is no second smallest element.
"""

class Solution:
    def minAnd2ndMin(self, arr):
        # If the array has fewer than 2 elements, return -1
        if len(arr) < 2:
            return -1

        # Sort the array
        arr.sort()

        # Traverse the sorted array to find the first distinct second smallest element
        smallest = arr[0]
        for num in arr[1:]:
            if num > smallest:
                return smallest, num
        
        # If no second smallest distinct element found, return -1
        return -1

sol = Solution()

# Test Case 1
arr1 = [2, 4, 3, 5, 6]
print(sol.minAnd2ndMin(arr1))  # Output: (2, 3)

# Test Case 2
arr2 = [1, 1, 1]
print(sol.minAnd2ndMin(arr2))  # Output: -1

# Test Case 3
arr3 = [5]
print(sol.minAnd2ndMin(arr3))  # Output: -1

'''
Here's a detailed line-by-line breakdown of the given code:

Class Definition
class Solution:
Defines a class named Solution. The class will contain the method to find the smallest and second smallest distinct elements in an array.

Method Definition
def minAnd2ndMin(self, arr):
Defines the method minAnd2ndMin inside the Solution class. The method takes one parameter:
arr: The array (or list) containing the numbers.

Handling Arrays with Fewer than 2 Elements
if len(arr) < 2:
Checks if the array has fewer than two elements. Since an array needs at least two distinct elements to find the second smallest number, 
this condition prevents further processing for arrays that are too short.

return -1
If the array has fewer than two elements, 
the method returns -1 to indicate that it's not possible to find both the smallest and second smallest distinct elements.

Sorting the Array
arr.sort()
Sorts the array in ascending order. Sorting helps to easily identify the smallest and second smallest elements, 
as they will be at the beginning of the sorted array.

Finding the Smallest and Second Smallest Distinct Elements
smallest = arr[0]
After sorting, the first element in the array is assigned to the variable smallest. This is the smallest element in the sorted array.

for num in arr[1:]:
Starts a loop that iterates over the elements of the sorted array, starting from the second element (arr[1:]), 
to find the second smallest distinct element.

if num > smallest:
For each element num in the loop, this line checks if it is greater than the smallest element. 
This ensures that the second smallest distinct element is found, as it must be larger than smallest.

return smallest, num
If a number greater than smallest is found, the method returns a tuple containing smallest (the smallest element) 
and num (the second smallest distinct element).

Handling Arrays with No Second Smallest Element
return -1
If the loop completes and no distinct second smallest element is found (e.g., in the case where all elements in the array are equal), 
the method returns -1 to indicate that there is no second smallest distinct element.

Object Instantiation
sol = Solution()
Creates an instance of the Solution class and assigns it to the variable sol. This instance can be used to call the minAnd2ndMin method.

Test Case 1
arr1 = [2, 4, 3, 5, 6]
Defines an array arr1 with multiple distinct elements.

print(sol.minAnd2ndMin(arr1))
Calls the minAnd2ndMin method on the array arr1. The method sorts the array as [2, 3, 4, 5, 6], 
and since 3 is the first distinct element greater than 2, it returns (2, 3).

Test Case 2
arr2 = [1, 1, 1]
Defines an array arr2 where all elements are the same.

print(sol.minAnd2ndMin(arr2))
Calls the minAnd2ndMin method on the array arr2. Since there is no distinct element greater than 1, the method returns -1.

Test Case 3
arr3 = [5]
Defines an array arr3 with only one element.

print(sol.minAnd2ndMin(arr3))
Calls the minAnd2ndMin method on the array arr3. Since the array has fewer than two elements, the method returns -1.
'''