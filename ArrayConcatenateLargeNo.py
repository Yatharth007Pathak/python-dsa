"""
Given an array of strings arr[] representing non-negative integers, arrange them so that, after concatenating them in order, 
it results in the largest possible number. Since the result may be very large, return it as a string.
Note: There are no leading zeros in each array element.

Examples:

Input: arr[] =  ["3", "30", "34", "5", "9"]
Output: "9534330"
Explanation: Given numbers are  {"3", "30", "34", "5", "9"}, the arrangement "9534330" gives the largest value.

Input: arr[] =  ["54", "546", "548", "60"]
Output: "6054854654"
Explanation: Given numbers are {"54", "546", "548", "60"}, the arrangement "6054854654" gives the largest value.

Input: arr[] =  ["3", "4", "6", "5", "9"]
Output: "96543"
Explanation: Given numbers are  {"3", "4", "6", "5", "9"}, the arrangement "96543" gives the largest value.
"""

from functools import cmp_to_key

class Solution:
    def printLargest(self, arr):
        # Define a custom comparator
        def compare(X, Y):
            # Concatenate both ways and compare
            if X + Y > Y + X:
                return -1  # X should come before Y
            else:
                return 1  # Y should come before X

        # Sort the array using the custom comparator
        sorted_arr = sorted(arr, key=cmp_to_key(compare))

        # Concatenate the sorted array to form the largest number
        largest_number = ''.join(sorted_arr)

        # Edge case: if the largest number is "0" (e.g., ["0", "0"])
        if largest_number[0] == '0':
            return "0"
        
        return largest_number

# Example usage
solution = Solution()
arr1 = ["3", "30", "34", "5", "9"]
print(solution.printLargest(arr1))  # Output: "9534330"

arr2 = ["54", "546", "548", "60"]
print(solution.printLargest(arr2))  # Output: "6054854654"

arr3 = ["3", "4", "6", "5", "9"]
print(solution.printLargest(arr3))  # Output: "96543"

'''
Here's a line-by-line breakdown of the code:

from functools import cmp_to_key
Imports the cmp_to_key function from Python's functools module. This function allows using a custom comparison function with sorting.

class Solution:
Defines a class named Solution.

def printLargest(self, arr):
Defines a method within the Solution class called printLargest. It takes in two parameters: 
self (the instance of the class) and arr (a list of strings representing numbers).

def compare(X, Y):
Defines a nested function compare to act as a custom comparator for sorting. 
It takes two arguments, X and Y, which represent two numbers as strings.

if X + Y > Y + X:
Concatenates X and Y in two ways (X + Y and Y + X). 
If X + Y is greater than Y + X, it implies that X should come before Y for the largest concatenated number.

return -1
If X + Y is greater, return -1, indicating that X should come before Y in the sorted array.

else:
Executes if X + Y is not greater than Y + X.

return 1
Returns 1, indicating that Y should come before X in the sorted array.

sorted_arr = sorted(arr, key=cmp_to_key(compare))
Sorts the list arr using the custom compare function, converted to a sorting key with cmp_to_key. The sorted list is stored in sorted_arr.

largest_number = ''.join(sorted_arr)
Concatenates all elements in sorted_arr to form a single string, largest_number, which represents the largest possible number from arrangement.

if largest_number[0] == '0':
Checks if the first character of largest_number is "0". This handles cases where all elements in arr are zeros (e.g., ["0", "0"]).

return "0"
If the largest number starts with "0", return "0" instead of multiple zeros, as 0 is the largest possible value in this case.

return largest_number
Returns largest_number, which is the largest possible number that can be formed from the elements of arr.

Example Usage:
solution = Solution()
Creates an instance of the Solution class named solution.

arr1 = ["3", "30", "34", "5", "9"]
Defines a list arr1 with string representations of numbers.

print(solution.printLargest(arr1)) # Output: "9534330"
Calls printLargest on arr1. The output "9534330" is printed, which is the largest possible number that can be formed from arr1.

arr2 = ["54", "546", "548", "60"]
Defines a list arr2 with another set of string representations of numbers.

print(solution.printLargest(arr2)) # Output: "6054854654"
Calls printLargest on arr2. The output "6054854654" is printed, which is the largest possible number that can be formed from arr2.

arr3 = ["3", "4", "6", "5", "9"]
Defines a list arr3.

print(solution.printLargest(arr3)) # Output: "96543"
Calls printLargest on arr3. The output "96543" is printed, which is the largest possible number that can be formed from arr3.

Complexity Analysis
Time Complexity: O(nlogn), where n is the number of strings, because of the sorting step.
Space Complexity: O(n) for storing the sorted array and the result.
'''

