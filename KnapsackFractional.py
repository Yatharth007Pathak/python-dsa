"""
Given two arrays value[] and weight[], you need to put these items in a knapsack of capacity w to get the maximum total value in the knapsack. 
Return a double value representing the maximum value in the knapsack, rounded to 6 decimal places.

Note: Unlike 0/1 knapsack, you are allowed to break the item here. 
The details of structure/class is defined in the comments above the given function.

Examples :

Input: values[] = [60, 100, 120], weights[] = [10, 20, 30], w = 50
Output: 240.000000
Explanation: Take the item with value 60 and weight 10, value 100 and weight 20 and split the third item with value 120 and weight 30, 
to fit it into weight 20. so it becomes (120/30)*20=80, so the total value becomes 60+100+80.0=240.0 
Thus, total maximum value of item we can have is 240.00 from the given capacity of sack. 

Input: values[] = [60, 100], weights[] = [10, 20], w = 50
Output: 160.000000
Explanation: Take both the items completely, without breaking. 
Total maximum value of item we can have is 160.00 from the given capacity of sack.

Input: val[] = [10, 20, 30], wt[] = [5, 10, 15], w = 100
Output: 60.000000
Explanation: In this case, the knapsack capacity exceeds the combined weight of all items (5 + 10 + 15 = 30). 
Therefore, we can take all items completely, yielding a total maximum value of 10 + 20 + 30 = 60.000000.
"""

class Solution:
    
    # Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, values, weights, w):
        # List to store (value, weight, value/weight ratio)
        items = [(values[i], weights[i], values[i] / weights[i]) for i in range(len(values))]
        
        # Sort items by value-to-weight ratio in descending order
        items.sort(key=lambda x: x[2], reverse=True)
        
        total_value = 0.0  # To store the total value of the knapsack
        remaining_capacity = w
        
        # Loop through the sorted items
        for value, weight, ratio in items:
            if remaining_capacity >= weight:
                # If the entire item can fit, take it
                total_value += value
                remaining_capacity -= weight
            else:
                # Take the fraction of the item that fits
                total_value += ratio * remaining_capacity
                break  # Knapsack is full
        
        # Return the total value rounded to 6 decimal places
        return round(total_value, 6)

# Example usage:
solution = Solution()
values1 = [60, 100, 120]
weights1 = [10, 20, 30]
w1 = 50
print(solution.fractionalknapsack(values1, weights1, w1))  # Output: 240.000000

values2 = [60, 100]
weights2 = [10, 20]
w2 = 50
print(solution.fractionalknapsack(values2, weights2, w2))  # Output: 160.000000


'''
Here's a line-by-line breakdown of the fractionalknapsack function:

class Solution:
Defines the Solution class, which contains the fractionalknapsack method.

def fractionalknapsack(self, values, weights, w):
Defines the function fractionalknapsack, which calculates the maximum value that can be obtained from a knapsack of capacity w 
with given values and weights.

items = [(values[i], weights[i], values[i] / weights[i]) for i in range(len(values))]:
Creates a list called items where each element is a tuple (value, weight, value/weight ratio) for each item. 
The ratio is used to maximize the value from the knapsack.

items.sort(key=lambda x: x[2], reverse=True):
Sorts the items list in descending order by the value-to-weight ratio (x[2]). 
This ensures that items with the highest value per unit weight are considered first, 
which is the key strategy for the fractional knapsack problem.

total_value = 0.0:
Initializes total_value to store the total value collected in the knapsack.

remaining_capacity = w:
Initializes remaining_capacity to track how much space is left in the knapsack.

for value, weight, ratio in items:
Starts a loop to iterate through the sorted items list. Each item consists of its value, weight, and value/weight ratio.

if remaining_capacity >= weight:
Checks if the entire item can fit into the remaining capacity of the knapsack.

total_value += value:
If the whole item fits, add its full value to total_value.

remaining_capacity -= weight:
Reduces the remaining_capacity by the weight of the item that was fully added.

else:
If the remaining capacity is less than the item's weight, only a fraction of the item can be added to the knapsack.

total_value += ratio * remaining_capacity:
Adds the value of the fractional part of the item that fits into the remaining capacity. 
The value added is equal to the value/weight ratio multiplied by the remaining capacity.

break:
After adding the fractional part of the item, the knapsack is full, so the loop terminates.

return round(total_value, 6):
Returns the total value collected in the knapsack, rounded to 6 decimal places for precision.

Example Usage:

values1 = [60, 100, 120]:
List of values for test case 1.

weights1 = [10, 20, 30]:
List of corresponding weights for test case 1.

w1 = 50:
Knapsack capacity for test case 1.

print(solution.fractionalknapsack(values1, weights1, w1)):
Calls the function fractionalknapsack and prints the result for test case 1, which outputs 240.000000.

values2 = [60, 100]:
List of values for test case 2.

weights2 = [10, 20]:
List of corresponding weights for test case 2.

w2 = 50:
Knapsack capacity for test case 2.

print(solution.fractionalknapsack(values2, weights2, w2)):
Calls the function fractionalknapsack and prints the result for test case 2, which outputs 160.000000.
'''