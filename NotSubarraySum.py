"""
Given a sorted array arr[] of positive integers, 
find the smallest positive integer such that it cannot be represented as the sum of elements of any subset of the given array set.

Examples:

Input: arr[] = [1, 2, 3]
Output: 7
Explanation: 7 is the smallest positive number for which no subset is there with sum 7.

Input: arr[] = [3, 6, 9, 10, 20, 28]
Output: 1
Explanation: 1 is the smallest positive number for which no subset is there with sum 1.
"""

class Solution:
    def findSmallest(self, arr):
        # Initialize the smallest number we can't achieve as 1
        result = 1
        
        # Traverse the array
        for num in arr:
            # If the current number is greater than 'result', 
            # it means we cannot achieve 'result' using any subset
            if num > result:
                break
            # Otherwise, add the number to 'result'
            result += num
        
        return result

# Example usage:
sol = Solution()
print(sol.findSmallest([1, 2, 3]))  # Output: 7
print(sol.findSmallest([3, 6, 9, 10, 20, 28]))  # Output: 1

'''
Here's a pointwise explanation for each line of the given code:

class Solution:
Defines a class named Solution.

def findSmallest(self, arr):
Defines a function named findSmallest that takes a list arr as an argument, 
used to find the smallest positive integer that cannot be represented as the sum of a subset of elements in arr.

result = 1
Initializes result to 1, representing the smallest number that cannot yet be formed from any subset of arr.

for num in arr:
Starts a for loop to iterate over each element num in arr.

if num > result:
Checks if the current number num is greater than result. If true, it means we cannot form the value result using any subset, 
as num is larger than the current result.

break
If num is greater than result, breaks out of the loop since the smallest unachievable value has been found.

result += num
If num is less than or equal to result, adds num to result to extend the range of numbers that can be formed.

return result
Returns the value of result, which is the smallest positive integer that cannot be represented as the sum of a subset of elements in arr.

# Example usage:
Adds a comment indicating the start of the example usage of the function.

sol = Solution()
Creates an instance of the Solution class.

print(sol.findSmallest([1, 2, 3])) # Output: 7
Calls findSmallest with the array [1, 2, 3] and prints the result, which is 7.

print(sol.findSmallest([3, 6, 9, 10, 20, 28])) # Output: 1
Calls findSmallest with the array [3, 6, 9, 10, 20, 28] and prints the result, which is 1.
'''