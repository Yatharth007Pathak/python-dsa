"""
Given an array arr of non-negative integers. Find the length of the longest sub-sequence such that elements in the 
subsequence are consecutive integers, the consecutive numbers can be in any order.

Examples:

Input: arr[] = [2, 6, 1, 9, 4, 5, 3]
Output: 6
Explanation: The consecutive numbers here are 1, 2, 3, 4, 5, 6. These 6 numbers form the longest consecutive subsquence.

Input: arr[] = [1, 9, 3, 10, 4, 20, 2]
Output: 4
Explanation: 1, 2, 3, 4 is the longest consecutive subsequence.

Input: arr[] = [15, 13, 12, 14, 11, 10, 9]
Output: 7
Explanation: The longest consecutive subsequence is 9, 10, 11, 12, 13, 14, 15, which has a length of 7.
"""

class Solution:
    # Function to return length of longest subsequence of consecutive integers
    def findLongestConseqSubseq(self, arr):
        if not arr:
            return 0
        
        # Convert the array to a set for quick lookups
        num_set = set(arr)
        longest_streak = 0

        # Iterate through each number in the array
        for num in arr:
            # Check if the current number is the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                # Count consecutive numbers in the sequence
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                # Update the longest streak found
                longest_streak = max(longest_streak, current_streak)

        return longest_streak

# Example inputs
arr1 = [2, 6, 1, 9, 4, 5, 3]
arr2 = [1, 9, 3, 10, 4, 20, 2]
arr3 = [15, 13, 12, 14, 11, 10, 9]

# Creating an instance of Solution
solution = Solution()

# Finding the length of the longest consecutive subsequence
print(solution.findLongestConseqSubseq(arr1))  # Output: 6
print(solution.findLongestConseqSubseq(arr2))  # Output: 4
print(solution.findLongestConseqSubseq(arr3))  # Output: 7

'''
Here's a line-by-line breakdown of the code:

Class Solution:
Defines a class called Solution, which contains methods for solving array-related problems.

Method findLongestConseqSubseq:
Defines a function called findLongestConseqSubseq to find the length of the longest subsequence of consecutive integers in a given array (arr).

Check if Array is Empty:
if not arr: checks if the array is empty. If arr is empty, it returns 0 since there can't be any consecutive subsequence.

Convert Array to Set for Quick Lookups:
num_set = set(arr) converts the array arr into a set called num_set. 
This allows for fast membership checks (whether an integer is in the set), which improves the efficiency of the solution.

Initialize Longest Streak:
longest_streak = 0 initializes a variable to keep track of the longest sequence of consecutive numbers found so far.

Loop through Each Number in arr:
for num in arr: starts a loop to go through each number (num) in the array.

Check if the Current Number is the Start of a Sequence:
if num - 1 not in num_set: checks if num is the start of a new sequence by seeing if the number just before num is not in the set. 
If num - 1 is not in num_set, num is the beginning of a new sequence.

Initialize Current Sequence Tracking:
current_num = num initializes current_num to num, which will be used to keep track of the current sequence.
current_streak = 1 initializes current_streak to 1, which counts the number of consecutive elements in the current sequence.

Count Consecutive Numbers in the Sequence:
while current_num + 1 in num_set: starts a loop that continues as long as the 
next number in the sequence (current_num + 1) is present in num_set.
current_num += 1 increments current_num to the next consecutive number.
current_streak += 1 increments current_streak to count this consecutive element.

Update the Longest Streak Found:
longest_streak = max(longest_streak, current_streak) updates longest_streak with the maximum 
of the current longest streak or the current_streak.

Return the Result:
return longest_streak returns the length of the longest sequence of consecutive integers found in arr.

Example Arrays for Testing:
arr1, arr2, and arr3 define three test cases with different sets of integers to test the function.

Creating an Instance of Solution:
solution = Solution() creates an instance of the Solution class to access its methods.

Finding and Printing the Length of the Longest Consecutive Subsequence:
print(solution.findLongestConseqSubseq(arr1)) calls the findLongestConseqSubseq function with arr1 and prints the result, which is 6.
print(solution.findLongestConseqSubseq(arr2)) calls the findLongestConseqSubseq function with arr2 and prints the result, which is 4.
print(solution.findLongestConseqSubseq(arr3)) calls the findLongestConseqSubseq function with arr3 and prints the result, which is 7.
'''