"""
Given an array arr consisting of positive integers numbers, remove all duplicates.

Example:

Input: arr[] = [2, 2, 3, 3, 7, 5] 
Output: [2, 3, 7, 5]
Explanation: After removing the duplicates 2 and 3 we get 2 3 7 5.

Input: arr[] = [2, 2, 5, 5, 7, 7] 
Output: [2, 5, 7]
Explanation: After removing the duplicates 2, 5 and 7 we get 2 5 7.
"""

class Solution:
    def removeDuplicates(self, arr):
        seen = set()  # Create a set to keep track of seen numbers
        result = []   # Create a list to store the result
        
        for num in arr:
            if num not in seen:  # If the number has not been seen yet
                seen.add(num)    # Add it to the set of seen numbers
                result.append(num)  # Append it to the result list
                
        return result  # Return the result list

# Example usage:
solution = Solution()
print(solution.removeDuplicates([2, 2, 3, 3, 7, 5]))  # Output: [2, 3, 7, 5]
print(solution.removeDuplicates([2, 2, 5, 5, 7, 7]))  # Output: [2, 5, 7]

'''
Here's a pointwise breakdown for each line of the code:

class Solution:
Defines a class named Solution.

def removeDuplicates(self, arr):
Defines a method called removeDuplicates that takes self (reference to the object) and arr (a list of integers) as parameters.

seen = set()
Initializes an empty set called seen to keep track of the numbers that have already been encountered.

result = []
Initializes an empty list called result to store the unique numbers from the input list.

for num in arr:
Starts a loop that iterates through each number (num) in the input list arr.

if num not in seen:
Checks if the current number num is not already in the seen set.

seen.add(num)

If the number has not been seen yet, adds it to the seen set.

result.append(num)
Appends the unique number num to the result list.

return result
After the loop completes, returns the result list containing only the unique numbers.

solution = Solution()
Creates an instance of the Solution class.

print(solution.removeDuplicates([2, 2, 3, 3, 7, 5]))
Calls the removeDuplicates method with the list [2, 2, 3, 3, 7, 5] and prints the result ([2, 3, 7, 5]).

print(solution.removeDuplicates([2, 2, 5, 5, 7, 7]))
Calls the removeDuplicates method with the list [2, 2, 5, 5, 7, 7] and prints the result ([2, 5, 7]).
'''