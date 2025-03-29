"""
Given an array of integers arr[] of size N, the task is to find the maximum of the minimum values 
for every possible window size in the array, where the window size ranges from 1 to N.

More formally, for each window size k, determine the smallest element in all windows of size k, 
and then find the largest value among these minimums where 1<=k<=N.

Examples :

Input: arr[] = [10, 20, 30, 50, 10, 70, 30]
Output: [70, 30, 20, 10, 10, 10, 10] 
Explanation: 
1. First element in output indicates maximum of minimums of all windows of size 1.
2. Minimums of windows of size 1 are [10], [20], [30], [50], [10], [70] and [30]. Maximum of these minimums is 70. 
3. Second element in output indicates maximum of minimums of all windows of size 2. 
4. Minimums of windows of size 2 are [10], [20], [30], [10], [10], and [30].
5. Maximum of these minimums is 30 Third element in output indicates maximum of minimums of all windows of size 3. 
6. Minimums of windows of size 3 are [10], [20], [10], [10] and [10].
7. Maximum of these minimums is 20. Similarly other elements of output are computed.

Input: arr[] = [10, 20, 30]
Output: [30, 20, 10]
Explanation: First element in output indicates maximum of minimums of all windows of size 1. 
Minimums of windows of size 1 are [10] , [20] , [30]. Maximum of these minimums are 30 and similarly other outputs can be computed
"""

class Solution:
    def maxOfMin(self, arr):
        n = len(arr)

        # Arrays to store previous and next smaller elements
        prev_smaller = [-1] * n
        next_smaller = [n] * n

        # Monotonic stack for previous smaller
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                prev_smaller[i] = stack[-1]
            stack.append(i)

        # Monotonic stack for next smaller
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                next_smaller[i] = stack[-1]
            stack.append(i)

        # Result array to store the maximum of minimums
        result = [0] * (n + 1)

        # Fill result using the boundaries
        for i in range(n):
            # Calculate the length of the window
            length = next_smaller[i] - prev_smaller[i] - 1
            result[length] = max(result[length], arr[i])

        # Fill the rest of the result array
        for i in range(n - 1, 0, -1):
            result[i] = max(result[i], result[i + 1])

        # Return result[1:] as result[0] is not used
        return result[1:]

sol = Solution()
arr = [10, 20, 30, 50, 10, 70, 30]
print(sol.maxOfMin(arr))  # Output: [70, 30, 20, 10, 10, 10, 10]

arr = [10, 20, 30]
print(sol.maxOfMin(arr))  # Output: [30, 20, 10]

'''

Here's a plain-text breakdown of the code:

class Solution:
Defines a class Solution to implement the solution for finding the maximum of minimums of all window sizes in an array.

def maxOfMin(self, arr):
Defines the method maxOfMin, which takes an array arr as input.

n = len(arr)
Stores the length of the array.

prev_smaller = [-1] * n
Creates an array prev_smaller to store the index of the previous smaller element for each element.
Initializes it to -1 (no previous smaller).

next_smaller = [n] * n
Creates an array next_smaller to store the index of the next smaller element for each element.
Initializes it to n (no next smaller).

stack = []
Initializes an empty stack to help find the previous smaller elements.

for i in range(n):
Iterates through the array from left to right.

while stack and arr[stack[-1]] >= arr[i]:
Pops elements from the stack until the top element is smaller than the current element.

if stack:
Updates prev_smaller[i] with the index of the previous smaller element if the stack is not empty.

stack.append(i)
Pushes the current index onto the stack.

stack = []
Reinitializes the stack to find the next smaller elements.

for i in range(n - 1, -1, -1):
Iterates through the array from right to left.

while stack and arr[stack[-1]] >= arr[i]:
Pops elements from the stack until the top element is smaller than the current element.

if stack:
Updates next_smaller[i] with the index of the next smaller element if the stack is not empty.

stack.append(i)
Pushes the current index onto the stack.

result = [0] * (n + 1)
Initializes a result array of size n + 1 to store the maximum of minimums for all window sizes.

for i in range(n):
Iterates through the array to compute the maximum of minimums.

length = next_smaller[i] - prev_smaller[i] - 1
Calculates the size of the window where the current element is the minimum.

result[length] = max(result[length], arr[i])
Updates the result for the window size by taking the maximum of the current and the stored value.

for i in range(n - 1, 0, -1):
Iterates from the second last to the first index in the result array.

result[i] = max(result[i], result[i + 1])
Ensures that results for smaller windows propagate correctly.

return result[1:]
Returns the result from index 1 onward since index 0 is not used.

arr = [10, 20, 30, 50, 10, 70, 30]
Defines an input array.

print(sol.maxOfMin(arr))
Calls the maxOfMin method and prints the output.
Output: [70, 30, 20, 10, 10, 10, 10]
Explanation: Maximum of minimums for all window sizes is computed.

arr = [10, 20, 30]
Defines another input array.

print(sol.maxOfMin(arr))
Calls the maxOfMin method and prints the output.
Output: [30, 20, 10]
Explanation: Maximum of minimums for all window sizes is computed.
'''