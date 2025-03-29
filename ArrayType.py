"""
You are given an array arr having unique elements. Your task is to return the type of array.
Note: The array can be categorized into ascending, descending, descending rotated and ascending rotated followed by:
Return 1 if the array is in ascending order
Return 2 if the array is in descending order
Return 3 if the array is in descending rotated order
Return 4 if the array is in ascending rotated order

Examples:

Input: arr[] = [2, 1, 5, 4, 3]
Output: 3
Explanation: Descending rotated, rotate 2 times left.

Input: arr[] = [3, 4, 5, 1, 2]
Output: 4
Explanation: Ascending rotated, rotate 2 times right. 
"""

class Solution:
    def maxNtype(self, arr):
        n = len(arr)
        
        # Check if array is in ascending order
        if arr == sorted(arr):
            return 1
        
        # Check if array is in descending order
        elif arr == sorted(arr, reverse=True):
            return 2
        
        # Check if array is in ascending rotated order
        elif arr[0] > arr[-1]:
            # Find the pivot where rotation happened (smallest element)
            min_index = arr.index(min(arr))
            if arr[min_index:] + arr[:min_index] == sorted(arr):
                return 4
        
        # Check if array is in descending rotated order
        elif arr[0] < arr[-1]:
            # Find the pivot where rotation happened (largest element)
            max_index = arr.index(max(arr))
            if arr[max_index:] + arr[:max_index] == sorted(arr, reverse=True):
                return 3
        
        return 0  # In case it doesn't match any of the categories

# Example usage
sol = Solution()
print(sol.maxNtype([2, 1, 5, 4, 3]))  # Output: 3 (Descending rotated)
print(sol.maxNtype([3, 4, 5, 1, 2]))  # Output: 4 (Ascending rotated)

'''
Here's a line-by-line breakdown of the code:

class Solution:
This defines a class named Solution which will contain the method maxNtype.

def maxNtype(self, arr):
This defines the method maxNtype inside the class, which takes one argument arr (the array to be checked for order/rotation type) 
and self (which refers to the instance of the class).

n = len(arr)
This calculates the length of the array arr and stores it in the variable n. 
This value might be useful in checking conditions or performing operations on the array.

if arr == sorted(arr):
This checks if the array arr is already sorted in ascending order by comparing arr to sorted(arr) (which returns a sorted version of the array).

return 1
If the array is in ascending order, the method returns 1.

elif arr == sorted(arr, reverse=True):
This checks if the array arr is sorted in descending order by comparing it to sorted(arr, reverse=True), 
which sorts the array in descending order.

return 2
If the array is in descending order, the method returns 2.

elif arr[0] > arr[-1]:
This checks if the array might be in ascending rotated order by comparing the first element (arr[0]) to the last element (arr[-1]). 
In an ascending rotated array, the first element should be greater than the last element.

min_index = arr.index(min(arr))
This finds the index of the smallest element in the array, which is the point where the array was "rotated" (the pivot).

if arr[min_index:] + arr[:min_index] == sorted(arr):
This checks if rearranging the array by moving the elements after 
the pivot to the front and before the pivot to the back results in a sorted array. This verifies if the array is in ascending rotated order.

return 4
If the array is in ascending rotated order, the method returns 4.

elif arr[0] < arr[-1]:
This checks if the array might be in descending rotated order by comparing the first element (arr[0]) to the last element (arr[-1]). 
In a descending rotated array, the first element should be smaller than the last element.

max_index = arr.index(max(arr))
This finds the index of the largest element in the array, which would be the pivot point where the array was rotated.

if arr[max_index:] + arr[:max_index] == sorted(arr, reverse=True):
This checks if rearranging the array by moving the elements after the pivot to the front and 
before the pivot to the back results in a descending sorted array. This confirms if the array is in descending rotated order.

return 3
If the array is in descending rotated order, the method returns 3.

return 0
If none of the above conditions match, meaning the array doesn't fit any of the four categories 
(ascending, descending, ascending rotated, or descending rotated), the method returns 0.

Example usage:
sol = Solution()
This creates an instance of the Solution class named sol.

print(sol.maxNtype([2, 1, 5, 4, 3]))
This calls the maxNtype method on the array [2, 1, 5, 4, 3], which is a descending rotated array. The output is 3.

print(sol.maxNtype([3, 4, 5, 1, 2]))
This calls the maxNtype method on the array [3, 4, 5, 1, 2], which is an ascending rotated array. The output is 4.
'''