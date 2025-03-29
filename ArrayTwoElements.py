"""
Given an unsorted array arr of of positive integers.
One number 'A' from set {1, 2,....,n} is missing and one number 'B' occurs twice in array. Find numbers A and B.

Examples

Input: arr[] = [2, 2]
Output: 2 1
Explanation: Repeating number is 2 and smallest positive missing number is 1.

Input: arr[] = [1, 3, 3] 
Output: 3 2
Explanation: Repeating number is 3 and smallest positive missing number is 2.
"""

class Solution:
    def findTwoElement(self, arr):
        n = len(arr)
        
        # Expected sum and sum of squares for numbers 1 to n
        expected_sum = n * (n + 1) // 2
        expected_sum_sq = n * (n + 1) * (2 * n + 1) // 6
        
        # Actual sum and sum of squares for the given array
        actual_sum = sum(arr)
        actual_sum_sq = sum(x * x for x in arr)
        
        # Let A be the missing number and B be the repeating number
        # We have the following two equations:
        # 1. A - B = expected_sum - actual_sum
        # 2. A^2 - B^2 = expected_sum_sq - actual_sum_sq
        #    => (A - B)(A + B) = expected_sum_sq - actual_sum_sq
        # Using equation 1, we can solve for A and B.
        
        diff_sum = expected_sum - actual_sum        # A - B
        diff_sum_sq = expected_sum_sq - actual_sum_sq  # A^2 - B^2
        
        # (A - B)(A + B) = A^2 - B^2
        sum_ab = diff_sum_sq // diff_sum  # A + B
        
        # Now we can find A and B
        A = (diff_sum + sum_ab) // 2
        B = sum_ab - A
        
        return B, A  # Repeating number, Missing number

# Example usage:
sol = Solution()
arr1 = [2, 2]
print(sol.findTwoElement(arr1))  # Output: (2, 1)

arr2 = [1, 3, 3]
print(sol.findTwoElement(arr2))  # Output: (3, 2)

'''
Here is a line-by-line breakdown of the code:

class Solution:
Defines a class Solution which will contain the method to solve the problem of finding the missing and repeating elements in an array.

def findTwoElement(self, arr):
This defines the method findTwoElement which takes an array arr as input and returns two elements: one that is missing and one that repeats.

n = len(arr):
This calculates the size of the array n, which represents the total number of elements. 
The array is supposed to contain elements from 1 to n, but one element repeats, and one is missing.

expected_sum = n * (n + 1) // 2:
This computes the sum of integers from 1 to n.
This represents the expected sum if all elements from 1 to n were present without any repetitions or missing elements.

expected_sum_sq = n * (n + 1) * (2 * n + 1) // 6:
This computes the sum of squares of integers from 1 to n.

actual_sum = sum(arr):
This calculates the actual sum of the elements in the array arr using Python's sum() function.

actual_sum_sq = sum(x * x for x in arr):
This calculates the actual sum of squares of the elements in arr. For each element x in the array, its square is computed and added to the sum.

diff_sum = expected_sum - actual_sum:
The difference between the expected sum and the actual sum is stored in diff_sum. This is:
diff_sum = A - B, where A is the missing element and B is the repeating element.

diff_sum_sq = expected_sum_sq - actual_sum_sq:
Similarly, this computes the difference between the expected sum of squares and the actual sum of squares, stored in diff_sum_sq. This is:

diff_sum_sq = A^2 - B^2
 
sum_ab = diff_sum_sq // diff_sum:
Using the equation A^2 - B^2 = (A + B)(A - B), we can derive that: sum_ab=A+B. This calculates A+B by dividing diff_sum_sq by diff_sum.

A = (diff_sum + sum_ab) // 2:
This calculates the value of A (the missing element) using the equations 
A - B = diff_sum and A + B = sum_ab. The formula is:
A = ((A - B) + (A + B)) / 2
 
B = sum_ab - A:
Once A is known, the value of B (the repeating element) can be computed as:
B = A + B - A

return B, A:
The method returns the repeating element B and the missing element A.

Example usage:
arr1 = [2, 2]:
The input array arr1 has the repeating element 2 and the missing element 1. When sol.findTwoElement(arr1) is called, it returns (2, 1).

arr2 = [1, 3, 3]:
The input array arr2 has the repeating element 3 and the missing element 2. When sol.findTwoElement(arr2) is called, it returns (3, 2).

The approach works by using sum and sum of squares to derive two key equations that help find the missing and repeating elements.
'''