"""
Given an array of elements arr[] with indices ranging from 0 to arr.size() - 1, your task is to write a program that rearranges the elements
of the array such that arr[i] = i. If an element i is not present in the array, -1 should be placed at the corresponding index.

Examples:

Input: arr[] = [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]
Output: [-1, 1, 2, 3, 4, -1, 6, -1, -1, 9]
Explanation: Here We can see there are 10 elements. So, the sorted array will look like [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 
but in our array we are not having 0, 5, 7 and 8. So, at there places we will be printing -1 and otherplaces will be having elements.

Input: arr[] = [2, 0, 1]
Output: [0, 1, 2]
Explanation: Here We can see all the elements are present so no -1 is returned in array.
"""


class Solution:
    def rearrange(self, arr):
        # Create a result array initialized with -1
        result = [-1] * len(arr)
        
        # Traverse the input array
        for num in arr:
            # Place the number in its corresponding index if valid
            if 0 <= num < len(arr):
                result[num] = num
        
        return result

# Example usage
sol = Solution()
print(sol.rearrange([-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]))  # Output: [-1, 1, 2, 3, 4, -1, 6, -1, -1, 9]
print(sol.rearrange([2, 0, 1]))  # Output: [0, 1, 2]

'''
The rearrange method repositions each valid number from the input array arr into the result array at the index corresponding to its value. 
If a number cannot be placed at its index (either because it is negative or exceeds the array bounds), the index remains -1. 
The method ensures an organized result with elements at their respective indices if possible.


Let's break down the code that rearranges an array such that each element is placed at its corresponding index if possible, 
and -1 is used for invalid positions.

class Solution:
Defines a class Solution that encapsulates the method rearrange.

def rearrange(self, arr):
This defines the method rearrange, which takes a list arr as input and returns a rearranged list.

result = [-1] * len(arr)
Initializes a new array result of the same length as arr, filled with -1. This result array will store the rearranged elements. 
Initially, all elements are set to -1.

for num in arr:
Iterates through each element num in the input array arr.

if 0 <= num < len(arr):
This checks if num is a valid index in the array. It ensures that num is a non-negative integer and less than the length of the array.

result[num] = num
If num is a valid index, it places num at the corresponding index num in the result array.

return result
After the loop finishes, the method returns the result array, where valid numbers are placed at their respective indices, 
and invalid positions remain as -1.

sol = Solution()
Creates an instance of the Solution class.

print(sol.rearrange([-1, -1, 6, 1, 9, 3, 2, -1, 4, -1]))
Calls the rearrange method with the array [-1, -1, 6, 1, 9, 3, 2, -1, 4, -1].
The expected output is [-1, 1, 2, 3, 4, -1, 6, -1, -1, 9] because:
1 is placed at index 1,
2 is placed at index 2,
3 is placed at index 3,
4 is placed at index 4,
6 is placed at index 6,
9 is placed at index 9.

print(sol.rearrange([2, 0, 1]))
Calls the rearrange method with the array [2, 0, 1].
The expected output is [0, 1, 2] because:
0 is placed at index 0,
1 is placed at index 1,
2 is placed at index 2.
'''