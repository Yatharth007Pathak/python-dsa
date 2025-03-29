"""
Given two sorted arrays a[] and b[], where each array may contain duplicate elements, 
the task is to return the elements in the union of the two arrays in sorted order.

Union of two arrays can be defined as the set containing distinct common elements that are present in either of the arrays.
Examples:

Input: a[] = [1, 2, 3, 4, 5], b[] = [1, 2, 3, 6, 7]
Output: 1 2 3 4 5 6 7
Explanation: Distinct elements including both the arrays are: 1 2 3 4 5 6 7.

Input: a[] = [2, 2, 3, 4, 5], b[] = [1, 1, 2, 3, 4]
Output: 1 2 3 4 5
Explanation: Distinct elements including both the arrays are: 1 2 3 4 5.

Input: a[] = [1, 1, 1, 1, 1], b[] = [2, 2, 2, 2, 2]
Output: 1 2
Explanation: Distinct elements including both the arrays are: 1 2.
"""

class Solution:

    # Function to return a list containing the union of the two arrays.
    def findUnion(self, a, b):
        result = []
        i, j = 0, 0
        n, m = len(a), len(b)

        while i < n and j < m:
            if a[i] < b[j]:
                # Add the element from a[] if not already in result
                if len(result) == 0 or result[-1] != a[i]:
                    result.append(a[i])
                i += 1
            elif a[i] > b[j]:
                # Add the element from b[] if not already in result
                if len(result) == 0 or result[-1] != b[j]:
                    result.append(b[j])
                j += 1
            else:
                # If both elements are same, add only one and move both pointers
                if len(result) == 0 or result[-1] != a[i]:
                    result.append(a[i])
                i += 1
                j += 1

        # If there are remaining elements in a[], add them
        while i < n:
            if len(result) == 0 or result[-1] != a[i]:
                result.append(a[i])
            i += 1

        # If there are remaining elements in b[], add them
        while j < m:
            if len(result) == 0 or result[-1] != b[j]:
                result.append(b[j])
            j += 1

        return result

a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 6, 7]
solution = Solution()
print(solution.findUnion(a, b))  # Output: [1, 2, 3, 4, 5, 6, 7]

'''
Here's a line-by-line breakdown of the code:

class Solution:
The Solution class is defined to hold the function findUnion that returns the union of two arrays.

def findUnion(self, a, b):
The function findUnion is defined with two parameters:

a: First sorted array.
b: Second sorted array.
result = []:
A list called result is initialized to store the union of the two arrays.

i, j = 0, 0:
Two pointers i and j are initialized to 0 to iterate over arrays a and b, respectively.

n, m = len(a), len(b):
Variables n and m are initialized to store the lengths of arrays a and b, respectively.

while i < n and j < m:
A loop starts that runs until either array a or b is fully traversed.

if a[i] < b[j]:
If the current element of a is smaller than the current element of b, the element from a should be added to result.

if len(result) == 0 or result[-1] != a[i]:
Before adding, it checks if the result list is empty or if the last element in result is not equal to a[i]. 
This ensures no duplicate elements are added.

result.append(a[i]):
The element a[i] is appended to result.

i += 1:
The pointer i is incremented to move to the next element in a.

elif a[i] > b[j]:
If the current element of a is greater than the current element of b, the element from b should be added to result.

if len(result) == 0 or result[-1] != b[j]:
Before adding, it checks if result is empty or if the last element in result is not equal to b[j]. This ensures no duplicates.

result.append(b[j]):
The element b[j] is appended to result.

j += 1:
The pointer j is incremented to move to the next element in b.

else:
This else block is reached when both a[i] and b[j] are equal.

if len(result) == 0 or result[-1] != a[i]:
Before adding, it checks if result is empty or if the last element in result is not equal to a[i]. 
This ensures only one copy of the duplicate element is added.

result.append(a[i]):
The element a[i] is appended to result.

i += 1:
The pointer i is incremented to move to the next element in a.

j += 1:
The pointer j is incremented to move to the next element in b.

while i < n:
After the main loop, this loop runs if there are remaining elements in a that have not been processed.

if len(result) == 0 or result[-1] != a[i]:
Before adding, it checks if the last element in result is not equal to a[i] to avoid duplicates.

result.append(a[i]):
The element a[i] is appended to result.

i += 1:
The pointer i is incremented.

while j < m:
This loop runs if there are remaining elements in b that have not been processed.

if len(result) == 0 or result[-1] != b[j]:
Before adding, it checks if the last element in result is not equal to b[j] to avoid duplicates.

result.append(b[j]):
The element b[j] is appended to result.

j += 1:
The pointer j is incremented.

return result:
The function returns the final union of arrays a and b, stored in result.
Example Usage:

a = [1, 2, 3, 4, 5]:
The first array a is initialized.

b = [1, 2, 3, 6, 7]:
The second array b is initialized.

solution = Solution():
An instance of the Solution class is created.

print(solution.findUnion(a, b)):
The findUnion method is called with arrays a and b, and the result is printed. The output is [1, 2, 3, 4, 5, 6, 7].
'''