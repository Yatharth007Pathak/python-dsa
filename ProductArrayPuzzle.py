"""
Given an array nums[], construct a Product Array nums[] such that nums[i] is equal to the product of all the elements of nums except nums[i].

Examples:

Input: nums[] = [10, 3, 5, 6, 2]
Output: [180, 600, 360, 300, 900]
Explanation: For i=0, P[i] = 3*5*6*2 = 180.
For i=1, P[i] = 10*5*6*2 = 600.
For i=2, P[i] = 10*3*6*2 = 360.
For i=3, P[i] = 10*3*5*2 = 300.
For i=4, P[i] = 10*3*5*6 = 900.

Input: nums[] = [12,0]
Output: [0, 12]
"""

class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        
        # Initialize the result array with 1s
        result = [1] * n
        
        # Compute left product for each index
        left_product = 1
        for i in range(n):
            result[i] = left_product
            left_product *= nums[i]
        
        # Compute right product for each index and multiply with the result array
        right_product = 1
        for i in range(n-1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]
        
        return result

# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    nums1 = [10, 3, 5, 6, 2]
    result1 = sol.productExceptSelf(nums1)
    print(f"Output for nums1 = {nums1}: {result1}")
    
    # Test case 2
    nums2 = [12, 0]
    result2 = sol.productExceptSelf(nums2)
    print(f"Output for nums2 = {nums2}: {result2}")

'''

Here's a line-by-line breakdown of the productExceptSelf function:

Function Definition

class Solution:
Defines the Solution class, which contains the method productExceptSelf.

def productExceptSelf(self, nums):
A method that calculates the product of all elements in the list nums, except for the element at the current index, without using division.

Initialization

n = len(nums)
Stores the length of the input list nums in n.

result = [1] * n
Initializes an array result of length n where every element is initially set to 1. 
This array will hold the final product result for each index.

Compute Left Products

left_product = 1
Initializes a variable left_product to 1. This will store the cumulative product of elements to the left of the current index.

for i in range(n):
Loops through each index i of the nums array from left to right.

result[i] = left_product
At each index i, assigns left_product to result[i]. Initially, this value is 1, and it will be updated as we move through the loop.

left_product *= nums[i]
Updates left_product by multiplying it with the current element nums[i]. 
This ensures that left_product always holds the product of all elements to the left of the current index for the next iteration.

Compute Right Products and Final Result

right_product = 1
Initializes a variable right_product to 1. This will store the cumulative product of elements to the right of the current index.

for i in range(n-1, -1, -1):
Loops through each index i of the nums array from right to left (starting from the last element and going towards the first).

result[i] *= right_product
Multiplies result[i] by right_product. This gives the final result for each index, incorporating both the left and right products.

right_product *= nums[i]
Updates right_product by multiplying it with the current element nums[i]. 
This ensures that right_product always holds the product of all elements to the right of the current index for the next iteration.

Return Statement

return result
Returns the final result array containing the product of all elements except the current one for each index.

Test Cases

if __name__ == "__main__":
This block ensures that the test cases will only run when the script is executed directly.

Test case 1
nums1 = [10, 3, 5, 6, 2]: First test case input list.
result1 = sol.productExceptSelf(nums1): Calls the productExceptSelf method and stores the result in result1.
print(f"Output for nums1 = {nums1}: {result1}"): Prints the result for the first test case.

Test case 2
nums2 = [12, 0]: Second test case input list.
result2 = sol.productExceptSelf(nums2): Calls the productExceptSelf method and stores the result in result2.
print(f"Output for nums2 = {nums2}: {result2}"): Prints the result for the second test case.

Example Output:
For nums1 = [10, 3, 5, 6, 2], the output is: [180, 600, 360, 300, 900].
For nums2 = [12, 0], the output is: [0, 12].

Time Complexity:
O(n), where n is the number of elements in the input list nums. We traverse the list twice (once for left products and once for right products).
This algorithm efficiently computes the product for all elements except the current one without using division, 
ensuring that it works even when there are zeros in the input.
'''