"""
There is an array arr of heights of stone and Geek is standing at the first stone and can jump to one of the following: 
Stone i+1, i+2, ... i+k stone, where k is the maximum number of steps that can be jumped and cost will be |hi-hj| is incurred, 
where j is the stone to land on. Find the minimum possible total cost incurred before the Geek reaches the last stone.

Example:

Input: k = 3, arr[]= [10, 30, 40, 50, 20]
Output: 30
Explanation: Geek will follow the path 1->2->5, the total cost would be | 10-30| + |30-20| = 30, which is minimum

Input: k = 1, arr[]= [10, 20, 10]
Output: 20
Explanation: Geek will follow the path 1->2->3, the total cost would be |10 - 20| + |20 - 10| = 20.
"""

class Solution:
    def minimizeCost(self, k, arr):
        n = len(arr)
        dp = [float('inf')] * n
        dp[0] = 0

        for i in range(1, n):
            for j in range(1, min(k, i) + 1):
                dp[i] = min(dp[i], dp[i - j] + abs(arr[i] - arr[i - j]))

        return dp[-1]

# Example usage
sol = Solution()
print(sol.minimizeCost(3, [10, 30, 40, 50, 20]))  # Output: 30
print(sol.minimizeCost(1, [10, 20, 10]))          # Output: 20

'''
This problem is a variant of the "Frog Jump" problem, where we want to find the minimum cost for reaching the last stone 
while allowing jumps of up to k stones. Dynamic programming can be used to solve this problem efficiently.


dp stands for Dynamic Programming, which is a method used in algorithmic problem-solving 
to solve problems with overlapping subproblems and optimal substructure.

Key Concepts of Dynamic Programming:
Overlapping Subproblems: The problem can be broken down into smaller subproblems, which are solved independently. 
In many cases, the same subproblems are solved multiple times.
Optimal Substructure: The optimal solution of the problem can be obtained by using the optimal solutions of its subproblems.

How Dynamic Programming Works:
Instead of solving the same subproblems repeatedly, dynamic programming stores the results of those subproblems (usually in an array or table), 
allowing them to be reused later. This helps reduce the time complexity of the solution.
The technique typically involves building a table (or array) to store the solution for subproblems in a bottom-up or top-down manner.


Let's break down the code step by step:

A class Solution is defined.

Inside the class, a method minimizeCost is defined, which takes three parameters: 
self (to refer to the class instance), k (maximum number of steps that can be taken), and arr (a list of integers representing costs).

The length of the array arr is calculated and stored in the variable n.

A list dp of length n is created and initialized with float('inf') (representing infinity), except for dp[0], which is set to 0. 
This list will be used to store the minimum cost to reach each position.

A loop starts from i = 1 to n - 1, iterating through each element in the array.

Inside the outer loop, another loop starts from j = 1 to min(k, i), 
representing the possible steps that can be taken from the previous positions to reach the current position i.

For each i and j, the value of dp[i] is updated to the minimum of its current value and the sum of dp[i - j]
and the absolute difference between arr[i] and arr[i - j]. 
This step calculates the minimum cost to reach position i by considering each possible step from i - j to i.

Finally, the function returns dp[-1], which represents the minimum cost to reach the last position of the array.

In the example usage:
sol.minimizeCost(3, [10, 30, 40, 50, 20]) returns 30. Here, the function computes the minimum cost to reach the last position, 
considering up to 3 steps at a time.
sol.minimizeCost(1, [10, 20, 10]) returns 20. Since k is 1, the function only allows moving to the next element, 
calculating the minimum cost accordingly.
'''