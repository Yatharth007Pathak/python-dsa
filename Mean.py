"""
Given the marks of N students in an Array A, calculate the mean.
Note: If result is a Decimal Value, find it's floor Value.

Example:
Input: N = 4, A = [56 , 67 , 30 , 79]
Output: 58
Explanation: 56+67+30+79 = 232;  232/4 = 58. So, the Output is 58.
"""

class Solution:
    def mean(self, N, A):
        # Calculate the sum of the array
        total_sum = sum(A)
        
        # Calculate the mean and return the floor value
        return total_sum // N

# Example usage:
A = [56, 67, 30, 79]
N = len(A)
sol = Solution()
print(sol.mean(N, A))  # Output: 58

'''
This code defines a Python class called Solution with a method find_median that calculates the median of an array. 
Here is a line-by-line breakdown of the code:

class Solution:
This defines a class named Solution. Classes in Python are used to encapsulate data and methods (functions) that operate on that data.

def find_median(self, v):
This defines a method find_median inside the class Solution. 
It takes two arguments: self (which refers to the instance of the class) and v (the array of numbers whose median is to be found).

v.sort()
This line sorts the array v in ascending order. Sorting is necessary to compute the median as it is the middle value in a sorted array.

n = len(v)
This calculates the length of the array v and stores it in the variable n. 
This length is needed to determine whether the array has an odd or even number of elements.

if n % 2 == 1:
This checks if the array v has an odd number of elements. If n % 2 is equal to 1, it means n is odd.

return v[n // 2]
If the array has an odd number of elements, this line returns the middle element, which is found at index n // 2.

else:
If the array has an even number of elements, this else block will be executed.

return (v[(n // 2) - 1] + v[n // 2]) // 2
This line returns the median when the array has an even number of elements. 
It calculates the average of the two middle elements, v[(n // 2) - 1] and v[n // 2], and uses integer division (//) to return the floor value.

arr = [90, 100, 78, 89, 67]
This is an example array, arr, provided to demonstrate the usage of the find_median method.

sol = Solution()
This creates an instance of the Solution class named sol.

print(sol.find_median(arr))
This calls the find_median method on the instance sol with arr as the argument and prints the result, which is the median of the array arr. 
The output is 89.
'''