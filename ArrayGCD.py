"""
Given an array of N positive integers, find GCD of all the array elements.

Example 1:
Input: N = 3, arr[] = {2, 4, 6}
Output: 2
Explanation: GCD of 2,4,6 is 2.

Example 2:
Input: N = 1, arr[] = {1}
Output: 1
Explanation: Greatest common divisor of all the numbers is 1.
"""

class Solution:
    def gcd(self, n, arr):
        # Helper function to compute GCD of two numbers
        def compute_gcd(a, b):
            while b != 0:
                a, b = b, a % b
            return a
        
        # Initialize result with the first element
        result = arr[0]
        
        # Compute GCD of the entire array
        for i in range(1, n):
            result = compute_gcd(result, arr[i])
            # If at any point GCD becomes 1, we can break early
            if result == 1:
                break
        
        return result

# Example 1
solution = Solution()
arr = [2, 4, 6]
print(solution.gcd(3, arr))  # Output: 2

# Example 2
arr = [1]
print(solution.gcd(1, arr))  # Output: 1

# Example 3
arr = [12, 15, 21]
print(solution.gcd(3, arr))  # Output: 3

'''
Here's a plain-text breakdown of the code:

class Solution:
Defines a class Solution to implement the solution for finding the GCD of an array.

def gcd(self, n, arr):
Defines a method gcd to compute the greatest common divisor (GCD) of an array of size n.

def compute_gcd(a, b):
Defines a nested helper function to compute the GCD of two numbers a and b using the Euclidean algorithm.

while b != 0:
Runs a loop until the remainder (b) becomes 0.

a, b = b, a % b
Updates a with b and b with a % b (remainder of the division).

return a
Returns the GCD, which is the last non-zero value of a.

result = arr[0]
Initializes result with the first element of the array.

for i in range(1, n):
Iterates over the rest of the array starting from the second element.

result = compute_gcd(result, arr[i])
Updates result by computing the GCD of the current result and the next element in the array.

if result == 1:
Checks if the GCD becomes 1 (the smallest possible GCD for integers).

break
Breaks the loop early because the GCD of the entire array cannot go below 1.

return result
Returns the GCD of the array.

solution = Solution()
Creates an instance of the Solution class.

arr = [2, 4, 6]
Defines an array of integers.

print(solution.gcd(3, arr))
Computes the GCD of the array [2, 4, 6] with n = 3.

Output: 2
Explanation: GCD of 2, 4, and 6 is 2.

arr = [1]
Defines an array with a single element.

print(solution.gcd(1, arr))
Computes the GCD of the array [1] with n = 1.

Output: 1
Explanation: The GCD of a single element is the element itself.

arr = [12, 15, 21]
Defines another array of integers.

print(solution.gcd(3, arr))
Computes the GCD of the array [12, 15, 21] with n = 3.

Output: 3
Explanation: GCD of 12, 15, and 21 is 3.
'''