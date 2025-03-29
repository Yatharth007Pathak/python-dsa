"""
Given an array arr[] containing positive elements. A and B are two numbers defining a range. 
The task is to check if the array contains all elements in the given range (inclusive).

Note: If the array contains all elements in the given range return true otherwise return false.

Examples :

Input: n = 7, A = 2, B = 5, arr[] =  {1, 4, 5, 2, 7, 8, 3}
Output: True
Explanation: It has all elements between range 2-5 i.e 2,3,4,5.

Input: n = 7, A = 2, B = 6, arr[] = {1, 4, 5, 2, 7, 8, 3}
Output: False
Explanation: The array does not contain 6 hence it do not contains all elements in the range 2-6, the output is No.
"""

class Solution:
    def check_elements(self, arr, n, A, B):
        # Create a set from the array to remove duplicates and for efficient lookup
        elements_set = set(arr)
        
        # Check if every number from A to B is present in the set
        for num in range(A, B + 1):
            if num not in elements_set:
                return False  # Return False as soon as we find a missing number
        
        return True  # All numbers are present

sol = Solution()

# Test Case 1
arr1 = [1, 4, 5, 2, 7, 8, 3]
print(sol.check_elements(arr1, len(arr1), 2, 5))  # Output: True

# Test Case 2
arr2 = [1, 4, 5, 2, 7, 8, 3]
print(sol.check_elements(arr2, len(arr2), 2, 6))  # Output: False

'''
Here's a detailed line-by-line breakdown of the given code:

Class Definition
class Solution:
This defines a class named Solution. Classes in Python are used to group related methods and data together, 
providing structure and organization to the code.

Method Definition
def check_elements(self, arr, n, A, B):
This line defines a method check_elements inside the Solution class. The method takes the following parameters:
self: Refers to the instance of the class.
arr: The array (or list) that contains the elements.
n: The length of the array arr (though not actually used in this method).
A and B: These define the range of numbers we want to check for their presence in the array.

Creating a Set from the Array
elements_set = set(arr)
This line converts the list arr into a set called elements_set. 
A set automatically removes duplicates and allows for fast lookup operations, making it efficient for checking if a number exists in it.

Checking for Numbers in the Range
for num in range(A, B + 1):
This initiates a loop that iterates over each number from A to B (inclusive). 
The range(A, B + 1) function generates numbers from A to B (since the range function is exclusive of the upper limit, 
B + 1 ensures that B is included).

if num not in elements_set:
Inside the loop, for each number num, this line checks if the number is not present in the elements_set. 
If the number is missing, it means that the array arr does not contain all numbers in the range from A to B.

return False
If the loop finds that a number in the range is missing from elements_set, this line immediately returns False, 
indicating that not all numbers from A to B are present in the array.

Returning True if All Numbers Are Present
return True
If the loop completes without finding any missing numbers, this line returns True, 
meaning all numbers in the range from A to B were found in the array.

Object Instantiation
sol = Solution()
This creates an instance of the Solution class and assigns it to the variable sol. 
You can now use this instance to call the method check_elements.

Test Case 1
arr1 = [1, 4, 5, 2, 7, 8, 3]
Defines a list arr1 containing integers.

print(sol.check_elements(arr1, len(arr1), 2, 5))
This calls the check_elements method on the arr1 array, checking if all numbers between 2 and 5 (inclusive) are present in the array.
The output here is True since the numbers 2, 3, 4, and 5 are all in arr1.

Test Case 2
arr2 = [1, 4, 5, 2, 7, 8, 3]
Defines another list arr2 containing integers (identical to arr1).

print(sol.check_elements(arr2, len(arr2), 2, 6))
This calls the check_elements method on arr2, but this time it checks if all numbers from 2 to 6 (inclusive) are present. 
The output is False because the number 6 is missing in arr2.
'''