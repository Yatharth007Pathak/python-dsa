"""
Given an array arr[] of size N containing equal number of odd and even numbers. 
Arrange the numbers in such a way that all the even numbers get the even index and odd numbers get the odd index.
Note: There are multiple possible solutions, Print any one of them. Also, 0-based indexing is considered.

Example:
Input: N = 6, arr[] = {3, 6, 12, 1, 5, 8}
Output: 1
Explanation: 6 3 12 1 8 5 is a possible solution. The output will always be 1 if your rearrangement is correct.

Example 2:
Input: N = 4, arr[] = {1, 2, 3, 4}
Output : 1
"""

class Solution:
    def reArrange(self, arr, N):
        even_index = 0  # Start from the first even index
        odd_index = 1   # Start from the first odd index
        
        while even_index < N and odd_index < N:
            # If the number at even_index is even, it's in the correct place
            if arr[even_index] % 2 == 0:
                even_index += 2
            # If the number at odd_index is odd, it's in the correct place
            elif arr[odd_index] % 2 == 1:
                odd_index += 2
            else:
                # Swap the elements at even_index and odd_index
                arr[even_index], arr[odd_index] = arr[odd_index], arr[even_index]
                even_index += 2
                odd_index += 2

# Example usage:
solution = Solution()
arr = [3, 6, 12, 1, 5, 8]
solution.reArrange(arr, len(arr))
print(arr)  # Output: [6, 3, 12, 1, 8, 5]

'''
Here's a breakdown of the code line by line, explained in a pointwise manner:

class Solution:
This defines a class named Solution. The class will contain methods to solve specific problems, in this case, 
rearranging elements in an array so that even-indexed positions contain even numbers and odd-indexed positions contain odd numbers.

def reArrange(self, arr, N):
This defines a method named reArrange inside the Solution class.
It takes three parameters: self (the instance of the class), arr (a list of integers), 
and N (an integer representing the number of elements in the list).

even_index = 0 # Start from the first even index
This initializes a variable even_index to 0.
This variable keeps track of the current even index position in the array where an even number should be placed.

odd_index = 1 # Start from the first odd index
This initializes a variable odd_index to 1.
This variable keeps track of the current odd index position in the array where an odd number should be placed.

while even_index < N and odd_index < N:
This starts a while loop that continues as long as both even_index and odd_index are within the bounds of the array arr. 
The loop ensures that the rearrangement continues until all positions are correctly filled.

if arr[even_index] % 2 == 0:
This checks if the element at even_index is even. If true, it means the element is already in the correct place.

even_index += 2
If the element at even_index is even, the even_index is incremented by 2 to move to the next even position in the array.

elif arr[odd_index] % 2 == 1:
This checks if the element at odd_index is odd. If true, it means the element is already in the correct place.

odd_index += 2
If the element at odd_index is odd, the odd_index is incremented by 2 to move to the next odd position in the array.

else:
If neither of the above conditions is true (i.e., arr[even_index] is odd and arr[odd_index] is even), 
it means the elements at even_index and odd_index are incorrectly placed and need to be swapped.

arr[even_index], arr[odd_index] = arr[odd_index], arr[even_index]
This swaps the elements at even_index and odd_index to correct their positions.

even_index += 2
After the swap, the even_index is incremented by 2 to move to the next even position.

odd_index += 2
After the swap, the odd_index is incremented by 2 to move to the next odd position.

# Example usage:
This comment indicates the beginning of an example that shows how to use the reArrange method.

solution = Solution()
This creates an instance of the Solution class.

arr = [3, 6, 12, 1, 5, 8]
This initializes an array arr with the elements [3, 6, 12, 1, 5, 8].

solution.reArrange(arr, len(arr))
This calls the reArrange method on the solution instance, passing the array arr and its length len(arr) as arguments.

print(arr) # Output: [6, 3, 12, 1, 8, 5]
This prints the modified array arr after the rearrangement.
The expected output is [6, 3, 12, 1, 8, 5], where even indices have even numbers and odd indices have odd numbers.
'''