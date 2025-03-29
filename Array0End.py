"""
Given an array arr[] of n positive integers. Push all the zeros of the given array to the right end of the array 
while maintaining the order of non-zero elements. Do the mentioned change in the array in-place.

Examples:

Input: n = 8, arr[] = [1, 2, 0, 4, 3, 0, 5, 0]
Output: [1, 2, 4, 3, 5, 0, 0, 0]
Explanation: There are three 0s that are moved to the end.

Input: n = 3, arr[] = [10, 20, 30]
Output: [10, 20, 30]
Explanation: No change in array as there are no 0s.

Input: n = 2, arr[] = [0, 0]
Output: [0, 0]
Explanation: No change in array as there are all 0s.
"""

class Solution:
    def pushZerosToEnd(self, arr, n):
        # Pointer to track the position of the next non-zero element
        non_zero_pos = 0

        # Traverse the array
        for i in range(n):
            if arr[i] != 0:
                # Swap the non-zero element with the element at non_zero_pos
                arr[non_zero_pos], arr[i] = arr[i], arr[non_zero_pos]
                non_zero_pos += 1

# Example usage:
solution = Solution()
arr = [3, 5, 0, 0, 4]
solution.pushZerosToEnd(arr, len(arr))
print(arr)  # Output: [3, 5, 4, 0, 0]


'''
Here's a breakdown of the code line by line, explained in a pointwise manner:

class Solution:
This defines a class named Solution. The class will contain methods to solve specific problems, in this case, 
pushing all zeros in an array to the end.

def pushZerosToEnd(self, arr, n):
This defines a method named pushZerosToEnd inside the Solution class.
It takes three parameters: self (the instance of the class), arr (a list of integers), 
and n (an integer representing the number of elements in the list).

non_zero_pos = 0
This initializes a variable non_zero_pos to 0.
This variable keeps track of the position where the next non-zero element should be placed in the array.

for i in range(n):
This starts a for loop to iterate over each index i from 0 to n-1 in the array arr.

if arr[i] != 0:
This checks if the element at index i in the array arr is not zero. If the element is non-zero, the following block is executed.

arr[non_zero_pos], arr[i] = arr[i], arr[non_zero_pos]
If the element is non-zero, it swaps the element at index i with the element at index non_zero_pos.
This effectively moves the non-zero element to the front of the array (at position non_zero_pos).

non_zero_pos += 1
After the swap, non_zero_pos is incremented by 1 to update the position for the next non-zero element.

# Example usage:
This comment indicates the beginning of an example that shows how to use the pushZerosToEnd method.

solution = Solution()
This creates an instance of the Solution class.

arr = [3, 5, 0, 0, 4]
This initializes an array arr with the elements [3, 5, 0, 0, 4].

solution.pushZerosToEnd(arr, len(arr))
This calls the pushZerosToEnd method on the solution instance, passing the array arr and its length len(arr) as arguments.

print(arr) # Output: [3, 5, 4, 0, 0]
This prints the modified array arr after all zeros have been moved to the end.
The expected output is [3, 5, 4, 0, 0].
'''