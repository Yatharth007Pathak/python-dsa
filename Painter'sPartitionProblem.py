"""
Dilpreet wants to paint his dog's home that has n boards with different lengths. 
The length of ith board is given by arr[i] where arr[] is an array of n integers. 
He hired k painters for this work and each painter takes 1 unit time to paint 1 unit of the board. 

The problem is to find the minimum time to get this job done if all painters start together with the constraint 
that any painter will only paint continuous boards, say boards numbered {2,3,4} or only board {1} or nothing but not boards {2,4,5}.

Input: n = 5, k = 3, arr[] = {5,10,30,20,15}
Output: 35
Explanation: The most optimal way will be: Painter 1 allocation : {5,10}, Painter 2 allocation : {30}, Painter 3 allocation : 
{20,15}, Job will be done when all painters finish i.e. at time = max(5+10, 30, 20+15) = 35

Input: n = 4, k = 2, arr[] = {10,20,30,40}
Output: 60
Explanation: The most optimal way to paint: Painter 1 allocation : {10,20,30}, Painter 2 allocation : {40}, Job will be complete at time = 60
"""

class Solution:
    def minTime(self, arr, n, k):
        # Helper function to check if we can allocate boards within max_time with k painters
        def is_possible(arr, n, k, max_time):
            total = 0
            painters = 1
            for length in arr:
                total += length
                if total > max_time:
                    # If total exceeds max_time, we need a new painter
                    painters += 1
                    total = length
                    if painters > k:
                        return False
            return True
        
        # Binary search on the answer
        left, right = max(arr), sum(arr)
        result = right
        
        while left <= right:
            mid = (left + right) // 2
            if is_possible(arr, n, k, mid):
                result = mid  # Update result if feasible
                right = mid - 1  # Try for a smaller max_time
            else:
                left = mid + 1  # Increase max_time
                
        return result

solution = Solution()

# Test case 1
arr1 = [5, 10, 30, 20, 15]
n1, k1 = 5, 3
print(solution.minTime(arr1, n1, k1))

# Test case 2
arr2 = [10, 20, 30, 40]
n2, k2 = 4, 2
print(solution.minTime(arr2, n2, k2))

# Test case 3 - Edge case with all boards of the same length
arr3 = [10, 10, 10, 10]
n3, k3 = 2
print(solution.minTime(arr3, n3, k3))

# Test case 4 - Only one painter
arr4 = [10, 20, 30, 40]
n4, k4 = 1
print(solution.minTime(arr4, n4, k4))

# Test case 5 - More painters than boards
arr5 = [5, 10, 15]
n5, k5 = 5
print(solution.minTime(arr5, n5, k5))

'''
Here's a line-by-line breakdown of the code in plain text.

Define a class Solution: This class is intended to contain the function minTime, 
which calculates the minimum time required to paint boards given a number of painters.

Define the function minTime within Solution: This function takes four parameters:
arr: an array of integers representing the lengths of boards.
n: the number of boards.
k: the number of painters available.

Define a helper function is_possible within minTime: This nested function checks if it is 
feasible to paint all boards within a given maximum time, max_time, with k painters.

Initialize variables total and painters in is_possible: total accumulates the length a painter can paint before reaching the limit max_time, 
and painters keeps track of the number of painters needed.

Start a loop over each board length in arr: Each board length is added to the total.

Check if total exceeds max_time: If it does, it means that one painter cannot paint more, so a new painter is required.

Increment painters and reset total: A new painter starts with the current board, so total is reset to this board's length.

Check if painters exceeds k: If more painters than available are required, return False (indicating it's not possible within max_time).

Return True if all boards can be painted within max_time: This indicates the maximum time limit is feasible with k painters.

Set initial values for left and right: left is the length of the longest board (minimum possible time), 
and right is the total length of all boards (maximum possible time).

Initialize result to right: Start by assuming the maximum time required, which will be updated with the minimum feasible time.

Begin a binary search loop while left is less than or equal to right: 
This loop finds the smallest max_time that can accommodate all boards with k painters.

Calculate mid as the midpoint of left and right: This mid represents a candidate max_time.

Call is_possible with mid to check feasibility: If the current mid is feasible with k painters, update result to mid.

Adjust right to mid - 1: This reduces the possible range, attempting to find a smaller max_time.

If mid is not feasible, increment left: This means a larger max_time is required to accommodate all boards with k painters.

Return result: After finding the minimum feasible max_time, return it as the final result.

Create an instance of Solution: Instantiate the Solution class to use the minTime method.

The test cases below run different scenarios to validate the minTime function. Explanation of Test Cases-
Test Case 1: The example case from the prompt, with an expected output of 35.
Test Case 2: Another prompt example, with an expected output of 60.
Test Case 3: All boards have the same length; expected output is 20 since two painters can split the boards equally.
Test Case 4: Only one painter, so they paint all boards sequentially; expected output is 100.
Test Case 5: More painters than boards; each board can be assigned to one painter, so expected output is the length of the longest board, 15.
'''