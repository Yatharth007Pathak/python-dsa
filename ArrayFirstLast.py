"""
Given a sorted array arr with possibly some duplicates, the task is to find the first and last occurrences of an element x in the given array.
Note: If the number x is not found in the array then return both the indices as -1.

Examples:

Input: arr[] = [1, 3, 5, 5, 5, 5, 67, 123, 125], x = 5
Output: [2, 5]
Explanation: First occurrence of 5 is at index 2 and last occurrence of 5 is at index 5

Input: arr[] = [1, 3, 5, 5, 5, 5, 7, 123, 125], x = 7
Output: [6, 6]
Explanation: First and last occurrence of 7 is at index 6

Input: arr[] = [1, 2, 3], x = 4
Output: [-1, -1]
Explanation: No occurrence of 4 in the array, so, output is [-1, -1]
"""

class Solution:
    def find(self, arr, x):
        def find_first(arr, x):
            left, right = 0, len(arr) - 1
            first_occurrence = -1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == x:
                    first_occurrence = mid
                    right = mid - 1  # Search in the left half for the first occurrence
                elif arr[mid] < x:
                    left = mid + 1
                else:
                    right = mid - 1
            return first_occurrence

        def find_last(arr, x):
            left, right = 0, len(arr) - 1
            last_occurrence = -1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] == x:
                    last_occurrence = mid
                    left = mid + 1  # Search in the right half for the last occurrence
                elif arr[mid] < x:
                    left = mid + 1
                else:
                    right = mid - 1
            return last_occurrence

        first = find_first(arr, x)
        last = find_last(arr, x)

        return [first, last] if first != -1 else [-1, -1]

# Example usage
solution = Solution()
print(solution.find([1, 3, 5, 5, 5, 5, 67, 123, 125], 5))  # Output: [2, 5]
print(solution.find([1, 3, 5, 5, 5, 5, 7, 123, 125], 7))  # Output: [6, 6]
print(solution.find([1, 2, 3], 4))  # Output: [-1, -1]

'''
Here's a line-by-line breakdown of the code:

Class Solution:
Defines a class named Solution which contains methods to solve problems.

Method find in Solution class:
This method finds the first and last occurrences of a given element (x) in a sorted array (arr).
It defines two helper functions, find_first and find_last, for finding the first and last positions of x in arr using binary search.

Helper Function find_first:
This function finds the first occurrence of x in arr using binary search.
left, right = 0, len(arr) - 1 initializes pointers left and right to the start and end of the array, respectively.
first_occurrence = -1 initializes a variable to store the index of the first occurrence of x, setting it to -1 initially (indicating not found).

Binary Search Loop in find_first:
while left <= right: runs the loop until left is greater than right.
mid = (left + right) // 2 calculates the middle index of the current search range.
If arr[mid] == x:
first_occurrence = mid updates first_occurrence to mid since x is found at this index.
right = mid - 1 continues searching in the left half to ensure this is the first occurrence.
If arr[mid] < x:
left = mid + 1 moves the left pointer to the right, as x would be in the right half.
If arr[mid] > x:
right = mid - 1 moves the right pointer to the left, as x would be in the left half.
return first_occurrence returns the index of the first occurrence of x or -1 if x is not found.

Helper Function find_last:
This function finds the last occurrence of x in arr using a similar binary search approach as find_first.
left, right = 0, len(arr) - 1 initializes the pointers.
last_occurrence = -1 sets up a variable to store the last occurrence of x (default -1 for "not found").

Binary Search Loop in find_last:
while left <= right: iterates while left is less than or equal to right.
mid = (left + right) // 2 calculates the middle index.
If arr[mid] == x:
last_occurrence = mid sets last_occurrence to mid.
left = mid + 1 shifts the left pointer to the right half to find the last occurrence.
If arr[mid] < x:
left = mid + 1 moves the left pointer to the right, as x would be in the right half.
If arr[mid] > x:
right = mid - 1 moves the right pointer to the left.
return last_occurrence returns the index of the last occurrence of x or -1 if x is not found.

Call find_first and find_last in find:
first = find_first(arr, x) finds the first occurrence of x.
last = find_last(arr, x) finds the last occurrence of x.

Return Result:
return [first, last] if first != -1 else [-1, -1]:
Returns [first, last] if x is found (first != -1).
Otherwise, returns [-1, -1] if x is not found in arr.

Example Usage:
solution = Solution() creates an instance of the Solution class.
print(solution.find([1, 3, 5, 5, 5, 5, 67, 123, 125], 5)) searches for 5 in the array, expecting [2, 5].
print(solution.find([1, 3, 5, 5, 5, 5, 7, 123, 125], 7)) searches for 7, expecting [6, 6].
print(solution.find([1, 2, 3], 4)) searches for 4 (not in the array), expecting [-1, -1].
'''