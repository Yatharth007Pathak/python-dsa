"""
Given an unsorted array arr containing only non-negative integers, your task is to find a continuous subarray 
(a contiguous sequence of elements) whose sum equals a specified value target. You need to return the 1-based indices of 
the leftmost and rightmost elements of this subarray.

Examples:

Input: arr[] = [1,2,3,7,5], target = 12
Output: [2, 4]
Explanation: The sum of elements from 2nd to 4th position is 12.

Input: arr[] = [1,2,3,4,5,6,7,8,9,10], target = 15,
Output: [1, 5]
Explanation: The sum of elements from 1st to 5th position is 15.

Input: arr[] = [7,2,1], target = 2
Output: [2, 2]
Explanation: The sum of elements from 2nd to 2nd position is 2.

Input: arr[] = [5,3,4], target = 2
Output: [-1]
Explanation: There is no subarray with sum 2.
"""

class Solution:
    def subArraySum(self, arr, target):
        n = len(arr)
        left = 0
        current_sum = 0

        for right in range(n):
            # Add the current element to the current sum
            current_sum += arr[right]

            # While the current sum exceeds the target, move the left pointer
            while current_sum > target and left <= right:
                current_sum -= arr[left]
                left += 1

            # Check if the current sum equals the target
            if current_sum == target:
                return [left + 1, right + 1]  # Convert to 1-based indices

        # If no subarray is found, return [-1]
        return [-1]

# Examples
solution = Solution()
print(solution.subArraySum([1, 2, 3, 7, 5], 12))  # Output: [2, 4]
print(solution.subArraySum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15))  # Output: [1, 5]
print(solution.subArraySum([7, 2, 1], 2))  # Output: [2, 2]
print(solution.subArraySum([5, 3, 4], 2))  # Output: [-1]

'''
Here's a line-by-line explanation of the code:

class Solution:
Defines a class named Solution to group the function that solves the problem.

def subArraySum(self, arr, target):
Declares a method subArraySum inside the class. This method takes three parameters: self (refers to the class instance), 
arr (the input array), and target (the target sum to find).

n = len(arr)
Calculates the length of the input array arr and stores it in n.

left = 0
Initializes a pointer left to 0, representing the start of the current subarray.

current_sum = 0
Initializes a variable current_sum to 0, which will store the sum of the current subarray.

for right in range(n):
Starts a loop with right as the index, iterating through all elements of the array.

current_sum += arr[right]
Adds the element at the right index to current_sum.

while current_sum > target and left <= right:
Enters a loop to shrink the subarray from the left while current_sum is greater than the target and left does not exceed right.

current_sum -= arr[left]
Subtracts the element at the left index from current_sum.

left += 1
Moves the left pointer one step to the right to exclude the leftmost element of the current subarray.

if current_sum == target:
Checks if current_sum is equal to the target sum.

return [left + 1, right + 1]
Returns a list with the start and end indices of the subarray (converted to 1-based indexing).

return [-1]
If the loop completes and no subarray is found, returns [-1] to indicate failure.

solution = Solution()
Creates an instance of the Solution class.

print(solution.subArraySum([1, 2, 3, 7, 5], 12))
Calls subArraySum with the array [1, 2, 3, 7, 5] and target 12. The expected output is [2, 4].

print(solution.subArraySum([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 15))
Calls subArraySum with the array [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] and target 15. The expected output is [1, 5].

print(solution.subArraySum([7, 2, 1], 2))
Calls subArraySum with the array [7, 2, 1] and target 2. The expected output is [2, 2].

print(solution.subArraySum([5, 3, 4], 2))
Calls subArraySum with the array [5, 3, 4] and target 2. The expected output is [-1].
'''