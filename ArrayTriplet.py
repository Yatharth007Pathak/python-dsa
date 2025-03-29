"""
Given an array arr of size n and an integer x. Find if there's a triplet in the array which sums up to the given integer x.

Examples

Input:n = 6, x = 13, arr[] = [1,4,45,6,10,8]
Output: 1
Explanation: The triplet {1, 4, 8} in the array sums up to 13.

Input: n = 6, x = 10, arr[] = [1,2,4,3,6,7]
Output: 1
Explanation: Triplets {1,3,6} & {1,2,7} in the array sum to 10. 

Input: n = 6, x = 24, arr[] = [40,20,10,3,6,7]
Output: 0
Explanation: There is no triplet with sum 24. 
"""

class Solution:
    # Function to find if there exists a triplet in the array that sums to x
    def find3Numbers(self, arr, n, x):
        # Sort the array
        arr.sort()
        
        # Iterate over the array
        for i in range(n - 2):  # Since we need at least 3 numbers
            l = i + 1  # Left pointer
            r = n - 1  # Right pointer
            
            # Use two pointers to find the other two elements
            while l < r:
                current_sum = arr[i] + arr[l] + arr[r]
                
                # If we find the sum, return True
                if current_sum == x:
                    return 1
                
                # If current sum is less, move the left pointer to the right
                elif current_sum < x:
                    l += 1
                
                # If current sum is more, move the right pointer to the left
                else:
                    r -= 1
        
        # If no triplet is found, return False
        return 0

# Example usage:
sol = Solution()

# Test cases
print(sol.find3Numbers([1, 4, 45, 6, 10, 8], 6, 13))  # Output: 1
print(sol.find3Numbers([1, 2, 4, 3, 6, 7], 6, 10))    # Output: 1
print(sol.find3Numbers([40, 20, 10, 3, 6, 7], 6, 24)) # Output: 0

'''
Here is a line-by-line breakdown of the code:

Class Definition: The code defines a class named Solution. 
This class contains a function that checks if there are three numbers in an array that sum up to a given value.

Function Definition: The method find3Numbers is defined with parameters: arr (the array), n (the number of elements in the array), 
and x (the target sum we're looking for).

Sort the Array: The function first sorts the array to allow the use of a two-pointer approach. 
Sorting helps in narrowing down the search efficiently.

Iterate Over the Array: The function then iterates over the array using a for loop, but only until the third last element, 
because we need three numbers to form a triplet.

Set Two Pointers: Inside the loop, two pointers are initialized:

l (left pointer), which is set to the element immediately after the current element i.
r (right pointer), which is set to the last element of the array.
Two-Pointer Technique: The function uses a while loop, where the left pointer (l) moves towards the right, 
and the right pointer (r) moves towards the left. This technique helps find the sum of three numbers.

Check Current Sum: Inside the while loop, the sum of the current element (arr[i]) and the elements 
pointed to by l and r is calculated (current_sum).

Check if Sum Matches:

If the sum matches the target (x), the function returns 1 to indicate that a valid triplet is found.
Adjust Pointers Based on Sum:

If the current sum is less than the target, it means we need a larger number, so the left pointer (l) is moved to the right.
If the current sum is greater than the target, it means we need a smaller number, so the right pointer (r) is moved to the left.
Return if No Triplet is Found: If no valid triplet is found during the iteration, 
the function returns 0 to indicate that no such triplet exists in the array.

Example Usage: The code outside the class demonstrates how to use the find3Numbers method by creating an 
instance of the Solution class (sol) and calling the function with various test cases.

Test Cases: The output of the test cases:

In the first case, the function returns 1 because there is a triplet in the array that sums to 13.
In the second case, it also returns 1 for a triplet summing to 10.
In the third case, it returns 0 because no triplet in the array sums to 24.
'''