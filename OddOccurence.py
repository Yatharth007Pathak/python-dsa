"""
Given an array arr[] of positive integers where every element appears even times except for one. 
Find that number occurring an odd number of times.

Examples:

Input: arr[] = [1, 1, 2, 2, 2]
Output: 2
Explanation: In the given array all element appear two times except 2 which appears thrice.

Input: arr[] = [8, 8, 7, 7, 6, 6, 1]
Output: 1
Explanation: In the given array all element appear two times except 1 which appears once.
"""

class Solution:
    def getSingle(self, arr):
        result = 0
        for num in arr:
            result ^= num  # XOR operation
        return result

# Example usage:
solution = Solution()

# Example 1:
arr1 = [1, 1, 2, 2, 2]
print(solution.getSingle(arr1))  # Output: 2

# Example 2:
arr2 = [8, 8, 7, 7, 6, 6, 1]
print(solution.getSingle(arr2))  # Output: 1

'''
Here's a line-by-line breakdown of the code:

class Solution:
Defines a class Solution, which contains methods to solve a specific problem.

def getSingle(self, arr):
Defines a method getSingle that takes one parameter: arr, which is a list of integers. 
The goal of this method is to find the integer that appears only once in the array while all other integers appear twice.

result = 0
Initializes a variable result to 0. 
This variable will hold the cumulative result of the XOR operation as the method processes each number in the array.

for num in arr:
Starts a loop to iterate through each integer num in the array arr.

result ^= num
Performs the XOR operation between result and num. The XOR operation has the following properties:

a ^ a = 0 (any number XORed with itself is 0)
a ^ 0 = a (any number XORed with 0 is the number itself)
XOR is commutative and associative, meaning the order of operations does not matter.
By XORing all the numbers in the array together, pairs of identical numbers will cancel each other out (resulting in 0), 
and the only number that will remain is the one that appears once.

return result
After processing all numbers in the array, returns the final value of result, which is the integer that appears only once.

Example usage:
solution = Solution()
Creates an instance of the Solution class.
Example 1:
arr1 = [1, 1, 2, 2, 2]
Initializes a list arr1 containing the integers 1, 1, 2, 2, 2.

print(solution.getSingle(arr1))
Calls the getSingle method with arr1 and prints the result. The output is 2, as 2 appears once while 1 appears twice.

Example 2:
arr2 = [8, 8, 7, 7, 6, 6, 1]
Initializes a list arr2 containing the integers 8, 8, 7, 7, 6, 6, 1.

print(solution.getSingle(arr2))
Calls the getSingle method with arr2 and prints the result. The output is 1, as 1 appears once while 8, 7, and 6 appear twice.




Example Walkthrough:
Example 1:
Input: [1, 1, 2, 2, 2]
XOR Calculation:
0⊕1=1
1⊕1=0 (the two 1s cancel out)
0⊕2=2
2⊕2=0 (the two 2s cancel out)
0⊕2=2 (result is 2, which appears thrice)
Output: 2

Example 2:
Input: [8, 8, 7, 7, 6, 6, 1]
XOR Calculation:
0⊕8=8
8⊕8=0 (the two 8s cancel out)
0⊕7=7
7⊕7=0 (the two 7s cancel out)
0⊕6=6
6⊕6=0 (the two 6s cancel out)
0⊕1=1 (result is 1, which appears once)
Output: 1

Time Complexity:
O(n), where n is the number of elements in the array. We go through the array once.

Space Complexity:
O(1), as we use a constant amount of space for the result variabl
'''