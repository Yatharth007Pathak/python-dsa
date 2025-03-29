"""
Given an array arr[ ] of length N consisting cost of N toys and an integer K depicting the amount with you. 
Your task is to find maximum number of toys you can buy with K amount. 

Example 1:
Input: N = 7, K = 50, arr[] = {1, 12, 5, 111, 200, 1000, 10}
Output: 4
Explaination: The costs of the toys you can buy are 1, 12, 5 and 10.

Example 2:
Input: N = 3, K = 100, arr[] = {20, 30, 50}
Output: 3
Explaination: You can buy all toys.
"""

class Solution:
    def toyCount(self, N, K, arr):
        # Sort the array of toy costs in ascending order
        arr.sort()
        
        # Initialize the count of toys we can buy and the total cost so far
        count = 0
        total_cost = 0
        
        # Iterate through the sorted array
        for cost in arr:
            # If adding the current toy's cost doesn't exceed the budget
            if total_cost + cost <= K:
                total_cost += cost
                count += 1
            else:
                # If adding the cost exceeds the budget, break the loop
                break
        
        return count

# Example usage:
sol = Solution()
print(sol.toyCount(7, 50, [1, 12, 5, 111, 200, 1000, 10]))  # Output: 4
print(sol.toyCount(3, 100, [20, 30, 50]))  # Output: 3

'''
Here's a pointwise explanation for each line of the given code:

class Solution:
Defines a class named Solution.

def toyCount(self, N, K, arr):
Defines a function named toyCount which takes three arguments: N (number of toys), K (budget), and arr (list of toy costs).

arr.sort()
Sorts the array arr of toy costs in ascending order so that cheaper toys can be bought first.

count = 0
Initializes count to 0, representing the number of toys that can be bought.

total_cost = 0
Initializes total_cost to 0, representing the current total cost of toys bought.

for cost in arr:
Starts a for loop to iterate over each toy cost in the sorted array arr.

if total_cost + cost <= K:
Checks if adding the current toy's cost to total_cost does not exceed the budget K.

total_cost += cost
If the budget allows, adds the current toy's cost to total_cost.

count += 1
Increments count by 1 to indicate that one more toy has been bought.

else:
If adding the current toy's cost exceeds the budget, executes the next statement.

break
Breaks out of the loop since no more toys can be bought within the budget.

return count
Returns the value of count, which is the total number of toys that can be bought.

# Example usage:
Adds a comment indicating the start of example usage of the function.

sol = Solution()
Creates an instance of the Solution class.

print(sol.toyCount(7, 50, [1, 12, 5, 111, 200, 1000, 10])) # Output: 4
Calls toyCount with N=7, K=50, and the toy costs [1, 12, 5, 111, 200, 1000, 10]. 
Prints the result, which is 4 (indicating that 4 toys can be bought within the budget).

print(sol.toyCount(3, 100, [20, 30, 50])) # Output: 3
Calls toyCount with N=3, K=100, and the toy costs [20, 30, 50]. 
Prints the result, which is 3 (indicating that all 3 toys can be bought within the budget).
'''