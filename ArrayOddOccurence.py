"""
Given an array of N positive integers where all numbers occur even number of times except one number which occurs odd number of times. 
Find the exceptional number.

Example 1:
Input: N = 7, Arr[] = {1, 2, 3, 2, 3, 1, 3}
Output: 3
Explaination: 3 occurs three times.

Example 2:
Input: N = 7, Arr[] = {5, 7, 2, 7, 5, 2, 5}
Output: 5
Explaination: 5 occurs three times.
"""

class Solution:
    def getOddOccurrence(self, arr, n):
        result = 0
        for num in arr:
            result ^= num  # XOR all the elements in the array
        return result

# Example usage:
solution = Solution()
print(solution.getOddOccurrence([1, 2, 3, 2, 3, 1, 3], 7))  # Output: 3
print(solution.getOddOccurrence([5, 7, 2, 7, 5, 2, 5], 7))  # Output: 5

'''
Here's a breakdown of how the code works:

Define class Solution: A class named Solution is defined with a method getOddOccurrence 
to find the element that appears an odd number of times in the given array.

Define getOddOccurrence method:
The method getOddOccurrence(self, arr, n) takes two input parameters:
arr: The array of integers where exactly one element occurs an odd number of times.
n: The length of the array (not necessarily needed for the operation, but included for reference).

XOR operation:
XOR Basics: The XOR (^) operation has some key properties:
x ^ x = 0 (any number XORed with itself results in 0).
x ^ 0 = x (any number XORed with 0 remains unchanged).
XOR is commutative and associative, so the order of XOR operations doesn't matter.

Method logic:
The variable result is initialized to 0.
The method loops through each element in the array and applies the XOR operation (result ^= num) for each number num in arr.
Numbers that occur an even number of times will cancel out (because x ^ x = 0), 
and only the number that occurs an odd number of times will remain.

Return the result: After XORing all the elements, the method returns result, which is the number that appears an odd number of times.

Example usage:

Example 1 (arr = [1, 2, 3, 2, 3, 1, 3]): The XOR process looks like:
result = 0 ^ 1 ^ 2 ^ 3 ^ 2 ^ 3 ^ 1 ^ 3
The pairs of 1s, 2s, and 3s cancel out, leaving only 3, which appears an odd number of times. The output is 3.

Example 2 (arr = [5, 7, 2, 7, 5, 2, 5]): The XOR process is:
result = 0 ^ 5 ^ 7 ^ 2 ^ 7 ^ 5 ^ 2 ^ 5
The pairs of 5s, 7s, and 2s cancel out, leaving 5, which appears an odd number of times. The output is 5.
'''