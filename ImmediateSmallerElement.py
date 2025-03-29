"""
Given an integer array arr. For each element in the array, check whether the right adjacent element (on the next immediate position) 
of the array is smaller. If next element is smaller, update the current index to that element. If not, then update to -1. 
Return the modified array.

Examples:

Input: arr[] = [4, 2, 1, 5, 3]
Output: [2, 1, -1, 3, -1]
Explanation: Array elements are 4, 2, 1, 5, 3. Next to 4 is 2 which is smaller, so we print 2. 
Next of 2 is 1 which is smaller,so we print 1. Next of 1 is 5 which is greater, so we print -1. 
Next of 5 is 3 which is smaller, so we print 3. 
Note that for last element, output is always going to be -1 because there is no element on right.

Input: arr[] = [5, 6, 2, 3, 1, 7]
Output: [-1, 2, -1, 1, -1, -1]
Explanation: Next to 5 is 6 which is greater, so we print -1. Next of 6 is 2 which is smaller, so we print 2. 
Next of 2 is 3 which is greater, so we print -1. Next of 3 is 1 which is smaller, so we print 1. 
Next of 1 is 7 which is greater, so we print -1. 
Note that for last element, output is always going to be -1 because there is no element on right.

Input: arr[] = [4, 1]
Output: [1, -1]
Explanation: 4 will be updated to 1 and 1 will be updated to -1.
"""

class Solution:
    def immediateSmaller(self, arr):
        n = len(arr)
        # Iterate through the array
        for i in range(n - 1):  # Last element will always be -1
            # Check if the next element is smaller
            if arr[i + 1] < arr[i]:
                arr[i] = arr[i + 1]
            else:
                arr[i] = -1
        # Last element has no next, so update to -1
        arr[-1] = -1
        return arr

# Example usage
solution = Solution()
arr1 = [4, 2, 1, 5, 3]
arr2 = [5, 6, 2, 3, 1, 7]
arr3 = [4, 1]

print(solution.immediateSmaller(arr1))  # Output: [2, 1, -1, 3, -1]
print(solution.immediateSmaller(arr2))  # Output: [-1, 2, -1, 1, -1, -1]
print(solution.immediateSmaller(arr3))  # Output: [1, -1]

'''

Here's a plain-text explanation of the code:

class Solution:
Defines a class named Solution containing the method immediateSmaller.

def immediateSmaller(self, arr):
A method to replace each element of the array with the next smaller element.
If no such element exists, replace it with -1.

n = len(arr)
Stores the length of the input array arr.

for i in range(n - 1):
Iterates through the array up to the second last element (n-1). The last element will always be updated to -1 since it has no next element.

if arr[i + 1] < arr[i]:
Compares the current element (arr[i]) with the next element (arr[i+1]).

arr[i] = arr[i + 1]
If the next element is smaller, replace the current element with the next element.

else:
If the next element is not smaller:

arr[i] = -1
Set the current element to -1.

arr[-1] = -1
The last element of the array has no next element, so it is always set to -1.

return arr
Returns the modified array after processing all elements.

solution = Solution()
Creates an instance of the Solution class.

arr1 = [4, 2, 1, 5, 3]
Initializes an array to test the method.

print(solution.immediateSmaller(arr1))
Calls immediateSmaller with arr1 and prints the result.

Example Outputs
Input: [4, 2, 1, 5, 3]
Step-by-step:
Compare 4 and 2: Replace 4 with 2.
Compare 2 and 1: Replace 2 with 1.
Compare 1 and 5: Replace 1 with -1.
Compare 5 and 3: Replace 5 with 3.
Set last element 3 to -1.
Output: [2, 1, -1, 3, -1].

Input: [5, 6, 2, 3, 1, 7]
Step-by-step:
Compare 5 and 6: Replace 5 with -1.
Compare 6 and 2: Replace 6 with 2.
Compare 2 and 3: Replace 2 with -1.
Compare 3 and 1: Replace 3 with 1.
Compare 1 and 7: Replace 1 with -1.
Set last element 7 to -1.
Output: [-1, 2, -1, 1, -1, -1].

Input: [4, 1]
Step-by-step:
Compare 4 and 1: Replace 4 with 1.
Set last element 1 to -1.
Output: [1, -1].
'''