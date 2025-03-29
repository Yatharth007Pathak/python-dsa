"""
The hiring team aims to find 3 candidates who are great collectively. Each candidate has his or her ability expressed as an integer. 
3 candidates are great collectively if the product of their abilities is maximum. 
Given the abilities of some candidates in an array, arr[], return the maximum collective ability from the pool of candidates.

Examples:

Input: arr[] = [10, 3, 5, 6, 20]
Output: 1200
Explanation: Multiplication of 10, 6, and 20 is 1200.

Input: arr[] = [-10, -3, -5, -6, -20]
Output: -90
Explanation: Multiplication of -3, -5 and -6 is -90.
"""

class Solution:
    def maxProduct(self, arr):
        # Sort the array
        arr.sort()

        # Calculate the product of the three largest numbers
        max_product1 = arr[-1] * arr[-2] * arr[-3]

        # Calculate the product of the two smallest numbers and the largest number
        max_product2 = arr[0] * arr[1] * arr[-1]

        # Return the maximum of the two products
        return max(max_product1, max_product2)

# Example usage
solution = Solution()
print(solution.maxProduct([10, 3, 5, 6, 20]))  # Output: 1200
print(solution.maxProduct([-10, -3, -5, -6, -20]))  # Output: -90

'''
Here's a breakdown of the code line by line:

class Solution:
This line defines a new class named Solution. In Python, classes are templates for creating objects and can contain methods and attributes.

def maxProduct(self, arr):
This line defines a method named maxProduct within the Solution class. The method takes two parameters: 
self (a reference to the current instance of the class) and arr (a list of numbers).

arr.sort()
This line sorts the input list arr in ascending order. Sorting allows easy access to the largest and smallest numbers in the list.

max_product1 = arr[-1] * arr[-2] * arr[-3]
This line calculates the product of the three largest numbers in the sorted array. 
arr[-1], arr[-2], and arr[-3] access the last three elements of the sorted list, which are the largest.

max_product2 = arr[0] * arr[1] * arr[-1]
This line calculates the product of the two smallest numbers (arr[0] and arr[1]) and the largest number (arr[-1]). 
This is important for cases where there are negative numbers, as two negatives multiplied together give a positive product.

return max(max_product1, max_product2)
This line returns the maximum value between max_product1 and max_product2. 
The max() function compares the two products and returns the larger one.

# Example usage
This is a comment indicating that the following lines show how to use the Solution class and its maxProduct method.

solution = Solution()
This line creates an instance of the Solution class and assigns it to the variable solution.

print(solution.maxProduct([10, 3, 5, 6, 20]))
This line calls the maxProduct method on the solution instance, passing in a list of numbers [10, 3, 5, 6, 20]. 
The result (maximum product) is printed to the console.

print(solution.maxProduct([-10, -3, -5, -6, -20]))
This line calls the maxProduct method again, this time with a list of negative numbers [-10, -3, -5, -6, -20]. 
The result is printed to the console, demonstrating the method's ability to handle negative inputs.
'''