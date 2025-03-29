"""
You are given weights and values of items, and put these items in a knapsack of capacity W to get the maximum total value in the knapsack. 
Note that we have only one quantity of each item.
In other words, given two integer arrays val and wt which represent values and weights associated with items respectively. 
Also given an integer W which represents knapsack capacity, find out the maximum sum values subset of val[] 
such that the sum of the weights of the corresponding subset is smaller than or equal to W. 
You cannot break an item, either pick the complete item or don't pick it (0-1 property).

Examples :

Input: W = 4, val[] = {1,2,3}, wt[] = {4,5,1}
Output: 3
Explanation: Choose the last item that weighs 1 unit and holds a value of 3. 

Input: W = 3, val[] = {1,2,3}, wt[] = {4,5,6}
Output: 0
Explanation: Every item has a weight exceeding the knapsack's capacity (3).
"""

class Solution:
    
    # Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self, W, wt, val):
        n = len(val)  # Number of items
        
        # Create a DP table to store the maximum value that can be obtained for each weight capacity
        dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
        
        # Build the table dp[][] in a bottom-up manner
        for i in range(1, n + 1):
            for w in range(1, W + 1):
                if wt[i-1] <= w:
                    # We either include the item i-1 or exclude it
                    dp[i][w] = max(val[i-1] + dp[i-1][w-wt[i-1]], dp[i-1][w])
                else:
                    # If the weight of the item is more than the capacity, we exclude it
                    dp[i][w] = dp[i-1][w]
        
        # The last cell of dp[n][W] will contain the maximum value we can obtain with n items and weight W
        return dp[n][W]

# Example usage:
W = 4
val = [1, 2, 3]
wt = [4, 5, 1]
solution = Solution()
print(solution.knapSack(W, wt, val))  # Output: 3

'''
Here's a line-by-line breakdown of the code:

class Solution:
A class named Solution is defined to contain the knapSack method.

def knapSack(self, W, wt, val):
The function knapSack is defined, which takes three parameters:

W is the maximum weight capacity of the knapsack.
wt is a list of item weights.
val is a list of item values corresponding to the weights.

n = len(val):
The variable n is initialized to store the number of items, which is the length of the val array.

dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]:
A 2D list dp is created. It has dimensions (n + 1) x (W + 1), where:
n + 1 rows correspond to the number of items plus one (for handling 0 items case).
W + 1 columns correspond to the weight capacity from 0 to W. Each element in the table is initialized to 0.

for i in range(1, n + 1):
A loop starts from 1 to n, iterating over all items.

for w in range(1, W + 1):
Another loop iterates over all possible weight capacities from 1 to W.

if wt[i-1] <= w:
This checks if the current item's weight (indexed as wt[i-1] because arrays are 0-based) is less than or equal to the current weight capacity w.

dp[i][w] = max(val[i-1] + dp[i-1][w-wt[i-1]], dp[i-1][w]):
If the item's weight is less than or equal to w, there are two possibilities:

Include the current item: Add the value of the current item (val[i-1]) to the optimal solution for the remaining weight (w - wt[i-1]).
Exclude the current item: Take the optimal solution from the previous row (dp[i-1][w]). The max() function is used to select the better option.

else:
If the current item's weight exceeds the current weight capacity w.

dp[i][w] = dp[i-1][w]:
If the current item cannot be included due to weight, 
the solution for this weight capacity is the same as the solution for the previous item (dp[i-1][w]).

return dp[n][W]:
After the table is fully constructed, the maximum value that can be obtained with n items and a knapsack capacity of W is stored in dp[n][W].

Example usage:

W = 4:
Defines the weight capacity of the knapsack.

val = [1, 2, 3]:
A list of values for the items.

wt = [4, 5, 1]:
A list of weights corresponding to the values.

solution = Solution():
Creates an instance of the Solution class.

print(solution.knapSack(W, wt, val)):
Calls the knapSack method with the given inputs and prints the result, which in this case is 3.

This implementation solves the 0/1 Knapsack problem using dynamic programming. 
The result 3 means that the maximum value that can be obtained within the weight capacity of 4 is 3, achieved by taking the third item.
'''