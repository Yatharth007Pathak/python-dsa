"""
Given an array arr of n positive integers, your task is to find all the leaders in the array. 
An element of the array is considered a leader if it is greater than all the elements on its right side 
or if it is equal to the maximum element on its right side. The rightmost element is always a leader.

Examples

Input: n = 6, arr[] = {16,17,4,3,5,2}
Output: [17, 5, 2]
Explanation: Note that there is nothing greater on the right side of 17, 5 and, 2.

Input: n = 5, arr[] = {10,4,2,4,1}
Output: [10, 4, 4, 1]
Explanation: Note that both of the 4s are in output, as to be a leader an equal element is also allowed on the right side

Input: n = 4, arr[] = {5, 10, 20, 40} 
Output: [40]
Explanation: When an array is sorted in increasing order, only the rightmost element is leader.

Input: n = 4, arr[] = {30, 10, 10, 5} 
Output: [30, 10, 10, 5]
Explanation: When an array is sorted in non-increasing order, all elements are leaders.
"""

class Solution:
    def leaders(self, n, arr):
        leaders_list = []
        max_from_right = arr[-1]  # The rightmost element is always a leader
        leaders_list.append(max_from_right)
        
        # Traverse the array from second last element to the first
        for i in range(n - 2, -1, -1):
            if arr[i] >= max_from_right:
                leaders_list.append(arr[i])
                max_from_right = arr[i]
        
        # The leaders are collected in reverse order, so reverse the list before returning
        leaders_list.reverse()
        return leaders_list

# Example usage:
sol = Solution()

arr1 = [16, 17, 4, 3, 5, 2]
print(sol.leaders(6, arr1))  # Output: [17, 5, 2]

arr2 = [10, 4, 2, 4, 1]
print(sol.leaders(5, arr2))  # Output: [10, 4, 4, 1]

arr3 = [5, 10, 20, 40]
print(sol.leaders(4, arr3))  # Output: [40]

arr4 = [30, 10, 10, 5]
print(sol.leaders(4, arr4))  # Output: [30, 10, 10, 5]

'''
Here's a line-by-line breakdown of the provided code:

class Solution:
This defines a class Solution, which will contain the method for finding leaders in an array.

def leaders(self, n, arr):
Defines a method leaders inside the class Solution.
self: A reference to the instance of the class.
n: The length of the array.
arr: The input array of integers.

leaders_list = []
max_from_right = arr[-1]
leaders_list: Initializes an empty list to store the leaders.
max_from_right: Assigns the last element of the array (arr[-1]) to this variable. 
Since the rightmost element is always a leader, we start by assuming it is the maximum element we've encountered so far.

leaders_list.append(max_from_right)
The rightmost element (arr[-1]) is appended to the leaders_list because it's always a leader.

for i in range(n - 2, -1, -1):
This starts a for loop that goes from the second-to-last element (n - 2) down to the first element (0). 
Looping Through the Array from Right to Left
range(n - 2, -1, -1): This specifies the range to loop through the array in reverse order, moving from index n-2 to index 0.

if arr[i] >= max_from_right:
Checks if the current element (arr[i]) is greater than or equal to max_from_right. 
If true, it means this element is also a leader because it's greater than or equal to all elements to its right.

leaders_list.append(arr[i])
max_from_right = arr[i]
If the condition is satisfied, the current element (arr[i]) is appended to the leaders_list.
Then, max_from_right is updated to this current element (arr[i]), since it becomes the new maximum element encountered so far from the right.

leaders_list.reverse()
The leaders were added in reverse order (starting from the right of the array). 
So, before returning the result, we reverse the leaders_list to maintain the correct order from left to right.

return leaders_list
Returns the final list of leaders.

sol = Solution()
Creates an instance of the Solution class called sol.

arr1 = [16, 17, 4, 3, 5, 2]
print(sol.leaders(6, arr1))
Calls the leaders method with arr1 and n=6 (length of the array). Prints the result, which is [17, 5, 2].

arr2 = [10, 4, 2, 4, 1]
print(sol.leaders(5, arr2))
Calls the leaders method with arr2 and n=5. Prints the result, which is [10, 4, 4, 1].

arr3 = [5, 10, 20, 40]
print(sol.leaders(4, arr3))
Calls the leaders method with arr3 and n=4. Prints the result, which is [40].

arr4 = [30, 10, 10, 5]
print(sol.leaders(4, arr4))
Calls the leaders method with arr4 and n=4. Prints the result, which is [30, 10, 10, 5].
'''