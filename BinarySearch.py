"""
Given a sorted array arr and an integer k, find the position(0-based indexing) at which k is present in the array using binary search.

Examples:

Input: k = 4, arr= [1, 2, 3, 4, 5]  
Output: 3
Explanation: 4 appears at index 3.

Input: k = 445, arr= [11, 22, 33, 44, 55] 
Output: -1
Explanation: 445 is not present.
"""

class Solution:
    def binarysearch(self, arr, k):
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if arr[mid] == k:
                return mid  # Return the index if the element is found
            elif arr[mid] < k:
                left = mid + 1  # Search in the right half
            else:
                right = mid - 1  # Search in the left half
        
        return -1  # Return -1 if the element is not found

# Example usage
s = Solution()
arr1 = [1, 2, 3, 4, 5]
k1 = 4
print(s.binarysearch(arr1, k1))  # Output: 3

arr2 = [11, 22, 33, 44, 55]
k2 = 445
print(s.binarysearch(arr2, k2))  # Output: -1

s = Solution()
print(s.binarysearch([1, 2, 3, 4, 5], 4))  # Output: 3
print(s.binarysearch([11, 22, 33, 44, 55], 445))  # Output: -1

'''
Here's a detailed breakdown of the code:

Class Definition (class Solution:): Defines a class named Solution which contains methods related to the solution of a problem. 
In this case, it includes the binarysearch method.

Method Definition (def binarysearch(self, arr, k):): Defines a method binarysearch within the Solution class. It takes two parameters:
arr: A list of integers where the search is performed.
k: The integer value to search for in the list.

Initialize Variables (left, right = 0, len(arr) - 1): Initializes left to 0 and right to len(arr) - 1. 
These represent the starting and ending indices of the array segment currently being searched.

While Loop (while left <= right:): Continues as long as left is less than or equal to right. This ensures that the search space is not empty.

Calculate Midpoint (mid = (left + right) // 2): Computes the midpoint index of the current search range. 
This index is where the middle element is located.

Condition 1 (if arr[mid] == k:): Checks if the element at index mid is equal to k. 
If so, it returns the index mid, indicating that the element has been found.

Condition 2 (elif arr[mid] < k:): Checks if the middle element is less than k. 
If true, it updates the left index to mid + 1, narrowing the search to the right half of the current segment.

Condition 3 (else:): If the middle element is greater than k, 
it updates the right index to mid - 1, narrowing the search to the left half of the current segment.

Return -1 (return -1): If the while loop completes without finding k, the method returns -1, indicating that the element is not in the array.

Example Usage (s = Solution()): Creates an instance of the Solution class.

First Test Case (print(s.binarysearch(arr1, k1))): Calls binarysearch with arr1 (a list [1, 2, 3, 4, 5]) and k1 (value 4). 
The expected output is 3 because 4 is located at index 3 in a zero-based index system.

Second Test Case (print(s.binarysearch(arr2, k2))): Calls binarysearch with arr2 (a list [11, 22, 33, 44, 55]) and k2 (value 445). 
The expected output is -1 because 445 is not present in the array.

Additional Test Cases: Calls binarysearch again on the same examples to confirm that the results are consistent. 
The outputs for the test cases remain the same as before:

[1, 2, 3, 4, 5] with 4 returns 3.
[11, 22, 33, 44, 55] with 445 returns -1.
'''