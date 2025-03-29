"""
Given an array arr[] of N positive integers. Find an integer denoting the maximum XOR subset value in the given array arr[].

Example 1:
Input : N = 3, arr[] = {2, 4, 5}
Output : 7
Explanation : The subset {2, 5} has maximum subset XOR value.

Example 2 :
Input : N= 3, arr[] = {9, 8, 5}
Output : 13
Explanation : The subset {8, 5} has maximum subset XOR value.
"""

class Solution:
    def maxSubsetXOR(self, arr, N):
        # Initialize index for basis elements
        index = 0
        
        # Process each bit from MSB to LSB
        for bit in range(31, -1, -1):  # Assuming 32-bit integers
            # Find the maximum element with the current bit set
            max_idx = index
            max_ele = -1
            for i in range(index, N):
                if (arr[i] & (1 << bit)) != 0 and arr[i] > max_ele:
                    max_ele = arr[i]
                    max_idx = i
            
            # If no element with the current bit set, skip this bit
            if max_ele == -1:
                continue
            
            # Swap to move the chosen element to the "basis" position
            arr[index], arr[max_idx] = arr[max_idx], arr[index]
            
            # XOR all other numbers having the current bit set
            for i in range(N):
                if i != index and (arr[i] & (1 << bit)) != 0:
                    arr[i] ^= arr[index]
            
            # Move to the next basis position
            index += 1
        
        # XOR of all basis elements gives the maximum XOR
        max_xor = 0
        for i in range(index):
            max_xor ^= arr[i]
        
        return max_xor

# Example 1
solution = Solution()
arr = [2, 4, 5]
N = 3
print(solution.maxSubsetXOR(arr, N))  # Output: 7

# Example 2
arr = [9, 8, 5]
N = 3
print(solution.maxSubsetXOR(arr, N))  # Output: 13

'''
Here’s a plain-text line-by-line explanation of the code:

class Solution:
Defines a class Solution.

def maxSubsetXOR(self, arr, N):
Declares the method maxSubsetXOR to find the maximum XOR of any subset of the array.
arr: The input array.
N: The size of the array.

index = 0
Initializes a pointer index to track the current position in the "basis" of the XOR space.

for bit in range(31, -1, -1):
Iterates through bits from the most significant bit (MSB) to the least significant bit (LSB). Assumes 32-bit integers.

max_idx = index
Tracks the index of the maximum element with the current bit set.

max_ele = -1
Tracks the maximum element itself (initialized to an invalid value).

for i in range(index, N):
Iterates through all remaining elements of the array to find the one with the current bit set and the highest value.

if (arr[i] & (1 << bit)) != 0 and arr[i] > max_ele:
Checks if the current bit is set in arr[i] and if arr[i] is greater than the current max_ele.

max_ele = arr[i]
Updates max_ele to the value of arr[i].

max_idx = i
Updates max_idx to the index of arr[i].

if max_ele == -1:
If no element has the current bit set, skip to the next bit.

continue
Skips the rest of the loop for this bit.

arr[index], arr[max_idx] = arr[max_idx], arr[index]
Swaps the maximum element found to the index position.

for i in range(N):
Iterates through all elements of the array.

if i != index and (arr[i] & (1 << bit)) != 0:
Checks if the current element (excluding the one at index) has the current bit set.

arr[i] ^= arr[index]
Performs XOR with the "basis" element at index, removing the current bit from arr[i].

index += 1
Moves to the next basis position.

max_xor = 0
Initializes the result to 0.

for i in range(index):
Iterates through all elements in the basis.

max_xor ^= arr[i]
Computes the XOR of all basis elements.

return max_xor
Returns the maximum XOR value.

solution = Solution()
Creates an instance of the Solution class.

arr = [2, 4, 5]
Defines the input array.

N = 3
Specifies the number of elements.

print(solution.maxSubsetXOR(arr, N))
Calls the method and prints the output, which is 7 (subset: {2, 5}).

arr = [9, 8, 5]
Defines a new input array.

N = 3
Specifies the number of elements.

print(solution.maxSubsetXOR(arr, N))
Calls the method and prints the output, which is 13 (subset: {9, 8}).
'''