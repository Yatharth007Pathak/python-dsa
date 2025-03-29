"""
Given an positive integer N and a list of N integers A[]. Each element in the array denotes the maximum length of jump you can cover. 
Find out if you can make it to the last index if you start at the first index of the list.

Example 1:
Input: N = 6, A[] = {1, 2, 0, 3, 0, 0} 
Output: 1
Explanation: Jump 1 step from first index to second index. Then jump 2 steps to reach 4th index, and now jump 2 steps to reach the end.

Example 2:
Input: N = 3, A[] =  {1, 0, 2}
Output: 0
Explanation: You can't reach the end of the array.
"""

class Solution:
    def canReach(self, A, N):
        # Initialize the farthest reach we can get to
        maxReach = 0
        
        # Traverse the array
        for i in range(N):
            # If the current index is beyond the maxReach, return 0 (can't move forward)
            if i > maxReach:
                return 0
            
            # Update maxReach to the farthest point we can reach from the current index
            maxReach = max(maxReach, i + A[i])
            
            # If we can reach the last index or beyond, return 1
            if maxReach >= N - 1:
                return 1
        
        return 0  # If we finish the loop and haven't reached the last index, return 0

# Example usage:
solution = Solution()
print(solution.canReach([1, 2, 0, 3, 0, 0], 6))  # Output: 1
print(solution.canReach([1, 0, 2], 3))           # Output: 0

'''
Line-by-Line Breakdown:

class Solution:
This defines a class Solution that contains the method canReach.

def canReach(self, A, N):
This defines the function canReach which takes two parameters:
A: an array of integers representing how far you can jump from each index.
N: the length of the array A.

maxReach = 0
The variable maxReach is initialized to 0. This will store the farthest index we can reach from the current or any previous index.

for i in range(N):
A loop starts, iterating over each index i of the array A.

if i > maxReach:
This checks if the current index i is beyond the farthest index we can reach (maxReach). If true, this means we cannot progress further, so:

return 0
If we reach an index that is beyond maxReach, we immediately return 0, indicating that it's impossible to reach the end of the array.

maxReach = max(maxReach, i + A[i])
This updates maxReach to the farthest position we can reach from the current index i. 
The value i + A[i] represents the farthest index we can jump to from index i. 
We take the maximum of the current maxReach and this new possible position.

if maxReach >= N - 1:
This checks if the farthest position we can reach (maxReach) is beyond or equal to the last index (N - 1).

return 1
If maxReach is greater than or equal to the last index, we can reach the end, so we return 1.

return 0
If the loop finishes and we haven't returned 1, it means that we cannot reach the last index, so the function returns 0.

solution = Solution()
Creates an instance of the Solution class.

print(solution.canReach([1, 2, 0, 3, 0, 0], 6)) # Output: 1
This call checks whether it's possible to reach the end of the array [1, 2, 0, 3, 0, 0]. The output is 1, meaning we can reach the last index.

print(solution.canReach([1, 0, 2], 3)) # Output: 0
This call checks if we can reach the end of the array [1, 0, 2]. The output is 0, meaning it's impossible to reach the last index.

Time Complexity: O(N) where N is the size of the array. We only need one pass through the array.
Space Complexity: O(1) since we only use a few extra variables for the solution.
'''