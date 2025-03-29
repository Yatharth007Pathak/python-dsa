"""
Given two sorted arrays a[] and b[] in non-decreasing order. Merge them in sorted order without using any extra space. 
Modify a so that it contains the first n elements and modify b so that it contains the last m elements.

Examples:

Input: a[] = [2, 4, 7, 10], b[] = [2, 3]
Output:
2 2 3 4
7 10
Explanation: After merging the two non-decreasing arrays, we get, 2 2 3 4 7 10

Input: a[] = [1, 5, 9, 10, 15, 20], b[] = [2, 3, 8, 13]
Output:
1 2 3 5 8 9
10 13 15 20
Explanation: After merging two sorted arrays we get 5 10 12 18 20.

Input: a[] = [0, 1], b[] = [2, 3]
Output:
0 1
2 3
Explanation: After merging two sorted arrays we get 0 1 2 3.
"""

class Solution:
    def mergeArrays(self, a, b):
        n, m = len(a), len(b)
        i, j = n - 1, 0  # Pointers for a (from end) and b (from start)
        
        # Step 1: Swap elements to maintain the order
        while i >= 0 and j < m:
            if a[i] > b[j]:
                a[i], b[j] = b[j], a[i]
            i -= 1
            j += 1

        # Step 2: Sort both arrays after swaps
        a.sort()
        b.sort()
        
        return a, b

# Example 1
a = [2, 4, 7, 10]
b = [2, 3]
solution = Solution()
a, b = solution.mergeArrays(a, b)
print("Array a:", a)  # Output: [2, 2, 3, 4]
print("Array b:", b)  # Output: [7, 10]

# Example 2
a = [1, 5, 9, 10, 15, 20]
b = [2, 3, 8, 13]
a, b = solution.mergeArrays(a, b)
print("Array a:", a)  # Output: [1, 2, 3, 5, 8, 9]
print("Array b:", b)  # Output: [10, 13, 15, 20]

'''
Here's an explanation of the code:

class Solution:
Defines a class named Solution with a method to merge two sorted arrays without using extra space.

def mergeArrays(self, a, b):
Defines the mergeArrays method, which takes self (instance of the class), a (the first array), and b (the second array) as parameters.

n, m = len(a), len(b)
Assigns n and m as the lengths of arrays a and b, respectively.

i, j = n - 1, 0
Initializes pointers i at the end of array a and j at the beginning of array b.

while i >= 0 and j < m:
Starts a loop to go through both arrays, swapping elements as needed until i goes out of bounds of a or j reaches the end of b.

if a[i] > b[j]:
Checks if the current element in a is greater than the current element in b.

a[i], b[j] = b[j], a[i]
If a[i] is greater than b[j], swaps a[i] with b[j] to ensure that smaller elements are in a and larger elements are in b.

i -= 1 and j += 1
Moves i one step left and j one step right to continue the comparisons and swaps.

a.sort() and b.sort()
Sorts both arrays a and b after completing the swapping process to ensure each array is sorted in ascending order.

return a, b
Returns the modified arrays a and b.

Example Usage:

Example 1:
a = [2, 4, 7, 10]
b = [2, 3]
Input: a contains [2, 4, 7, 10], b contains [2, 3].
Output: a is [2, 2, 3, 4], b is [7, 10].

Example 2:
a = [1, 5, 9, 10, 15, 20]
b = [2, 3, 8, 13]
Input: a contains [1, 5, 9, 10, 15, 20], b contains [2, 3, 8, 13].
Output: a is [1, 2, 3, 5, 8, 9], b is [10, 13, 15, 20].

Complexity Analysis
Time Complexity: O((n+m)log(n+m)) due to the sorting operations after swapping.
Space Complexity: O(1) since we're modifying the arrays a and b in-place without extra space.
'''