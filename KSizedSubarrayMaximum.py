"""
Given an array arr[] and an integer k. Find the maximum for each and every contiguous subarray of size k.

Examples:

Input: k = 3, arr[] = [1, 2, 3, 1, 4, 5, 2, 3, 6]
Output: [3, 3, 4, 5, 5, 5, 6] 
Explanation: 
1st contiguous subarray = [1 2 3] max = 3
2nd contiguous subarray = [2 3 1] max = 3
3rd contiguous subarray = [3 1 4] max = 4
4th contiguous subarray = [1 4 5] max = 5
5th contiguous subarray = [4 5 2] max = 5
6th contiguous subarray = [5 2 3] max = 5
7th contiguous subarray = [2 3 6] max = 6

Input: k = 4, arr[] = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
Output: [10, 10, 10, 15, 15, 90, 90]
Explanation: 
1st contiguous subarray = [8 5 10 7], max = 10
2nd contiguous subarray = [5 10 7 9], max = 10
3rd contiguous subarray = [10 7 9 4], max = 10
4th contiguous subarray = [7 9 4 15], max = 15
5th contiguous subarray = [9 4 15 12], max = 15
6th contiguous subarray = [4 15 12 90], max = 90
7th contiguous subarray = {15 12 90 13}, max = 90
"""

from collections import deque

class Solution:
    # Function to find maximum of each subarray of size k
    def maxOfSubarrays(self, arr, k):
        result = []
        q = deque()
        
        for i in range(len(arr)):
            # Remove elements that are out of this window
            if q and q[0] <= i - k:
                q.popleft()
            
            # Remove elements smaller than the current element from the deque
            while q and arr[q[-1]] <= arr[i]:
                q.pop()
            
            # Add the current element's index to the deque
            q.append(i)
            
            # Once we have processed the first k elements, the maximum for the window is at the front of the deque
            if i >= k - 1:
                result.append(arr[q[0]])
        
        return result

solution = Solution()

# Example 1
arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
k = 3
print(solution.maxOfSubarrays(arr, k))  # Output: [3, 3, 4, 5, 5, 5, 6]

# Example 2
arr = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13]
k = 4
print(solution.maxOfSubarrays(arr, k))  # Output: [10, 10, 10, 15, 15, 90, 90]

# Example 3
arr = [5, 1, 3, 4, 2, 6]
k = 1
print(solution.maxOfSubarrays(arr, k))  # Output: [5, 1, 3, 4, 2, 6]

'''
Explanation of the Code:

from collections import deque
Imports the deque class from the collections module. A deque allows efficient appending and popping of elements from both ends, 
which is useful for implementing the sliding window.

class Solution:
Defines a class Solution that contains the method maxOfSubarrays.

def maxOfSubarrays(self, arr, k):
Defines the method maxOfSubarrays, which takes an array arr and an integer k as input and returns the maximum of each subarray of size k.

result = []
Initializes an empty list result to store the maximums of each subarray.

q = deque()
Initializes an empty deque q to keep track of indices of elements in the current sliding window. 
This deque will help efficiently find the maximum value in each window.

for i in range(len(arr)):
Loops through each element of the array by index i.

if q and q[0] <= i - k:
Checks if the element at the front of the deque is out of the current window (i.e., its index is older than k positions ago).
If true, the element is removed from the front of the deque using q.popleft().

while q and arr[q[-1]] <= arr[i]:
Removes elements from the back of the deque while the current element is greater than or equal to the element at the back of the deque.
This ensures that the deque always stores indices of elements in decreasing order.

q.append(i)
Adds the index of the current element to the deque.

if i >= k - 1:
Once the first k elements have been processed, the window is complete.
The condition i >= k - 1 ensures that we start appending the maximums to the result list.

result.append(arr[q[0]])
Appends the value of the element at the front of the deque to the result list.
This is the maximum of the current window because the deque stores indices of elements 
in decreasing order, with the largest element at the front.

return result
Returns the result list containing the maximums of each subarray of size k.

Example 1:
Input: arr = [1, 2, 3, 1, 4, 5, 2, 3, 6], k = 3
Step-by-Step:
Window 1: [1, 2, 3] → Max: 3
Window 2: [2, 3, 1] → Max: 3
Window 3: [3, 1, 4] → Max: 4
Window 4: [1, 4, 5] → Max: 5
Window 5: [4, 5, 2] → Max: 5
Window 6: [5, 2, 3] → Max: 5
Window 7: [2, 3, 6] → Max: 6
Output: [3, 3, 4, 5, 5, 5, 6]

Example 2:
Input: arr = [8, 5, 10, 7, 9, 4, 15, 12, 90, 13], k = 4
Step-by-Step:
Window 1: [8, 5, 10, 7] → Max: 10
Window 2: [5, 10, 7, 9] → Max: 10
Window 3: [10, 7, 9, 4] → Max: 10
Window 4: [7, 9, 4, 15] → Max: 15
Window 5: [9, 4, 15, 12] → Max: 15
Window 6: [4, 15, 12, 90] → Max: 90
Window 7: [15, 12, 90, 13] → Max: 90
Output: [10, 10, 10, 15, 15, 90, 90]

Example 3:
Input: arr = [5, 1, 3, 4, 2, 6], k = 1
Step-by-Step:
Since k = 1, each element is its own subarray.
Therefore, the maximum of each subarray is the element itself.
Output: [5, 1, 3, 4, 2, 6]
'''