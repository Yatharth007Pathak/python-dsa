"""
You have given two sorted arrays arr1[] & arr2[] of distinct elements. The first array has one element extra added in between. 
Return the index of the extra element.
Note: 0-based indexing is followed.

Example:
Input: n = 7, arr1 = [2,4,6,8,9,10,12], arr2 = [2,4,6,8,10,12]
Output: 4
Explanation: In the first array, 9 is extra added and it's index is 4.
"""

class Solution:
    def findExtra(self, n, arr1, arr2):
        # Initialize pointers for both arrays
        i = 0
        j = 0
        
        # Traverse both arrays
        while i < n - 1 and j < n - 1:
            if arr1[i] == arr2[j]:
                i += 1
                j += 1
            else:
                # The extra element is found
                return i
        
        # If we reached here, it means extra element is at the end of arr1
        return i

# Example usage:
solution = Solution()
n = 7
arr1 = [2, 4, 6, 8, 9, 10, 12]
arr2 = [2, 4, 6, 8, 10, 12]
print(solution.findExtra(n, arr1, arr2))  # Output: 4

'''
Let's break down the findExtra method from the given Python class:

class Solution:
This line defines a class named Solution that contains methods related to solving problems.

def findExtra(self, n, arr1, arr2):
This line defines a method findExtra within the Solution class. The method takes three parameters: 
n (the length of the first array arr1), arr1 (the first array with an extra element), and arr2 (the second array without the extra element).

i = 0
This line initializes a pointer i for iterating through arr1, starting from index 0.

j = 0
This line initializes a pointer j for iterating through arr2, also starting from index 0.

while i < n - 1 and j < n - 1:
This line starts a while loop that continues as long as i and j are within valid bounds of their respective arrays. 
The loop condition ensures that both pointers do not exceed the length of their arrays, which is n - 1 for arr2 and n for arr1.

if arr1[i] == arr2[j]:
This line checks if the current elements pointed to by i in arr1 and j in arr2 are equal.

i += 1
If the elements are equal, this line moves the pointer i to the next element in arr1.

j += 1
Similarly, this line moves the pointer j to the next element in arr2.

else:
This block executes if the elements at arr1[i] and arr2[j] are not equal.

return i
Since an unequal element indicates that the extra element in arr1 is found at index i, this line returns i.

return i
If the while loop completes without finding an extra element (i.e., all elements of arr2 have been matched), this line returns i. 
This implies that the extra element is at the end of arr1, and i marks its index.

Example Usage Explanation:
For arr1 = [2, 4, 6, 8, 9, 10, 12] and arr2 = [2, 4, 6, 8, 10, 12] with n = 7:
Both arrays are traversed until an element in arr1 does not match the corresponding element in arr2.
The first mismatch occurs at index 4, where arr1[4] (which is 9) does not match arr2[4].
Therefore, the method returns 4, indicating that the extra element (9) is at index 4 in arr1.
'''