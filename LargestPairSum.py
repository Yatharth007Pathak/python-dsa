"""
Find the largest pair sum in an array of distinct integers.

Examples :

Input: arr[] = [12, 34, 10, 6, 40]
Output: 74
Explanation: Sum of 34 and 40 is the largest, i.e, 34 + 40 = 74.

Input: arr[] = [10, 20, 30]
Output: 50
Explanation: 20 + 30 = 50.
"""

from typing import List

class Solution:
    def pairsum(self, arr: List[int]) -> int:
        # Sort the array in descending order
        arr.sort(reverse=True)
        # Return the sum of the first two elements
        return arr[0] + arr[1]

# Example usage
sol = Solution()
print(sol.pairsum([12, 34, 10, 6, 40]))  # Output: 74
print(sol.pairsum([10, 20, 30]))          # Output: 50

'''
Code Breakdown

from typing import List
This line imports the List type from the typing module, allowing us to specify that the function will take a list of integers as input.

class Solution:
This line defines a new class named Solution. In Python, classes are used to encapsulate data and functions that operate on that data.

def pairsum(self, arr: List[int]) -> int:
This line defines a method named pairsum within the Solution class.
self refers to the instance of the class, allowing access to its properties and methods.
arr: List[int] indicates that arr is expected to be a list of integers.
-> int specifies that the method will return an integer.

# Sort the array in descending order
This comment explains the purpose of the next line of code, which is to sort the input array.

arr.sort(reverse=True)
This line sorts the arr list in-place in descending order.
The reverse=True argument specifies that the sorting should be done in reverse order (highest to lowest).

# Return the sum of the first two elements
This comment indicates that the next line of code will return the sum of the two largest numbers in the sorted array.

return arr[0] + arr[1]
This line returns the sum of the first two elements of the sorted array (arr[0] and arr[1]), which are largest numbers due to the sorting step.

# Example usage
This comment marks the beginning of an example usage section to demonstrate how to use the pairsum method.

sol = Solution()
This line creates an instance of Solution class and assigns it to the variable sol. This instance can now be used to call the pairsum method.

print(sol.pairsum([12, 34, 10, 6, 40])) # Output: 74
This line calls the pairsum method on the sol instance, passing in a list of integers. The result is printed to the console.
In this case, the two largest numbers are 40 and 34, and their sum is 74.

print(sol.pairsum([10, 20, 30])) # Output: 50
This line calls the pairsum method again with a different list of integers. The result is printed to the console.
Here, the two largest numbers are 30 and 20, and their sum is 50.
'''