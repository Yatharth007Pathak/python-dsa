"""
You are given N pairs of numbers. In every pair, the first number is always smaller than the second number. 
A pair (c, d) can follow another pair (a, b) if b < c. Chain of pairs can be formed in this fashion. 
You have to find the longest chain which can be formed from the given set of pairs. 
 
Example 1:
Input: N = 5, P[] = {5  24 , 39 60 , 15 28 , 27 40 , 50 90}
Output: 3
Explanation: The given pairs are { {5, 24}, {39, 60}, {15, 28}, {27, 40}, {50, 90} }, 
the longest chain that can be formed is of length 3, and the chain is {{5, 24}, {27, 40}, {50, 90}}

Example 2:
Input: N = 2, P[] = {5 10 , 1 11}
Output: 1
Explanation: The max length chain possible is only of length one.
"""

class Pair:
    def __init__(self, a, b):
        self.a = a
        self.b = b

class Solution:
    def maxChainLen(self, Parr, n):
        # Sort pairs based on their second value (end value of the pair)
        Parr.sort(key=lambda x: x.b)

        # Initialize chain length and end of the last added pair
        max_length = 0
        end = float('-inf')
        
        # Iterate over the sorted pairs
        for pair in Parr:
            # If the start of the current pair is greater than the end of the last added pair
            if pair.a > end:
                # Increment the chain length
                max_length += 1
                # Update the end to the current pair's end
                end = pair.b

        return max_length

# Example usage:
pairs = [Pair(5, 24), Pair(39, 60), Pair(15, 28), Pair(27, 40), Pair(50, 90)]
solution = Solution()
print(solution.maxChainLen(pairs, len(pairs)))  # Output: 3

'''
Here's a line-by-line breakdown of the code:

class Pair:
Defines a class named Pair for creating a pair with two values.

def __init__(self, a, b):
Initializes the Pair class with a constructor method, taking two parameters, a and b, which represent the start and end values of the pair.

self.a = a
Sets the a attribute of the Pair instance to a, representing the start value.

self.b = b
Sets the b attribute of the Pair instance to b, representing the end value.

class Solution:
Defines a class named Solution that contains a method to find the maximum chain length of pairs.

def maxChainLen(self, Parr, n):
Defines a method maxChainLen within the Solution class. It takes in self (instance), Parr (a list of pairs), and n (the number of pairs).

Parr.sort(key=lambda x: x.b)
Sorts the list of pairs Parr based on the second value (b) of each pair in ascending order.

max_length = 0
Initializes max_length to zero, which will store the length of the longest chain of pairs.

end = float('-inf')
Sets end to negative infinity to keep track of the end value of the last added pair in the chain.

for pair in Parr:
Begins a loop to iterate over each pair in the sorted list Parr.

if pair.a > end:
Checks if the start of the current pair (pair.a) is greater than the end value of the last added pair in the chain.

max_length += 1
If the condition is met, increments max_length by 1, adding the current pair to the chain.

end = pair.b
Updates end to the current pair's end value, marking the end of the chain with the newly added pair.

return max_length
Returns max_length, which represents the length of the longest chain of pairs.

Example Usage:
pairs = [Pair(5, 24), Pair(39, 60), Pair(15, 28), Pair(27, 40), Pair(50, 90)]
Creates a list of Pair instances representing pairs with their start and end values.

solution = Solution()
Creates an instance of the Solution class named solution.

print(solution.maxChainLen(pairs, len(pairs))) # Output: 3
Calls maxChainLen on the list of pairs to find the longest chain length and prints the result. 
The expected output is 3, indicating the maximum chain length of pairs.
'''