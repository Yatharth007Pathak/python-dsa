"""
Given an array arr[] that contains positive and negative integers (may contain 0 as well). 
Find the maximum product that we can get in a subarray of arr.

Note: It is guaranteed that the output fits in a 32-bit integer.

Examples

Input: arr[] = [-2, 6, -3, -10, 0, 2]
Output: 180
Explanation: The subarray with maximum product is {6, -3, -10} with product = 6 * (-3) * (-10) = 180.

Input: arr[] = [-1, -3, -10, 0, 60]
Output: 60
Explanation: The subarray with maximum product is {60}.

Input: arr[] = [2, 3, 4]
Output: 24
Explanation: For an array with all positive elements, the result is product of all elements. 
"""

class Solution:
    # Function to find maximum product subarray
    def maxProduct(self, arr):
        # Initialize the maximum product, minimum product, and result
        max_product = arr[0]
        min_product = arr[0]
        result = arr[0]

        # Traverse the array starting from the second element
        for i in range(1, len(arr)):
            # If current element is negative, swap max_product and min_product
            if arr[i] < 0:
                max_product, min_product = min_product, max_product
            
            # Update max_product and min_product
            max_product = max(arr[i], max_product * arr[i])
            min_product = min(arr[i], min_product * arr[i])

            # Update the result with the maximum product found so far
            result = max(result, max_product)

        return result

# Example inputs
arr1 = [-2, 6, -3, -10, 0, 2]
arr2 = [-1, -3, -10, 0, 60]
arr3 = [2, 3, 4]

# Creating an instance of Solution
solution = Solution()

# Finding maximum product subarray for each example
print(solution.maxProduct(arr1))  # Output: 180
print(solution.maxProduct(arr2))  # Output: 60
print(solution.maxProduct(arr3))  # Output: 24

'''
Here's line-by-line breakdown of the code:

Class Solution:
Defines a class called Solution, which contains methods for solving array-related problems.

Method maxProduct:
Defines a function called maxProduct to find the maximum product of a contiguous subarray in a given array (arr).

Initial Setup in maxProduct:
max_product = arr[0] initializes max_product to the first element of the array. 
This variable will store the maximum product found up to the current position.
min_product = arr[0] initializes min_product to the first element of the array. 
This variable will store the minimum product found up to the current position (helpful in handling negative numbers).
result = arr[0] initializes result to the first element of the array. 
This variable will store the final maximum product of any subarray encountered.

Loop through the Array:
for i in range(1, len(arr)): starts a loop to go through each element in arr, starting from the second element.

Handling Negative Numbers:
if arr[i] < 0: checks if the current element is negative.
max_product, min_product = min_product, max_product swaps max_product and min_product if the current element is negative. 
This is done because multiplying by a negative number could make the maximum product the minimum product and vice versa.

Updating max_product and min_product:
max_product = max(arr[i], max_product * arr[i]) updates max_product to be the maximum of either the current element itself 
or the product of max_product with the current element. This helps in maintaining the largest product possible up to the current index.
min_product = min(arr[i], min_product * arr[i]) updates min_product to be the minimum of either the current element itself 
or the product of min_product with the current element. This helps in maintaining the smallest product 
(useful when a negative number could result in a larger positive product if multiplied by another negative).

Updating the Final Result:
result = max(result, max_product) updates result to be the maximum of result or max_product. 
This ensures that result holds the highest product of any subarray encountered so far.

Returning the Result:
return result returns the maximum product of any subarray in the array.

Example Arrays for Testing:
arr1 = [-2, 6, -3, -10, 0, 2] defines the first test array with mixed values (positive, negative, and zero).
arr2 = [-1, -3, -10, 0, 60] defines the second test array with mostly negative numbers and one large positive value.
arr3 = [2, 3, 4] defines the third test array with all positive values.

Creating an Instance of Solution:
solution = Solution() creates an instance of the Solution class to access its methods.

Calculating Maximum Product Subarrays:
print(solution.maxProduct(arr1)) calls the maxProduct function with arr1 and prints the result, which is expected to be 180.
print(solution.maxProduct(arr2)) calls the maxProduct function with arr2 and prints the result, which is expected to be 60.
print(solution.maxProduct(arr3)) calls the maxProduct function with arr3 and prints the result, which is expected to be 24.
'''