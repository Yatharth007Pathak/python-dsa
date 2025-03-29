"""
Given an array arr[] of N integers, calculate the median.
Note: Return the floor value of the median. 

Example:
Input: N = 5, arr[] = 90 100 78 89 67
Output: 89
Explanation: After sorting the array middle element is the median 
"""

class Solution:
    def find_median(self, v):
        # Sort the array
        v.sort()
        
        # Find the length of the array
        n = len(v)
        
        # If the array has an odd number of elements, return the middle one
        if n % 2 == 1:
            return v[n // 2]
        else:
            # If the array has an even number of elements, return the floor value of the average of the two middle elements
            return (v[(n // 2) - 1] + v[n // 2]) // 2

# Example usage:
arr = [90, 100, 78, 89, 67]
sol = Solution()
print(sol.find_median(arr))  # Output: 89

'''
This code defines a Python class called Solution with a method find_median that calculates the median of an array. 
Here is a line-by-line breakdown of the code:

class Solution:
This defines a class named Solution. Classes in Python are used to encapsulate data and methods (functions) that operate on that data.

def find_median(self, v):
This defines a method find_median inside the class Solution. It takes two arguments: 
self (which refers to the instance of the class) and v (the array of numbers whose median is to be found).

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
This calls the find_median method on the instance sol with arr as the argument and prints the result, 
which is the median of the array arr. The output is 89.
'''