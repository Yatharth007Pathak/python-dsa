"""
Given two sorted arrays arr1 and arr2 and an element k. 
The task is to find the element that would be at the kth position of the combined sorted array.

Examples :

Input: k = 5, arr1[] = [2, 3, 6, 7, 9], arr2[] = [1, 4, 8, 10]
Output: 6
Explanation: The final combined sorted array would be - 1, 2, 3, 4, 6, 7, 8, 9, 10. The 5th element of this array is 6.

Input: k = 7, arr1[] = [100, 112, 256, 349, 770], arr2[] = [72, 86, 113, 119, 265, 445, 892]
Output: 256
Explanation: Combined sorted array is - 72, 86, 100, 112, 113, 119, 256, 265, 349, 445, 770, 892. 7th element of this array is 256.
"""

class Solution:
    # Function to find the kth element in the merged sorted array
    def kthElement(self, k, arr1, arr2):
        i, j, count = 0, 0, 0
        n, m = len(arr1), len(arr2)
        
        # Traverse both arrays
        while i < n and j < m:
            # If element in arr1 is smaller, consider it in the merged array
            if arr1[i] <= arr2[j]:
                count += 1
                # When count equals k, return the current element
                if count == k:
                    return arr1[i]
                i += 1
            # If element in arr2 is smaller, consider it in the merged array
            else:
                count += 1
                # When count equals k, return the current element
                if count == k:
                    return arr2[j]
                j += 1
        
        # If one of the arrays is exhausted, continue with the other array
        while i < n:
            count += 1
            if count == k:
                return arr1[i]
            i += 1
        
        while j < m:
            count += 1
            if count == k:
                return arr2[j]
            j += 1
        
        return -1  # In case k is invalid

solution = Solution()

# Example 1
arr1 = [2, 3, 6, 7, 9]
arr2 = [1, 4, 8, 10]
k = 5
print(solution.kthElement(k, arr1, arr2))  # Output: 6

# Example 2
arr1 = [100, 112, 256, 349, 770]
arr2 = [72, 86, 113, 119, 265, 445, 892]
k = 7
print(solution.kthElement(k, arr1, arr2))  # Output: 256

'''

Here's a line-by-line breakdown of the code:

class Solution:
The Solution class is defined to contain the function kthElement that finds the k-th element in the merged sorted array.

def kthElement(self, k, arr1, arr2):
The method kthElement is defined with three parameters:

k: The position of the element to find in the merged sorted array.
arr1: The first sorted array.
arr2: The second sorted array.
i, j, count = 0, 0, 0:
Three variables are initialized:

i: Pointer for traversing arr1.
j: Pointer for traversing arr2.
count: A counter to keep track of the number of elements considered from both arrays.
n, m = len(arr1), len(arr2):
Variables n and m are initialized to store the lengths of arrays arr1 and arr2, respectively.

while i < n and j < m:
A loop starts to traverse both arrays arr1 and arr2 simultaneously. The loop continues until one of the arrays is fully traversed.

if arr1[i] <= arr2[j]:
This checks if the current element of arr1 is smaller than or equal to the current element of arr2.

count += 1:
The counter count is incremented, as another element is considered for the merged sorted array.

if count == k:
If the count equals k, this means the current element is the k-th element in the merged array.

return arr1[i]:
The current element from arr1 is returned as the k-th element.

i += 1:
The pointer i is incremented to move to the next element in arr1.

else:
This else block is executed when the current element of arr2 is smaller than the current element of arr1.

count += 1:
The counter count is incremented.

if count == k:
If the count equals k, the current element is the k-th element in the merged array.

return arr2[j]:
The current element from arr2 is returned as the k-th element.

j += 1:
The pointer j is incremented to move to the next element in arr2.

while i < n:
This loop runs if arr1 still has elements left after arr2 is fully traversed.

count += 1:
The counter count is incremented for each element from arr1.

if count == k:
If the count equals k, the current element is the k-th element in the merged array.

return arr1[i]:
The current element from arr1 is returned as the k-th element.

i += 1:
The pointer i is incremented.

while j < m:
This loop runs if arr2 still has elements left after arr1 is fully traversed.

count += 1:
The counter count is incremented for each element from arr2.

if count == k:
If the count equals k, the current element is the k-th element in the merged array.

return arr2[j]:
The current element from arr2 is returned as the k-th element.

j += 1:
The pointer j is incremented.

return -1:
If k is invalid (i.e., greater than the total number of elements in both arrays), the function returns -1.
Example Usage:

arr1 = [2, 3, 6, 7, 9]:
The first sorted array arr1 is initialized.

arr2 = [1, 4, 8, 10]:
The second sorted array arr2 is initialized.

k = 5:
The position k is defined as 5.

print(solution.kthElement(k, arr1, arr2)):
The kthElement method is called with k, arr1, and arr2. The output is 6, which is the 5th element in the merged sorted array.

arr1 = [100, 112, 256, 349, 770]:
Another test case with the first sorted array arr1.

arr2 = [72, 86, 113, 119, 265, 445, 892]:
The second sorted array arr2 is initialized.

k = 7:
The position k is defined as 7.

print(solution.kthElement(k, arr1, arr2)):
The kthElement method is called with k, arr1, and arr2. The output is 256, which is the 7th element in the merged sorted array.
'''