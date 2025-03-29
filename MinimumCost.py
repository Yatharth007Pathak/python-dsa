"""
Given an array arr containing the lengths of the different ropes, we need to connect these ropes to form one rope. 
The cost to connect two ropes is equal to sum of their lengths. The task is to connect the ropes with minimum cost.  

Examples:

Input: arr[] = [4, 3, 2, 6]
Output: 29
Explanation: We can connect the ropes in following ways.
1) First connect ropes of lengths 2 and 3. Which makes the array [4, 5, 6]. Cost of this operation 2 + 3 = 5. 
2) Now connect ropes of lengths 4 and 5. Which makes the array [9, 6]. Cost of this operation 4 + 5 = 9.
3) Finally connect the two ropes and all ropes have connected. Cost of this operation 9 + 6 =15
Total cost for connecting all ropes is 5 + 9 + 15 = 29. This is the optimized cost for connecting ropes. 
Other ways of connecting ropes would always have same or more cost. 
For example, if we connect 4 and 6 first (we get three rope of 3, 2 and 10), 
then connect 10 and 3 (we gettwo rope of 13 and 2). Finally we connect 13 and 2. Total cost in this way is 10 + 13 + 15 = 38.

Input: arr[] = [4, 2, 7, 6, 9]
Output: 62 
Explanation: First, connect ropes 4 and 2, which makes the array [6, 7, 6, 9]. Cost of this operation 4 + 2 = 6. 
Next, add ropes 6 and 6, which results in [12, 7, 9]. Cost of this operation 6 + 6 = 12.
Then, add 7 and 9, which makes the array [12,16]. Cost of this operation 7 + 9 = 16. And
finally, add these two which gives [28]. Hence, the total cost is 6 + 12 + 16 + 28 = 62.
"""

import heapq
from typing import List

class Solution:
    def minCost(self, arr: List[int]) -> int:
        # Create a min heap from the given array
        heapq.heapify(arr)
        
        total_cost = 0

        # Keep combining ropes until we have only one rope left
        while len(arr) > 1:
            # Extract two smallest ropes
            first = heapq.heappop(arr)
            second = heapq.heappop(arr)
            
            # Calculate the cost of combining these two ropes
            cost = first + second
            total_cost += cost

            # Add the combined rope back into the heap
            heapq.heappush(arr, cost)

        return total_cost

# Example usage
sol = Solution()
print(sol.minCost([4, 3, 2, 6]))  # Output: 29
print(sol.minCost([4, 2, 7, 6, 9]))  # Output: 62

'''
Let's break down this code step by step:


import heapq:
Imports the heapq module, which provides an implementation of the min-heap (priority queue) data structure.

from typing import List:
Imports the List type from the typing module to specify the type of input parameters.

class Solution::
Defines a class named Solution to encapsulate the solution method.

def minCost(self, arr: List[int]) -> int::
Defines a method minCost that takes a list of integers (arr) as input and returns an integer (int) representing the minimum cost.

heapq.heapify(arr):
Converts the list arr into a min-heap. In a min-heap, the smallest element is always at the root (index 0).

total_cost = 0:
Initializes a variable total_cost to keep track of the cumulative cost of combining the ropes.

while len(arr) > 1::
Starts a loop that continues until only one rope is left in the heap.

first = heapq.heappop(arr):
Removes and returns the smallest element from the heap (first rope).

second = heapq.heappop(arr):
Removes and returns the next smallest element from the heap (second rope).

cost = first + second:
Calculates the cost of combining these two ropes (first + second).

total_cost += cost:
Adds the current cost to total_cost.

heapq.heappush(arr, cost):
Adds the newly combined rope (of length cost) back into the heap.

return total_cost:
Returns the accumulated total_cost after combining all ropes into one.

sol = Solution():
Creates an instance of the Solution class.

print(sol.minCost([4, 3, 2, 6])):
Calls the minCost method with the list [4, 3, 2, 6] and prints the result (Output: 29).

print(sol.minCost([4, 2, 7, 6, 9])):
Calls the minCost method with the list [4, 2, 7, 6, 9] and prints the result (Output: 62).
'''