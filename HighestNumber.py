"""
Given an integer array a[] of size n, find the highest element of the array. 
The array will either be strictly increasing or strictly increasing and then strictly decreasing.
Note: a[i] != a[i+1] 

Example 1:
Input: 11, 1 2 3 4 5 6 5 4 3 2 1
Output: 6
Explanation: Highest element of array a[] is 6.

Example 2:
Input: 5, 1 2 3 4 5
Output: 5
Explanation: Highest element of array a[] is 5.
"""

from typing import List

class Solution:
    def findPeakElement(self, a: List[int]) -> int:
        n = len(a)
        
        # If the array is empty
        if n == 0:
            return None
        
        # If the array has only one element
        if n == 1:
            return a[0]
        
        left, right = 0, n - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            # Compare middle element with its next element
            if a[mid] > a[mid + 1]:
                # If mid is greater than next element, the peak lies on the left side (including mid)
                right = mid
            else:
                # If mid is less than next element, the peak lies on the right side (excluding mid)
                left = mid + 1
        
        # left will be pointing to the maximum element
        return a[left]

# Example usage
sol = Solution()
print(sol.findPeakElement([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]))  # Output: 6
print(sol.findPeakElement([1, 2, 3, 4, 5]))  # Output: 5

'''
Here's a line-by-line breakdown of the code:

from typing import List
This line imports the List type from the typing module, which allows for type hinting with lists in the code.

class Solution:
Defines a class named Solution. This is a common practice in coding challenges to encapsulate the solution methods.

def findPeakElement(self, a: List[int]) -> int:
This line defines a method named findPeakElement within the Solution class. It takes two parameters:
self: a reference to the current instance of the class.
a: a list of integers (annotated as List[int]), which represents the input array.
The method is expected to return an integer (-> int).

n = len(a)
This line calculates the length of the input list a and assigns it to the variable n.

if n == 0:
    return None
Checks if the list is empty. If it is, the method returns None.

if n == 1:
    return a[0]
Checks if the list has only one element. If it does, the method returns that single element as it is the peak.

left, right = 0, n - 1
Initializes two pointers, left and right, to denote the range of indices being considered. 
left is set to 0 (the start of the list), and right is set to n - 1 (the last index of the list).

while left < right:
Starts a while loop that continues as long as left is less than right.

mid = left + (right - left) // 2
Calculates the middle index mid of the current range using integer division. 
This helps to avoid overflow issues when calculating the middle index.

if a[mid] > a[mid + 1]:
Compares the element at the mid index with the element at the mid + 1 index.

right = mid
If the element at mid is greater than the next element, it implies that the peak must be on the left side (including mid). 
Thus, it updates right to mid.

else:
    left = mid + 1
If the element at mid is not greater than the next element, it implies that the peak must be on the right side (excluding mid). 
Thus, it updates left to mid + 1.

return a[left]
After exiting the loop, the method returns the element at the left index, which will be pointing to a peak element in the array.

sol = Solution()
Creates an instance of the Solution class and assigns it to the variable sol.

print(sol.findPeakElement([1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]))  # Output: 6
Calls the findPeakElement method on the sol instance with a sample input list. 
It prints the output, which should be 6, as it is the peak in the given list.

print(sol.findPeakElement([1, 2, 3, 4, 5]))  # Output: 5
Calls the findPeakElement method again with another sample input list and prints the output, which should be 5, 
as it is the peak in the ascending list.
'''