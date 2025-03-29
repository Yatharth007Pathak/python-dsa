"""
Given a set of items, each with a weight and a value, represented by the array wt and val respectively. 
Also, a knapsack with weight limit capacity.
The task is to fill the knapsack in such a way that we can get the maximum profit. Return the maximum profit.
Note: Each item can be taken any number of times.

Examples:

Input: capacity = 3, val = [1, 1], wt = [2, 1]
Output: 3
Explanation:
1.Pick the 2nd element thrice.
2.Total profit = 1 + 1 + 1 = 3.
Also the total weight = 1 + 1 + 1  = 3 which is <= 3.

Input: capacity = 8, val[] = [6, 1, 7, 7], wt[] = [1, 3, 4, 5]
Output: 48
Explanation: The optimal choice is to pick the 1st element 8 times.

Input: capacity = 1, val[] = [6, 8, 7, 100], wt[] = [2, 3, 4, 5]
Output: 0
Explanation: We can't pick any element .hence, total profit is 0.
"""

class Solution:
    def knapSack(self, capacity, val, wt):
        # Initialize dp array with 0's, where dp[i] represents max profit for capacity i
        dp = [0] * (capacity + 1)
        
        # Loop through all capacities from 1 to the given capacity
        for i in range(1, capacity + 1):
            # For each item, check if it can contribute to the maximum profit at this capacity
            for j in range(len(wt)):
                if wt[j] <= i:  # If item j can fit into the current capacity i
                    # Calculate the profit if we include this item
                    dp[i] = max(dp[i], dp[i - wt[j]] + val[j])
        
        # The maximum profit for the given capacity
        return dp[capacity]

# Example usage
solution = Solution()
capacity = 3
val = [1, 1]
wt = [2, 1]
print(solution.knapSack(capacity, val, wt))  # Output: 3

capacity = 8
val = [6, 1, 7, 7]
wt = [1, 3, 4, 5]
print(solution.knapSack(capacity, val, wt))  # Output: 48

'''
Here is a line-by-line explanation of the code:

class Solution:
Defines a class called Solution. In Python, classes are used to organize code and group related functions.

def knapSack(self, capacity, val, wt):
Defines a method within the Solution class called knapSack, which takes the parameters: capacity (the knapsack's maximum weight capacity), 
val (a list of item values), and wt (a list of item weights). self represents the instance of the class.

dp = [0] * (capacity + 1)
Creates a list called dp of size capacity + 1, filled with zeros. This list will store the maximum profit possible for 
each capacity from 0 to the given capacity.

for i in range(1, capacity + 1):
Starts a loop over capacities i from 1 up to and including the given capacity. This loop iterates through each possible knapsack capacity.

for j in range(len(wt)):
Starts a nested loop that goes through each item by its index j in the list wt.

if wt[j] <= i:
Checks if the weight of item j is less than or equal to the current capacity i. 
This condition determines if item j can fit into a knapsack of size i.

dp[i] = max(dp[i], dp[i - wt[j]] + val[j])
Updates dp[i] to the maximum of its current value and the value obtained by including item j. The expression dp[i - wt[j]] + val[j] 
calculates the new value by adding the value of item j to the best profit achievable with the remaining capacity (i - wt[j]).

return dp[capacity]
After both loops are complete, dp[capacity] contains the maximum profit for the given capacity, and this value is returned as the result.

Example Usage:
solution = Solution()
Creates an instance of the Solution class called solution.

capacity = 3
Sets the knapsack capacity to 3.

val = [1, 1]
Defines a list val where each element represents the value of an item.

wt = [2, 1]
Defines a list wt where each element represents the weight of an item.

print(solution.knapSack(capacity, val, wt)) # Output: 3
Calls the knapSack method on solution with the given capacity, val, and wt. This prints the maximum profit that can be achieved, which is 3.

capacity = 8
Sets the knapsack capacity to 8 for a second example.

val = [6, 1, 7, 7]
Defines a new list val of item values.

wt = [1, 3, 4, 5]
Defines a new list wt of item weights.

print(solution.knapSack(capacity, val, wt)) # Output: 48
Calls the knapSack method again with the new capacity, val, and wt. 
This prints the maximum profit that can be achieved with these items and capacity, which is 48.
'''