"""
Given an array arr[] with repeated elements, the task is to find the maximum distance between two occurrences of an element.

Note: You may assume that every input array has repetitions.

Examples:

Input: arr = [1, 1, 2, 2, 2, 1]
Output: 5
Explanation: distance for 1 is: 5-0 = 5, distance for 2 is : 4-2 = 2, So max distance is 5.

Input: arr = [3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2]
Output: 10
Explanation: maximum distance for 2 is 11-1 = 10, maximum distance for 1 is 4-2 = 2 ,maximum distance for 4 is 10-5 = 5, So max distance is 10.
"""

class Solution:
    def maxDistance(self, arr) -> int:
        # Dictionary to store the first occurrence of each element
        first_occurrence = {}
        max_dist = 0

        # Iterate through the array
        for i in range(len(arr)):
            if arr[i] not in first_occurrence:
                # Store the index of the first occurrence
                first_occurrence[arr[i]] = i
            else:
                # Calculate the distance from the first occurrence
                dist = i - first_occurrence[arr[i]]
                # Update the maximum distance
                max_dist = max(max_dist, dist)

        return max_dist

# Example usage
sol = Solution()
print(sol.maxDistance([1, 1, 2, 2, 2, 1]))        # Output: 5
print(sol.maxDistance([3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2]))  # Output: 10


'''
The maxDistance method efficiently computes the maximum distance between the first and last occurrence 
of the same element by storing the index of the first occurrence of each element in a dictionary and then calculating 
the distance between the first and subsequent occurrences. The maximum distance is updated and returned as the result.


Code Breakdown

class Solution:
Defines a class Solution that encapsulates the functionality of the method maxDistance.

def maxDistance(self, arr) -> int:
This defines a method maxDistance which takes a list arr as input and returns an integer representing 
the maximum distance between the first and last occurrence of the same element.

first_occurrence = {}
This initializes an empty dictionary first_occurrence to store the index of the first occurrence of each element in the array.

max_dist = 0
This initializes the variable max_dist to 0, which will keep track of the maximum distance between the first and last occurrence of an element.

for i in range(len(arr)):
A for loop iterates through the array arr using the index i.

if arr[i] not in first_occurrence:
This checks if the element arr[i] has not been encountered before.

first_occurrence[arr[i]] = i
If the element arr[i] is encountered for the first time, its index i is stored in the first_occurrence dictionary.

else:
This block runs if the element arr[i] has already been encountered before, meaning it is a repeated element.

dist = i - first_occurrence[arr[i]]
The distance between the first occurrence and the current occurrence of arr[i] is calculated as i - first_occurrence[arr[i]].

max_dist = max(max_dist, dist)
The maximum distance max_dist is updated by taking the maximum of the current max_dist and the newly calculated distance dist.

return max_dist
After the loop finishes, the method returns the maximum distance found.

sol = Solution()
Creates an instance of the Solution class.

print(sol.maxDistance([1, 1, 2, 2, 2, 1]))
Calls the maxDistance method with the array [1, 1, 2, 2, 2, 1].
The maximum distance is 5, between the first occurrence of 1 at index 0 and its last occurrence at index 5.

print(sol.maxDistance([3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2]))
Calls the maxDistance method with the array [3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2].
The maximum distance is 10, between the first occurrence of 2 at index 1 and its last occurrence at index 11.
'''