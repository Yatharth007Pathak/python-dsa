"""
You are given an integer array arr[]. Your task is to find the smallest positive number missing from the array.
Note: Positive number starts from 1. The array can have negative integers too.

Examples:

Input: arr[] = [1, 2, 3, 4, 5]
Output: 6
Explanation: Smallest positive missing number is 6.

Input: arr[] = [0, -10, 1, 3, -20]
Output: 2
Explanation: Smallest positive missing number is 2.
"""

class Solution:
    
    # Function to find the smallest positive number missing from the array.
    def missingNumber(self, arr):
        n = len(arr)
        
        # Step 1: Segregate positive and non-positive numbers
        # Move all non-positive numbers to the left side
        j = 0
        for i in range(n):
            if arr[i] <= 0:
                arr[i], arr[j] = arr[j], arr[i]
                j += 1
        
        # Now, arr[j:] contains only positive numbers
        # Step 2: Mark the positions of positive numbers
        return self.findMissingPositive(arr[j:], n - j)
    
    # Helper function to find missing positive number in a positive subarray
    def findMissingPositive(self, arr, size):
        for i in range(size):
            val = abs(arr[i])
            if val - 1 < size and arr[val - 1] > 0:
                arr[val - 1] = -arr[val - 1]
        
        # Step 3: Find the first index with a positive value
        for i in range(size):
            if arr[i] > 0:
                return i + 1
        
        # If all indices are marked, the missing number is size + 1
        return size + 1

# Example usage:
solution = Solution()
arr1 = [1, 2, 3, 4, 5]
arr2 = [0, -10, 1, 3, -20]
print(solution.missingNumber(arr1))  # Output: 6
print(solution.missingNumber(arr2))  # Output: 2

'''
Here's a line-by-line breakdown of the code:

class Solution:
Defines the Solution class.

def missingNumber(self, arr):
Defines the function missingNumber, which takes arr (an array of integers) and finds the smallest positive missing number.

n = len(arr):
n stores the length of the array.

j = 0:
Initializes j, which will be used to segregate positive and non-positive numbers in the array.

for i in range(n):
Starts a loop to iterate through the array.

if arr[i] <= 0:
Checks if the current element is non-positive (i.e., less than or equal to 0).

arr[i], arr[j] = arr[j], arr[i]:
If a non-positive element is found, it is swapped with the element at index j, effectively moving it to the left side of the array.

j += 1:
After a swap, j is incremented to track the position of the next non-positive number.

return self.findMissingPositive(arr[j:], n - j):
After segregating the array, the findMissingPositive function is called with the subarray arr[j:] 
(which contains only positive numbers) and its size n - j. 
This function will identify the smallest missing positive number from this positive subarray.

Helper Function:
def findMissingPositive(self, arr, size):
Defines the helper function findMissingPositive, which takes a positive subarray and its size as input 
and finds the missing smallest positive number.

for i in range(size):
Loops through the positive subarray.

val = abs(arr[i]):
Takes the absolute value of the current element in the array.

if val - 1 < size and arr[val - 1] > 0:
Checks if the value val lies within the range of the array (i.e., val - 1 is a valid index) and if the value at that index is positive. 
This ensures that only valid positions within the array are marked.

arr[val - 1] = -arr[val - 1]:
Marks the position corresponding to val by negating the value at index val - 1, indicating that val exists in the array.

for i in range(size):
After marking positions, another loop is started to find the first unmarked position.

if arr[i] > 0:
If a positive value is found at index i, it means the number i + 1 is missing from the array.

return i + 1:
Returns the smallest missing positive number as i + 1.

return size + 1:
If all positions are marked, it means the array contains all numbers from 1 to size, so the smallest missing positive number is size + 1.
Example Usage:
solution = Solution():
Creates an instance of the Solution class.

arr1 = [1, 2, 3, 4, 5]:
Test case 1: The array contains consecutive positive numbers.

arr2 = [0, -10, 1, 3, -20]:
Test case 2: The array contains non-positive numbers and missing positive numbers.

print(solution.missingNumber(arr1)):
Calls missingNumber on arr1 and prints the result. The output is 6, since the array has all numbers from 1 to 5, 
and the smallest missing number is 6.

print(solution.missingNumber(arr2)):
Calls missingNumber on arr2 and prints the result. The output is 2, since 2 is the smallest missing positive number in this array.
'''