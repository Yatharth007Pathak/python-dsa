"""
Given an array arr[] of positive integers and an integer k, Your task is to return k largest elements in decreasing order. 

Examples

Input: arr[] = [12, 5, 787, 1, 23], k = 2
Output: [787, 23]
Explanation: 1st largest element in the array is 787 and second largest is 23.

Input: arr[] = [1, 23, 12, 9, 30, 2, 50], k = 3 
Output: [50, 30, 23]
Explanation: Three Largest elements in the array are 50, 30 and 23.

Input: arr[] = [12, 23], k = 1
Output: [23]
Explanation: 1st Largest element in the array is 23.
"""

class Solution:
    def kLargest(self, arr, k):
        # Sort the array in descending order
        sorted_arr = sorted(arr, reverse=True)
        
        # Return the first k elements
        return sorted_arr[:k]

# Example usage
solution = Solution()
arr1 = [12, 5, 787, 1, 23]
k1 = 2
print(solution.kLargest(arr1, k1))  # Output: [787, 23]

arr2 = [1, 23, 12, 9, 30, 2, 50]
k2 = 3
print(solution.kLargest(arr2, k2))  # Output: [50, 30, 23]

arr3 = [12, 23]
k3 = 1
print(solution.kLargest(arr3, k3))  # Output: [23]

'''
Here's a line-by-line breakdown of the code:

class Solution:
Defines a class named Solution.

def kLargest(self, arr, k):
Defines a method within the Solution class named kLargest. This method takes in three parameters: self (the instance of the class), 
arr (the input list of numbers), and k (the number of largest elements to find).

sorted_arr = sorted(arr, reverse=True)
Sorts the input list arr in descending order (from largest to smallest) using the sorted() function, 
with reverse=True to achieve descending order. The sorted list is stored in sorted_arr.

return sorted_arr[:k]
Returns the first k elements of sorted_arr by slicing it as sorted_arr[:k]. These elements are the largest k values in the array.

Example Usage:
solution = Solution()
Creates an instance of the Solution class called solution.

arr1 = [12, 5, 787, 1, 23]
Defines a list arr1 with several integers.

k1 = 2
Sets k1 to 2, meaning we want the two largest elements from arr1.

print(solution.kLargest(arr1, k1)) # Output: [787, 23]
Calls the kLargest method with arr1 and k1. The output [787, 23] is printed, showing the two largest elements in arr1.

arr2 = [1, 23, 12, 9, 30, 2, 50]
Defines another list arr2 with a different set of integers.

k2 = 3
Sets k2 to 3, meaning we want the three largest elements from arr2.

print(solution.kLargest(arr2, k2)) # Output: [50, 30, 23]
Calls the kLargest method with arr2 and k2. The output [50, 30, 23] is printed, showing the three largest elements in arr2.

arr3 = [12, 23]
Defines a third list arr3.

k3 = 1
Sets k3 to 1, meaning we want the single largest element from arr3.

print(solution.kLargest(arr3, k3)) # Output: [23]
Calls the kLargest method with arr3 and k3. The output [23] is printed, showing the single largest element in arr3.

Explanation
Sorting: sorted(arr, reverse=True) sorts the array in descending order.
Slicing: sorted_arr[:k] retrieves the first k elements, which are the largest elements in descending order.

Complexity Analysis
Time Complexity: O(nlogn), where n is the length of the array, due to the sorting operation.
Space Complexity: O(n), needed to store the sorted array.
'''