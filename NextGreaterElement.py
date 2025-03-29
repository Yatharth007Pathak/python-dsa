"""
Given an array arr[ ] of integers, the task is to find the next greater element for each element of array in order of their appearance in 
the array. Next greater element of an element in the array is the nearest element on the right which is greater than the current element.
If there does not exist next greater of current element, then next greater element for current element is -1. 
For example, next greater of the last element is always -1.

Examples

Input: arr[] = [1, 3, 2, 4]
Output: [3, 4, 4, -1]
Explanation: The next larger element to 1 is 3, 3 is 4, 2 is 4 and for 4, since it doesn't exist, it is -1.

Input: arr[] = [6, 8, 0, 1, 3]
Output: [8, -1, 1, 3, -1]
Explanation: The next larger element to 6 is 8, for 8 there is no larger elements hence it is -1, for 0 it is 1 , 
for 1 it is 3 and then for 3 there is no larger element on right and hence -1.

Input: arr[] = [10, 20, 30, 50]
Output: [20, 30, 50, -1]
Explanation: For a sorted array, the next element is next greater element also exxept for the last element.

Input: arr[] = [50, 40, 30, 10]
Output: [-1, -1, -1, -1]
Explanation: There is no greater element for any of the elements in the array, so all are -1.
"""

class Solution:
    # Function to find the next greater element for each element of the array.
    def nextLargerElement(self, arr):
        # Initialize an empty stack and a result array filled with -1
        stack = []
        result = [-1] * len(arr)

        # Traverse the array from the end to the beginning
        for i in range(len(arr) - 1, -1, -1):
            # Pop elements from the stack that are smaller than or equal to arr[i]
            while stack and stack[-1] <= arr[i]:
                stack.pop()
                
            # If the stack is not empty, the top element is the next greater element
            if stack:
                result[i] = stack[-1]
            
            # Push the current element to the stack
            stack.append(arr[i])

        return result

solution = Solution()

# Test Case 1
arr = [1, 3, 2, 4]
print(solution.nextLargerElement(arr))  # Expected Output: [3, 4, 4, -1]

# Test Case 2
arr = [6, 8, 0, 1, 3]
print(solution.nextLargerElement(arr))  # Expected Output: [8, -1, 1, 3, -1]

# Test Case 3
arr = [10, 20, 30, 50]
print(solution.nextLargerElement(arr))  # Expected Output: [20, 30, 50, -1]

# Test Case 4
arr = [50, 40, 30, 10]
print(solution.nextLargerElement(arr))  # Expected Output: [-1, -1, -1, -1]

'''
Explanation:

Using a Stack:
A stack is used to keep track of elements in the array, which helps in efficiently finding the next greater element for each position.

Traversing from Right to Left:
We iterate from the end of the array to the beginning. 
This allows us to find the next greater element on the right side for each element as we go.

Pop Smaller or Equal Elements:
For each element arr[i], we pop elements from the stack that are smaller than or equal to arr[i], 
as they cannot be the "next greater element" for this or any earlier elements.

Set the Next Greater Element:
If the stack is not empty after popping, the top element of the stack is the next greater element for arr[i]. Otherwise, it remains -1.

Push the Current Element:
The current element is pushed onto the stack to serve as a potential "next greater" for future elements to the left.

Complexity Analysis:
Time Complexity: O(n), where n is the length of the array. Each element is pushed and popped from the stack once.
Space Complexity: O(n) for the result array and the stack.

Example Walkthrough:
For the array [1, 3, 2, 4]:
Start from the last element 4: No greater element to the right, so result is [-1].
Move to 2: The next greater element is 4.
Move to 3: The next greater element is 4.
Move to 1: The next greater element is 3.
Final output: [3, 4, 4, -1]

Test Cases:
Case 1: [1, 3, 2, 4] -> [3, 4, 4, -1]
Case 2: [6, 8, 0, 1, 3] -> [8, -1, 1, 3, -1]
Case 3: [10, 20, 30, 50] -> [20, 30, 50, -1]
Case 4: [50, 40, 30, 10] -> [-1, -1, -1, -1]
'''