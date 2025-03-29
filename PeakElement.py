"""
Given an 0-indexed array of integers arr[] of size n, find its peak element and return it's index. 
An element is considered to be peak if it's value is greater than or equal to the values of its adjacent elements (if they exist).

Note: The output will be 1 if the index returned by your function is correct; otherwise, it will be 0.

Examples :

Input: n = 3, arr[] = {1, 2, 3} 
Output: 1
Explanation: If the index returned is 2, then the output printed will be 1. Since arr[2] = 3 is greater than its adjacent elements, and there 
is no element after it, we can consider it as a peak element. No other index satisfies the same property, so answer will be printed as 0.

Input: n = 7, arr[] = {1, 1, 1, 2, 1, 1, 1}
Output: 1
Explanation: In this case there are 5 peak elements with indices as {0,1,3,5,6}. Returning any of them will give you correct answer.
"""

class Solution:
    def peakElement(self, arr, n):
        # If the array has only one element, return its index
        if n == 1:
            return 0

        # Check if the first or last element is a peak
        if arr[0] >= arr[1]:
            return 0
        if arr[n - 1] >= arr[n - 2]:
            return n - 1

        # Check the rest of the array
        for i in range(1, n - 1):
            if arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]:
                return i
        
        return -1  # In case no peak is found, though there will always be one

# Test cases
sol = Solution()

# Example 1
arr1 = [1, 2, 3]
n1 = len(arr1)
result1 = sol.peakElement(arr1, n1)
print(1 if result1 == 2 else 0)

# Example 2
arr2 = [1, 1, 1, 2, 1, 1, 1]
n2 = len(arr2)
result2 = sol.peakElement(arr2, n2)
print(1 if result2 in [0, 1, 3, 5, 6] else 0)

'''
Here's a breakdown of the code line by line:

class Solution:
A class named Solution is defined. This class contains the method peakElement, which will be used to find a peak element in an array.

def peakElement(self, arr, n):
A method peakElement is defined inside the class Solution. It takes three parameters: 
self (referring to the instance of the class), arr (the array in which the peak element is to be found), and n (the length of the array).

if n == 1:
This checks if the array contains only one element.

return 0
If the array has only one element, it returns the index 0 since the single element is trivially a peak.

if arr[0] >= arr[1]:
Checks if the first element of the array is a peak. A peak is defined as an element that is not smaller than its neighbors. 
Since the first element has no left neighbor, we only compare it to the second element.

return 0
If the first element is a peak, the method returns 0, the index of the first element.

if arr[n - 1] >= arr[n - 2]:
Checks if the last element is a peak by comparing it to the second-to-last element. 
Since the last element has no right neighbor, we only compare it to the element before it.

return n - 1
If the last element is a peak, the method returns its index, which is n - 1.

for i in range(1, n - 1):
A loop is started that iterates over the rest of the elements (from the second to the second-to-last) in the array.

if arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]:
For each element in the loop, it checks if the element is greater than or equal to both its left and right neighbors. 
If it satisfies this condition, the element is a peak.

return i
If a peak is found during the iteration, the method returns the index of that peak element.

return -1
If no peak is found after iterating through the array, the method returns -1. 
However, this line will never be reached since the problem guarantees that a peak will always exist.

sol = Solution()
Creates an instance of the Solution class.

arr1 = [1, 2, 3]
A sample array arr1 is defined for testing the method.

n1 = len(arr1)
The length of the array arr1 is stored in n1.

result1 = sol.peakElement(arr1, n1)
The peakElement method is called with arr1 and its length n1. The result is stored in result1.

print(1 if result1 == 2 else 0)
Checks if the peak index found is 2 and prints 1 if true, otherwise it prints 0.

arr2 = [1, 1, 1, 2, 1, 1, 1]
Another sample array arr2 is defined for testing the method.

n2 = len(arr2)
The length of the array arr2 is stored in n2.

result2 = sol.peakElement(arr2, n2)
The peakElement method is called with arr2 and its length n2. The result is stored in result2.

print(1 if result2 in [0, 1, 3, 5, 6] else 0)
Checks if the peak index found is in the list [0, 1, 3, 5, 6] and prints 1 if true, otherwise it prints 0.
'''