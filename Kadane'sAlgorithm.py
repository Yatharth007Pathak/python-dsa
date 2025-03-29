"""
Given an integer array arr[]. Find the contiguous sub-array(containing at least one number) that has the maximum sum and return its sum.

Examples:
Input: arr[] = [1, 2, 3, -2, 5]
Output: 9
Explanation: Max subarray sum is 9 of elements (1, 2, 3, -2, 5) which is a contiguous subarray.

Input: arr[] = [-1, -2, -3, -4]
Output: -1
Explanation: Max subarray sum is -1 of element (-1)

Input: arr[] = [2, 3, -8, 7, -1, 2, 3]
Output: 11
Explanation: The subarray (7, -1, 2, 3) has the largest sum 11.

Input: arr[] = [5, 4, 1, 7, 8]
Output: 25
Explanation: The subarray (5, 4, 1, 7, 8) has the largest sum 25.
"""

class Solution:
    # Function to find the sum of the contiguous subarray with the maximum sum.
    def maxSubArraySum(self, arr):
        # Initialize the variables to store the maximum sum found so far and the current sum
        max_sum = float('-inf')  # This will store the maximum sum
        current_sum = 0  # This will store the sum of the current subarray

        for num in arr:
            # Add the current number to the current sum
            current_sum += num

            # If the current sum is greater than max_sum, update max_sum
            if current_sum > max_sum:
                max_sum = current_sum

            # If the current sum is negative, reset it to 0
            # because starting a new subarray from the next element might be more beneficial
            if current_sum < 0:
                current_sum = 0

        return max_sum

# Example Usage:
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
solution = Solution()
print(solution.maxSubArraySum(arr))  # Output will be 6, corresponding to the subarray [4, -1, 2, 1]


'''
To solve this problem, you can use Kadane's Algorithm, which efficiently finds the maximum sum of a contiguous subarray in an array.

Here's a detailed breakdown of the code, line by line:

class Solution:
This line defines a new class called Solution. In Python, classes are used to encapsulate data and methods (functions) that operate on that data.

def maxSubArraySum(self, arr):
This defines a method called maxSubArraySum within the Solution class. The method takes two arguments: 
self (which refers to the instance of the class) and arr, which is the list of integers for which we want to find the maximum subarray sum.

max_sum = float('-inf')
Initializes a variable max_sum to negative infinity. 
This is used to keep track of the maximum sum encountered so far as the algorithm iterates through the array.

current_sum = 0
Initializes current_sum to 0. This variable will store the sum of the current subarray being evaluated.

for num in arr:
Begins a loop that iterates over each element in the array arr. 
The variable num represents the current element in the array during each iteration.

current_sum += num
Adds the current element (num) to current_sum, updating the sum of the current subarray.

if current_sum > max_sum:
Checks if current_sum is greater than max_sum. 
If true, this means the current subarray has a larger sum than any previously encountered, and the algorithm will update max_sum.

max_sum = current_sum
Updates max_sum to the value of current_sum since current_sum is greater than the previous max_sum.

if current_sum < 0:
Checks if current_sum is less than 0. If the sum of the current subarray is negative, 
it's not beneficial to include it in future subarrays, so the sum is reset.

current_sum = 0
Resets current_sum to 0. This means the algorithm will start a new subarray from the next element in the list.

return max_sum
After the loop finishes, the method returns max_sum, which contains the largest sum of any subarray within the input array arr.

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
This line creates a list named arr containing the elements [-2, 1, -3, 4, -1, 2, 1, -5, 4]. 
These are the integers for which the maximum subarray sum will be calculated.

solution = Solution()
Here, an instance of the Solution class is created and stored in the variable solution. 
This allows access to the methods defined in the Solution class, particularly maxSubArraySum.

print(solution.maxSubArraySum(arr))
This line calls the maxSubArraySum method on the solution instance, passing the list arr as an argument.
The method processes the array to find the maximum sum of any subarray within arr.
The result (the maximum subarray sum) is then printed to the console.
'''