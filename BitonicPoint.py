"""
Given an array arr of n elements that is first strictly increasing and then maybe strictly decreasing, 
find the bitonic point, that is the maximum element in the array.
Bitonic Point is a point before which elements are strictly increasing and after which elements are strictly decreasing.
Note: If the array is increasing then just print the last element will be the maximum value.

Examples:

Input: n = 7, arr[] = [1, 2, 4, 5, 7, 8, 3]
Output: 8
Explanation: Elements before 8 are strictly increasing [1, 2, 4, 5, 7] and elements after 8 are strictly decreasing [3].

Input: n = 5, arr[] = [10, 20, 30, 40, 50]
Output: 50
Explanation: Elements before 50 are strictly increasing [10, 20, 30 40] and there are no elements after 50.

Input: n = 5, arr[] = [120, 100, 80, 20, 0]
Output: 120
Explanation: There are no elements before 120 and elements after 120 are strictly decreasing [100, 80, 20, 0].

"""

class Solution:
    def findMaximum(self, arr, n):
        # If the array is empty
        if n == 0:
            return None
        
        # If the array has only one element
        if n == 1:
            return arr[0]
        
        left, right = 0, n - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            # Compare middle element with its next element
            if arr[mid] > arr[mid + 1]:
                # If mid is greater than next element, then peak lies on the left side (including mid)
                right = mid
            else:
                # If mid is less than or equal to next element, peak lies on the right side (excluding mid)
                left = mid + 1
        
        # left will be pointing to the maximum element
        return arr[left]

# Example usage
sol = Solution()
print(sol.findMaximum([1, 15, 25, 45, 42, 21, 17, 12, 11], 9))  # Output: 45
print(sol.findMaximum([1, 45, 47, 50, 5], 5))  # Output: 50

'''
Code Breakdown

class Solution:
Class Definition: Defines a class named Solution. This class will contain methods related to solving problems.

def findMaximum(self, arr, n):
Method Definition: Defines a method findMaximum that takes two parameters:
arr: a list of integers (the array in which we want to find the maximum).
n: an integer representing the number of elements in the array.

# If the array is empty
if n == 0:
    return None
Check for Empty Array:
If n is 0 (meaning the array is empty), the function returns None.

# If the array has only one element
if n == 1:
    return arr[0]
Check for Single Element:
If n is 1, the function returns the only element in the array, arr[0].

left, right = 0, n - 1
Initialize Pointers:
Two pointers, left and right, are initialized. left starts at the beginning of the array (index 0) and right starts at the last index (n - 1).

while left < right:
Loop Condition:
The loop continues as long as left is less than right. This means we will keep narrowing down our search until left meets right.

mid = left + (right - left) // 2
Calculate Midpoint:
The midpoint index mid is calculated using the formula left + (right - left) // 2. 
This helps avoid overflow that can occur with (left + right) // 2.

# Compare middle element with its next element
if arr[mid] > arr[mid + 1]:
Comparison:
This condition checks if the middle element arr[mid] is greater than the next element arr[mid + 1].

# If mid is greater than next element, then peak lies on the left side (including mid)
right = mid
Adjust Right Pointer:
If arr[mid] is greater than arr[mid + 1], it indicates that the peak (maximum element) lies to the left of mid, including mid. 
Hence, we update right to mid.

else:
    # If mid is less than or equal to next element, peak lies on the right side (excluding mid)
    left = mid + 1
Adjust Left Pointer:
If arr[mid] is less than or equal to arr[mid + 1], it indicates that the peak lies to the right of mid, excluding mid. 
Hence, we update left to mid + 1.

# left will be pointing to the maximum element
return arr[left]
Return Maximum:
Once the loop exits, left will be pointing to the maximum element in the array. The function returns arr[left].

sol = Solution()
Create an Instance: An instance of the Solution class is created and assigned to sol.

print(sol.findMaximum([1, 15, 25, 45, 42, 21, 17, 12, 11], 9))  # Output: 45
Function Call: The findMaximum method is called with an example array. It prints the output, which is 45, the maximum element in the array.

print(sol.findMaximum([1, 45, 47, 50, 5], 5))  # Output: 50
Another Function Call: The method is called again with a different array, and it prints 50, the maximum element in this case.
'''