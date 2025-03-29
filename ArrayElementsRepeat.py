"""
Given an array arr of size n which contains elements in range from 0 to n-1, 
you need to find all the elements occurring more than once in the given array. 
Return the answer in ascending order. If no such element is found, return list containing [-1].

Example:
Input: n = 4, arr[] = [0,3,1,2]
Output: [-1]
Explanation: There is no repeating element in the array. Therefore output is -1.

Input: n = 5, arr[] = [2, 3, 1, 2, 3]
Output: [2, 3] 
Explanation: 2 and 3 occur more than once in the given array.

Input: n = 1, arr[] = [2]
Output: [] 
Explanation: There is single element in the array. Therefore output is empty.
"""

from typing import List

class Solution:
    def duplicates(self, n: int, arr: List[int]) -> List[int]:
        result = []

        # Traverse the array and mark visited elements by making the corresponding index negative
        for i in range(n):
            index = abs(arr[i])
            if arr[index] >= 0:
                arr[index] = -arr[index]
            else:
                result.append(index)

        # Sorting the result to ensure it is in ascending order
        result = sorted(set(result))

        # If no duplicates are found, return [-1]
        if not result:
            return [-1]
        
        return result


# Example usage:
solution = Solution()
print(solution.duplicates(5, [2, 3, 1, 2, 3]))  # Output: [2, 3]
print(solution.duplicates(3, [0, 1, 2]))        # Output: [-1]


'''
Here's a breakdown of the code line by line, explained in a pointwise manner:

from typing import List
This imports the List type from Python's typing module, allowing us to specify that a 
function parameter or return type should be a list of integers.

class Solution:
This defines a class named Solution. The class will contain methods to solve the problem at hand.

def duplicates(self, n: int, arr: List[int]) -> List[int]:
This defines a method named duplicates inside the Solution class.
It takes three parameters: self (the instance of the class), n (an integer representing the number of elements in the list), 
and arr (a list of integers).
The method is expected to return a list of integers (List[int]).

result = []
This initializes an empty list named result, which will store the duplicate elements found in the array.

for i in range(n):
This starts a for loop to iterate over each index i from 0 to n-1 in the array arr.

index = abs(arr[i])
This assigns the absolute value of the element at index i in arr to the variable index. 
The absolute value is used to handle cases where the element has already been marked as visited (i.e., made negative).

if arr[index] >= 0:
This checks if the element at position index in arr is non-negative, meaning it has not been visited before.

arr[index] = -arr[index]
If the element at position index is non-negative, it is made negative to mark it as visited. 
This indicates that the element corresponding to this index has been encountered.

else:
If the element at position index is already negative, it means the element corresponding to this index has been encountered before, 
indicating a duplicate.

result.append(index)
If a duplicate is found, the index (which corresponds to the duplicate element) is added to the result list.

result = sorted(set(result))
This removes any duplicate elements from the result list using set() and then sorts the list in ascending order.

if not result:
This checks if the result list is empty, which would mean no duplicates were found.

return [-1]
If no duplicates are found, the method returns a list containing -1.

return result
If duplicates are found, the method returns the sorted result list.

solution = Solution()
This creates an instance of the Solution class.

print(solution.duplicates(5, [2, 3, 1, 2, 3]))
This calls the duplicates method with an array of 5 elements [2, 3, 1, 2, 3] and prints the output. The expected output is [2, 3].

print(solution.duplicates(3, [0, 1, 2]))
This calls the duplicates method with an array of 3 elements [0, 1, 2] and prints the output. 
The expected output is [-1] since there are no duplicates.
'''