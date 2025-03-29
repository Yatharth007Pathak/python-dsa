"""
Given an array arr[] of N elements and a number K., split the given array into K subarrays such that the maximum subarray sum 
achievable out of K subarrays formed is minimum possible. Find that possible subarray sum.

Example 1:
Input: N = 4, K = 3, arr[] = {1, 2, 3, 4}
Output: 4
Explanation: Optimal Split is {1, 2}, {3}, {4}. Maximum sum of all subarrays is 4, which is minimum possible for 3 splits. 

Example 2:
Input: N = 3, K = 2, A[] = {1, 1, 2}
Output: 2
Explanation: Splitting the array as {1,1} and {2} is optimal. This results in a maximum sum subarray of 2.
"""

class Solution:
    def splitArray(self, arr, N, K):
        def isPossible(mid):
            count = 1  # Number of subarrays needed
            current_sum = 0

            for num in arr:
                if current_sum + num > mid:
                    # Start a new subarray
                    count += 1
                    current_sum = num
                    if count > K:  # More subarrays than allowed
                        return False
                else:
                    current_sum += num
            return True

        # Binary search for the minimum possible largest sum
        low, high = max(arr), sum(arr)
        result = high

        while low <= high:
            mid = (low + high) // 2
            if isPossible(mid):
                result = mid  # Update result if current mid is valid
                high = mid - 1
            else:
                low = mid + 1

        return result

    def printSplitArrayResult(self, arr, K):
        N = len(arr)
        result = self.splitArray(arr, N, K)
        print(f"The minimum possible maximum subarray sum for {K} splits is: {result}")


# Example usage
solution = Solution()

# Test case 1
arr1 = [1, 2, 3, 4]
K1 = 3
solution.printSplitArrayResult(arr1, K1)

# Test case 2
arr2 = [1, 1, 2]
K2 = 2
solution.printSplitArrayResult(arr2, K2)

'''
Here's a detailed explanation of the splitArray function and its operation:

Function: splitArray
Parameters
arr: The input array.
N: Length of the array.
K: Number of subarrays to split into.

Subfunction: isPossible
This helper function checks whether a given maximum subarray sum (mid) is achievable with at most K subarrays.

Logic of isPossible(mid)

Initialize:
count = 1: Start with one subarray.
current_sum = 0: Current sum of the ongoing subarray.

Traverse the array:
Add the current element to current_sum.
If adding the current element exceeds mid, start a new subarray:
Increment count.
Reset current_sum to the current element.
If the number of subarrays exceeds K, return False.

Return True if the split is valid.

Binary Search to Find the Optimal Maximum Sum

Binary Search Variables
low = max(arr): The minimum possible largest sum is the largest element (e.g., in [1, 2, 3, 4], low = 4).
high = sum(arr): The maximum possible largest sum is the sum of all elements (e.g., in [1, 2, 3, 4], high = 10).
result = high: Stores the smallest valid maximum sum found during the binary search.

Binary Search Process
Compute the midpoint mid = (low + high) // 2.
Check if splitting the array with mid as the maximum subarray sum is possible using isPossible(mid):

If True:
Update result = mid (valid solution found).
Search for a smaller valid maximum sum by setting high = mid - 1.

If False:
Search for a larger valid maximum sum by setting low = mid + 1.

End Condition
When the loop ends, result contains the minimum possible largest subarray sum.

Function: printSplitArrayResult
Combines splitArray with test outputs:
Calculates the result using splitArray.
Prints the formatted result.

Execution of Test Cases

Test Case 1
Input: arr1 = [1, 2, 3, 4], K1 = 3
Process:
Possible splits:
[1], [2], [3, 4] → Max sum = 7
[1, 2], [3], [4] → Max sum = 4
Output: The minimum possible maximum subarray sum: 4.

Test Case 2
Input: arr2 = [1, 1, 2], K2 = 2
Process:
Possible splits:
[1, 1], [2] → Max sum = 2
[1], [1, 2] → Max sum = 3
Output: The minimum possible maximum subarray sum: 2.

Printed Outputs
For Test Case 1: "The minimum possible maximum subarray sum for 3 splits is: 4"
For Test Case 2: "The minimum possible maximum subarray sum for 2 splits is: 2"
'''