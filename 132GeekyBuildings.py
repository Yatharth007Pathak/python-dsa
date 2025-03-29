"""
There are N buildings in Linear Land. They appear in a linear line one after the other and their heights are given in the array arr[]. 
Geek wants to select three buildings in Linear Land and remodel them as recreational spots. 
The third of the selected building must be taller than the first and shorter than the second.
Can geek build the three-building recreational zone? 

Example 1:

Input: N = 6, arr[] = {4, 7, 11, 5, 13, 2}
Output: True
Explanation: [4, 7, 5] fits the condition. 

Example 2:

Input: N = 4, arr[] = {11, 11, 12, 9}
Output: False
Explanation: No 3 buildings fit the given condition. 
"""

class Solution:
    def recreationalSpot(self, arr, n):
        # Iterate over the array considering each element as the middle building
        for j in range(1, n - 1):
            left_set = set()
            right_set = set()

            # Check left buildings
            for i in range(j):
                if arr[i] < arr[j]:  # arr[i] can be the first building
                    left_set.add(arr[i])

            # Check right buildings
            for k in range(j + 1, n):
                if arr[k] > arr[j]:  # arr[k] can be the third building
                    right_set.add(arr[k])

            # If there is a valid combination of left and right buildings
            if left_set and right_set:
                return True
        
        return False

# Example usage:
solution = Solution()
print(solution.recreationalSpot([4, 7, 11, 5, 13, 2], 6))  # Output: True
print(solution.recreationalSpot([11, 11, 12, 9], 4))       # Output: False
