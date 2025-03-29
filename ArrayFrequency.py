"""
You are given an array arr[] containing positive integers. These integers can be from 1 to p, and some numbers may be repeated or absent. 
Your task is to count the frequency of all numbers that lie in the range 1 to n.

Note:

Do modify the array in-place changes in arr[], such that arr[i] = frequency(i) and assume 1-based indexing.
The elements greater than n in the array can be ignored when counting.

Examples

Input: n = 5, arr[] = [2, 3, 2, 3, 5], p = 5
Output: [0, 2, 2, 0, 1]
Explanation: Counting frequencies of each array element We have: 1 occurring 0 times. 2 occurring 2 times. 
3 occurring 2 times. 4 occurring 0 times. 5 occurring 1 time, all the modifications done in the same given arr[].

Input: n = 4, arr[] = [3, 3, 3, 3], p = 3
Output: [0, 0, 4, 0]
Explanation: Counting frequencies of each array element We have: 1 occurring 0 times. 2 occurring 0 times. 
3 occurring 4 times. 4 occurring 0 times.

Input: n = 2, arr[] = [8, 9], p = 9
Output: [0, 0]
Explanation: Counting frequencies of each array element We have: 1 occurring 0 times. 2 occurring 0 times. 
Since here P=9, but there are no 9th Index present so can't count the value.
"""

class Solution:
    # Function to count the frequency of all elements from 1 to N in the array.
    def frequencyCount(self, arr, N, P):
        # Step 1: Decrease each element by 1 to make it zero-indexed
        for i in range(N):
            arr[i] -= 1
        
        # Step 2: Increment frequency using index (modifying in-place)
        for i in range(N):
            # Only count values within range [0, N-1]
            if arr[i] % P < N:
                arr[arr[i] % P] += P
        
        # Step 3: Calculate the actual frequency
        for i in range(N):
            arr[i] = arr[i] // P

# Example 1
arr = [2, 3, 2, 3, 5]
N = 5
P = 5
solution = Solution()
solution.frequencyCount(arr, N, P)
print(arr)  # Output should be: [0, 2, 2, 0, 1]

# Example 2
arr = [3, 3, 3, 3]
N = 4
P = 3
solution.frequencyCount(arr, N, P)
print(arr)  # Output should be: [0, 0, 4, 0]

'''
Explanation:

Adjust Array to Zero-Indexed:
Since the array contains values from 1 to N, subtracting 1 from each element makes it zero-indexed. 
This way, the value of each element corresponds to a valid index in the array.

Use Modulo Operation for Counting:
For each element in the array, if the zero-indexed value (arr[i] % P) is within the range [0, N-1], 
it represents a valid number (from 1 to N). We then increment the value at that index by 
P to "mark" a count without disrupting the actual values. Using arr[arr[i] % P] += P allows us to encode counts in multiples of 
P, where arr[i] % P retrieves the original value at each step.

Extract Final Counts:
After all increments, arr[i] // P gives the number of times element i + 1 appeared in the array. 
We overwrite each position with this count, providing the required frequencies.

Complexity Analysis:
Time Complexity: O(N), where N is the length of the array. Each element is processed a constant number of times.
Space Complexity: O(1), as we are modifying the input array in-place.

Test Cases:
Example 1: arr = [2, 3, 2, 3, 5], N=5, P=5
Expected Output: [0, 2, 2, 0, 1]
Explanation: The count for elements 1, 2, 3, 4, 5 is 0, 2, 2, 0, 1.

Example 2: arr = [3, 3, 3, 3], N=4, P=3
Expected Output: [0, 0, 4, 0]
Explanation: The count for elements 1, 2, 3, 4 is 0, 0, 4, 0.

Each test confirms that the function successfully counts frequencies in the array from 1 to N. Great job!
'''