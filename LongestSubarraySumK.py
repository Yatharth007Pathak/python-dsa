"""
Given an array arr containing n integers and an integer k. 
Your task is to find the length of the longest Sub-Array with the sum of the elements equal to the given value k.

Examples:

Input : n = 6, arr[] = {10, 5, 2, 7, 1, 9}, k = 15
Output : 4
Explanation: The sub-array is {5, 2, 7, 1}.

Input : n= 3, arr[] = {-1, 2, 3}, k = 6
Output : 0
Explanation: There is no such sub-array with sum 6.
"""

class Solution:
    def lenOfLongSubarr(self, arr, n, k):
        # Dictionary to store (prefix_sum, index)
        sum_index_map = {}
        max_len = 0
        current_sum = 0
        
        for i in range(n):
            # Add the current element to the cumulative sum
            current_sum += arr[i]
            
            # If the cumulative sum equals k, we found a subarray from the start
            if current_sum == k:
                max_len = i + 1
            
            # If current_sum - k is in the map, there exists a subarray with sum k
            if (current_sum - k) in sum_index_map:
                max_len = max(max_len, i - sum_index_map[current_sum - k])
            
            # Only store the current sum index if it's not already in the map
            if current_sum not in sum_index_map:
                sum_index_map[current_sum] = i
        
        return max_len

# Test cases
if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    arr1 = [10, 5, 2, 7, 1, 9]
    k1 = 15
    print(solution.lenOfLongSubarr(arr1, len(arr1), k1))

    # Test case 2
    arr2 = [-1, 2, 3]
    k2 = 6
    print(solution.lenOfLongSubarr(arr2, len(arr2), k2))

    # Test case 3
    arr3 = [1, 2, 3, 4, 5]
    k3 = 9
    print(solution.lenOfLongSubarr(arr3, len(arr3), k3))

    # Test case 4
    arr4 = [1, -1, 5, -2, 3]
    k4 = 3
    print(solution.lenOfLongSubarr(arr4, len(arr4), k4))

    # Test case 5
    arr5 = [3, 1, 0, 1, 8, 2, 3, 6]
    k5 = 5
    print(solution.lenOfLongSubarr(arr5, len(arr5), k5))

    # Test case 6
    arr6 = [1, 2, 3]
    k6 = 3
    print(solution.lenOfLongSubarr(arr6, len(arr6), k6))

'''
Line-by-Line Breakdown

class Solution:
This defines a class named Solution.

def lenOfLongSubarr(self, arr, n, k):
This defines a method lenOfLongSubarr within Solution. It takes three parameters:
arr: the input array of integers.
n: the length of the array.
k: the target sum for which we need to find the longest subarray.

sum_index_map = {}
Initializes an empty dictionary sum_index_map to store cumulative sums and their earliest occurrence indices. 
This helps in quickly finding subarrays with a specified sum.

max_len = 0
Initializes max_len to 0, which will store the length of the longest subarray that has a sum of k.

current_sum = 0
Initializes current_sum to 0, which will keep a cumulative sum of elements as we traverse the array.

for i in range(n):
Starts a loop to iterate through each index i in the array.

current_sum += arr[i]
Adds the current element arr[i] to current_sum, updating the cumulative sum up to the current index.

if current_sum == k:
Checks if current_sum is exactly equal to k. 
If true, this means the subarray from the beginning (index 0) to the current index i has a sum of k.

max_len = i + 1
If current_sum == k, the length of this subarray is i + 1, so max_len is updated to i + 1.

if (current_sum - k) in sum_index_map:
Checks if current_sum - k exists in sum_index_map. If it does, 
then there exists an earlier index j such that the sum of elements from j + 1 to i equals k.

max_len = max(max_len, i - sum_index_map[current_sum - k])
Updates max_len to the maximum of its current value and the length of the subarray from sum_index_map[current_sum - k] + 1 to i.

if current_sum not in sum_index_map:
Checks if current_sum is not already in sum_index_map. This ensures only the earliest occurrence of each cumulative sum is recorded.

sum_index_map[current_sum] = i
Stores current_sum in sum_index_map with its corresponding index i.

return max_len
After iterating through the array, returns max_len, which now contains the length of the longest subarray with a sum of k.

Example Usage:
Each test case provides an array arr and a target sum k and then calls lenOfLongSubarr to find the longest subarray with a sum of k.

Test Case 1: [10, 5, 2, 7, 1, 9], k = 15. Expected output: 4 (longest subarray [5, 2, 7, 1]).
Test Case 2: [-1, 2, 3], k = 6. Expected output: 0 (no subarray sums to 6).
Test Case 3: [1, 2, 3, 4, 5], k = 9. Expected output: 3 (longest subarray [2, 3, 4]).
Test Case 4: [1, -1, 5, -2, 3], k = 3. Expected output: 4 (longest subarray [1, -1, 5, -2]).
Test Case 5: [3, 1, 0, 1, 8, 2, 3, 6], k = 5. Expected output: 4 (longest subarray [1, 0, 1, 8]).
Test Case 6: [1, 2, 3], k = 3. Expected output: 2 (longest subarray [1, 2]).
'''