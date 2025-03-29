"""
You are given an array a, of n elements. Find the minimum index based distance between two distinct elements of the array, x and y. 
Return -1, if either x or y does not exist in the array.

Example 1:

Input: N = 4, A[] = {1,2,3,2}, x = 1, y = 2
Output: 1
Explanation: x = 1 and y = 2. There are two distances between x and y, which are 1 and 3 out of which the least is 1.

Example 2:
Input: N = 7, A[] = {86,39,90,67,84,66,62}, x = 42, y = 12, 
Output: -1
Explanation: x = 42 and y = 12. We return -1 as x and y don't exist in the array.
"""

class Solution:
    def minDist(self, arr, n, x, y):
        # Initialize the positions of x and y as -1 (meaning not found yet)
        x_pos = -1
        y_pos = -1
        min_distance = float('inf')  # Use infinity as the initial value for comparison
        
        # Traverse the array
        for i in range(n):
            if arr[i] == x:
                x_pos = i  # Update the position of x
            elif arr[i] == y:
                y_pos = i  # Update the position of y
            
            # If both x and y have been found, calculate the distance
            if x_pos != -1 and y_pos != -1:
                min_distance = min(min_distance, abs(x_pos - y_pos))
        
        # If the minimum distance was updated, return it, otherwise return -1
        return min_distance if min_distance != float('inf') else -1

solution = Solution()

arr1 = [1, 2, 3, 2]
n1 = 4
x1 = 1
y1 = 2
print(solution.minDist(arr1, n1, x1, y1))  # Output: 1

arr2 = [86, 39, 90, 67, 84, 66, 62]
n2 = 7
x2 = 42
y2 = 12
print(solution.minDist(arr2, n2, x2, y2))  # Output: -1

'''

This code defines a method minDist within the Solution class that calculates the 
minimum distance between two elements, x and y, in an array arr of length n.

Breakdown of the Code:

Initialize Variables:
x_pos and y_pos are initialized to -1, which means the positions of x and y are unknown at the start.
min_distance is set to infinity (float('inf')) because we want to keep track of the smallest distance, 
and infinity provides a useful initial comparison value.

Traverse the Array: The function iterates over the array using a for loop:
If the current element arr[i] is equal to x, x_pos is updated to i (the index of x).
If the current element arr[i] is equal to y, y_pos is updated to i (the index of y).

Calculate Minimum Distance:
If both x_pos and y_pos are not -1 (which means both x and y have been found), 
the function calculates the absolute difference between their positions using abs(x_pos - y_pos).
It then updates min_distance to the smaller of the current min_distance and the newly calculated distance.

Return the Result:
If min_distance has been updated from infinity (meaning both x and y were found), it returns the minimum distance.
Otherwise, if either x or y was not found, it returns -1.

Example 1:
Input: arr = [1, 2, 3, 2], x = 1, y = 2
The minimum distance between x = 1 and y = 2 is 1, because 1 is at index 0 and the nearest 2 is at index 1.

Example 2:
Input: arr = [86, 39, 90, 67, 84, 66, 62], x = 42, y = 12
Since neither 42 nor 12 is present in the array, the function returns -1.

Edge Cases:
If either x or y is not present in the array, the function returns -1.
If x and y appear multiple times, it calculates the smallest distance between any pair of occurrences.
This approach efficiently finds the minimum distance in a single pass with a time complexity of O(n).
'''