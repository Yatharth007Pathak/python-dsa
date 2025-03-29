"""
You are given an array arr of size n - 1 that contains distinct integers in the range from 1 to n (inclusive). 
This array represents a permutation of the integers from 1 to n with one element missing. 
Your task is to identify and return the missing element.

Examples:

Input: arr[] = [1, 2, 3, 5]
Output: 4
Explanation: All the numbers from 1 to 5 are present except 4.

Input: arr[] = [8, 2, 4, 5, 3, 7, 1]
Output: 6
Explanation: All the numbers from 1 to 8 are present except 6.

Input: arr[] = [1]
Output: 2
Explanation: Only 1 is present so the missing element is 2.
"""

class Solution:
    def missingNumber(self, arr):
        n = len(arr) + 1  # The size of the complete array should be n
        total_sum = n * (n + 1) // 2  # Sum of all numbers from 1 to n
        actual_sum = sum(arr)  # Sum of the given array
        return total_sum - actual_sum  # The missing number is the difference

# Examples
solution = Solution()
print(solution.missingNumber([1, 2, 3, 5]))  # Output: 4
print(solution.missingNumber([8, 2, 4, 5, 3, 7, 1]))  # Output: 6
print(solution.missingNumber([1]))  # Output: 2

'''
Here's a line-by-line explanation in plain text:

class Solution:
Defines a class named Solution to group the function that calculates the missing number.

def missingNumber(self, arr):
Declares a method missingNumber inside the class. This method takes two parameters: self (refers to the class instance) and arr (the input array of numbers).

n = len(arr) + 1
Calculates the total number of elements that should be in the array if no number were missing. Adds 1 because the array is missing exactly one number.

total_sum = n * (n + 1) // 2
Computes the sum of all integers from 1 to n using the formula for the sum of the first n natural numbers: Sum= n(n+1)/2

actual_sum = sum(arr)
Calculates the sum of the elements in the input array arr.

return total_sum - actual_sum
Finds the missing number by subtracting the sum of the elements in the array (actual_sum) from the expected total sum (total_sum).

Examples:

solution = Solution()
Creates an instance of the Solution class.

print(solution.missingNumber([1, 2, 3, 5]))
Calls the missingNumber method with the array [1, 2, 3, 5].
Explanation:
n = 5
total_sum = 15 (sum of numbers 1 to 5)
actual_sum = 11 (sum of [1, 2, 3, 5])
Missing number = 15 - 11 = 4
Output: 4.

print(solution.missingNumber([8, 2, 4, 5, 3, 7, 1]))
Calls the missingNumber method with the array [8, 2, 4, 5, 3, 7, 1].
Explanation:
n = 8
total_sum = 36 (sum of numbers 1 to 8)
actual_sum = 30 (sum of [8, 2, 4, 5, 3, 7, 1])
Missing number = 36 - 30 = 6
Output: 6.

print(solution.missingNumber([1]))
Calls the missingNumber method with the array [1].
Explanation:
n = 2
total_sum = 3 (sum of numbers 1 to 2)
actual_sum = 1 (sum of [1])
Missing number = 3 - 1 = 2
Output: 2.
'''