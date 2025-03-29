"""
You are given a number k and array arr. Your task is to rearrange the elements of array arr according to the absolute difference with k, 
i.e., an element having minimum difference comes first, and so on.
Note: If two or more elements are at equal distances arrange them in the same sequence as in the given array.

Examples:

Input: k = 7, arr[] = [10, 5, 3, 9, 2]
Output: [5, 9, 10, 3, 2]
Explanation: Sorting the numbers according to the absolute difference with 7, we have array elements as 5, 9, 10, 3, 2.

Input: k = 6, arr[] = [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]
Explanation: Sorting the numbers according to the absolute difference with 6, we have array elements as 5, 4, 3, 2, 1.
"""

class Solution:
    def sortABS(self, k, arr):
        # Sort the array using a custom key based on absolute difference with k
        arr.sort(key=lambda x: abs(x - k))
        return arr

# Example usage
solution = Solution()
print(solution.sortABS(7, [10, 5, 3, 9, 2]))  # Output: [5, 9, 10, 3, 2]
print(solution.sortABS(6, [1, 2, 3, 4, 5]))  # Output: [5, 4, 3, 2, 1]

'''
Here's a breakdown of the code:

class Solution:
Defines a class named Solution. This class contains methods that solve specific problems.

def sortABS(self, k, arr):
Defines a method called sortABS within the Solution class. This method takes two arguments: k, an integer, and arr, a list of integers. 
The goal of this method is to sort the array based on the absolute difference between each element and the value k.

arr.sort(key=lambda x: abs(x - k))
The sort method is called on the array arr. The key parameter is used to specify a custom sorting order. 
Here, a lambda function is passed as the key, which calculates the absolute difference between each element x in the array and k (abs(x - k)).
The array is sorted in ascending order based on these absolute differences. Elements closer to k will appear earlier in the sorted array.
The key parameter is used to specify a function that serves as a basis for sorting.
lambda is a keyword used to create an anonymous function (a function without a name). The syntax is lambda arguments: expression.
Custom Sort Key: The lambda x: abs(x - k) function is used as the sorting key. It calculates the absolute difference between each element and k.
The expression abs(x - k) computes the absolute difference between x and k. 
The abs() function returns the absolute value of a number, meaning it removes any negative sign.

return arr
The method returns the sorted array.

solution = Solution()
Creates an instance of the Solution class.

print(solution.sortABS(7, [10, 5, 3, 9, 2]))
Calls the sortABS method with k=7 and arr=[10, 5, 3, 9, 2]. The method sorts the array based on the absolute difference between 
each element and 7, resulting in [5, 9, 10, 3, 2], which is printed to the console.
For k = 7 and arr = [10, 5, 3, 9, 2]:
Differences: [3, 2, 4, 2, 5]
Sorted by differences: [5 (2), 9 (2), 10 (3), 3 (4), 2 (5)]
Result: [5, 9, 10, 3, 2]


print(solution.sortABS(6, [1, 2, 3, 4, 5]))
Calls the sortABS method with k=6 and arr=[1, 2, 3, 4, 5]. The method sorts the array based on the absolute difference between 
each element and 6, resulting in [5, 4, 3, 2, 1], which is printed to the console.
For k = 6 and arr = [1, 2, 3, 4, 5]:
Differences: [5, 4, 3, 2, 1]
Sorted by differences: [5 (1), 4 (2), 3 (3), 2 (4), 1 (5)]
Result: [5, 4, 3, 2, 1]
'''