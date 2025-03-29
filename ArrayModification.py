"""
Given an array arr. Return the modified array in such a way that if the current and next numbers are valid numbers 
and are equal then double the current number value and replace the next number with 0. 
After the modification, rearrange the array such that all 0's are shifted to the end.

Note:
Assume '0' as the invalid number and all others as a valid number.
Modify on the given array arr itself.
The sequence of the valid numbers is present in the same order.

Example:

Input: arr[] = [2, 2, 0, 4, 0, 8] 
Output: [4, 4, 8, 0, 0, 0] 
Explanation: At index 0 and 1 both the elements are the same. So, we will change the element at index 0 to 4 
and the element at index 1 is 0 then we will shift all the zeros to the end of the array. So, the array will become [4, 4, 8, 0, 0, 0].

Input: arr[] = [0, 2, 2, 2, 0, 6, 6, 0, 0, 8] 
Output: [4, 2, 12, 8, 0, 0, 0, 0, 0, 0]
Explanation: At index 5 and 6 both the elements are the same. So, we will change the element at index 5 to 12 and the element at index 6 is 0. 
We will change the element at index 1 to 4 and the element at index 2 is 0. Then we shift all the zeros to the end of the array. 
So, array will become [4, 2, 12, 8, 0, 0, 0, 0, 0, 0].
"""

class Solution:
    def modifyAndRearrangeArr(self, arr):
        n = len(arr)
        
        # Step 1: Modify the array according to the given rules
        i = 0
        while i < n - 1:
            if arr[i] != 0 and arr[i] == arr[i + 1]:
                arr[i] *= 2
                arr[i + 1] = 0
                i += 1  # Skip the next element since it's set to 0
            i += 1
        
        # Step 2: Rearrange the array by moving all zeros to the end
        result = [num for num in arr if num != 0]  # Extract all non-zero elements
        result.extend([0] * (n - len(result)))  # Append the necessary number of zeros
        
        return result

solution = Solution()

arr = [2, 2, 0, 4, 0, 8]
print(solution.modifyAndRearrangeArr(arr))  # Output: [4, 4, 8, 0, 0, 0]

arr = [0, 2, 2, 2, 0, 6, 6, 0, 0, 8]
print(solution.modifyAndRearrangeArr(arr))  # Output: [4, 2, 12, 8, 0, 0, 0, 0, 0, 0]

'''
Explanation of the Code:

class Solution:
Defines the Solution class, which contains the method modifyAndRearrangeArr.

def modifyAndRearrangeArr(self, arr):
Defines the method modifyAndRearrangeArr, which takes an array arr and returns a modified version of the array according to specific rules.

n = len(arr)
Calculates the length of the array arr and stores it in the variable n.

i = 0
Initializes the variable i to 0, which will be used to iterate through the array.

while i < n - 1:
Starts a while loop that iterates through the array, checking each pair of consecutive elements. The loop runs until i reaches n - 1.
if arr[i] != 0 and arr[i] == arr[i + 1]:
Checks if the current element (arr[i]) is not 0 and is equal to the next element (arr[i + 1]).

arr[i] *= 2
If the condition is met (i.e., two consecutive non-zero elements are equal), it doubles the current element (arr[i]).

arr[i + 1] = 0
Sets the next element (arr[i + 1]) to 0, since it has been merged with the current element.

i += 1
Increments i by 1 to skip over the next element, which was set to 0 in the previous step.

i += 1
Increments i by 1 to continue checking the next pair of elements in the array.

result = [num for num in arr if num != 0]
Creates a list result containing all non-zero elements from arr. This step removes all zeros from the array.

result.extend([0] * (n - len(result)))
Appends the required number of zeros to the end of the result array to make its length equal to the original array (n).

return result
Returns the modified array result.
'''