"""
Given an integer k and array arr. Your task is to return the position of the first occurrence of k 
in the given array and if element k is not present in the array then return -1.
Note: 1-based indexing is followed here.

Examples:

Input: k = 16 , arr = [9, 7, 16, 16, 4]
Output: 3
Explanation: The value 16 is found in the given array at positions 3 and 4, with position 3 being the first occurrence.

Input: k=98 , arr = [1, 22, 57, 47, 34, 18, 66]
Output: -1
Explanation: k = 98 isn't found in the given array.    
"""

from typing import List

class Solution:
    def search(self, k: int, arr: List[int]) -> int:
        # Loop through the array using 1-based indexing
        for i in range(len(arr)):
            if arr[i] == k:
                return i + 1  # Return 1-based index
        return -1  # Return -1 if k is not found

s = Solution()
print(s.search(16, [9, 7, 16, 16, 4]))  # Output: 3
print(s.search(98, [1, 22, 57, 47, 34, 18, 66]))  # Output: -1

'''
Here's a breakdown of the code line by line:

from typing import List: This imports List from the typing module, which allows for type hinting that an argument is a list of integers.

class Solution:: A class named Solution is defined to encapsulate the search method.

def search(self, k: int, arr: List[int]) -> int:: The method search is defined within the Solution class. Here's a detailed explanation:

def: This keyword is used to define a function or method in Python.
search: This is the name of the method being defined. In this case, it's named search, indicating that it will perform a search operation.

self: This is a reference to the instance of the class in which this method is defined. 
It allows the method to access attributes and other methods of the class. 
It must be the first parameter of any method inside a class, but it's not passed explicitly when the method is called on an object.

k: int: This defines the first parameter k, which is expected to be of type int (an integer). 
This is the element the method will search for in the list arr.

arr: List[int]: This defines the second parameter arr, which is a list of integers. 
The List[int] type hint is provided by the typing module, and it indicates that arr is expected to be a list where each element is an integer.

-> int: This specifies the return type of the method. In this case, -> int means the method is expected to return an integer. 
This integer will be the 1-based index of the found element, or -1 if the element is not found.

for i in range(len(arr)):: A for loop is initiated to iterate over the array. i is the index variable, ranging from 0 to len(arr) - 1.

if arr[i] == k:: Inside the loop, it checks if the current element in the array (arr[i]) is equal to k, the target value.

return i + 1: If the target value is found, the function returns the index i plus 1 to account for 1-based indexing.

return -1: If the loop completes without finding the target value k, 
the function returns -1 to indicate that the value was not found in the array.

s = Solution(): An instance of the Solution class is created and stored in the variable s.

print(s.search(16, [9, 7, 16, 16, 4])): The search method is called with the target 16 and the array [9, 7, 16, 16, 4]. 
The expected output is 3, as the first occurrence of 16 is at index 2, and returning 1-based indexing gives 3.

print(s.search(98, [1, 22, 57, 47, 34, 18, 66])): The search method is called with the target 98 and the array [1, 22, 57, 47, 34, 18, 66]. 
Since 98 is not present in the array, the expected output is -1.
'''