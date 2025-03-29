"""
You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array 
of arr[], where arr[i]  is the type of fruit the ith tree produces.
You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow :

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. 
The picked fruits must fit in one of the baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array of fruits, return the maximum number of fruits you can pick.

Examples:

Input: arr[]= [2, 1, 2]
Output: 3
Explanation: We can pick one fruit from all three trees. Please note that the type of fruits is same in the 1st and 3rd baskets.

Input: arr[] = [3, 1, 2, 2, 2, 2]
Output: 5
Explanation: It's optimal to pick from the last 5 trees. Please note that we do not pick the first basket 
as we would have to stop at thrid tree which would result in only 2 fruits collected.
"""

from collections import defaultdict

class Solution:
    def totalFruits(self, arr):
        # Dictionary to store the count of each fruit type in the window
        fruit_count = defaultdict(int)
        left = 0  # Left pointer of the window
        max_fruits = 0  # Maximum fruits that can be collected

        for right in range(len(arr)):
            # Add the current fruit to the window
            fruit_count[arr[right]] += 1

            # If we have more than 2 types of fruits, shrink the window
            while len(fruit_count) > 2:
                fruit_count[arr[left]] -= 1
                if fruit_count[arr[left]] == 0:
                    del fruit_count[arr[left]]
                left += 1

            # Update the maximum size of the window
            max_fruits = max(max_fruits, right - left + 1)

        return max_fruits

# Example usage
solution = Solution()
print(solution.totalFruits([2, 1, 2]))  # Output: 3
print(solution.totalFruits([3, 1, 2, 2, 2, 2]))  # Output: 5

'''
Explanation of the Code
This code solves the "Fruit into Baskets" problem using a sliding window technique.

class Solution:
Defines a class Solution that contains the method totalFruits.

def totalFruits(self, arr):
A method to find the maximum number of fruits that can be collected from two types of fruits in the array arr.

fruit_count = defaultdict(int)
A dictionary to keep track of the count of each fruit type in the current window.
Uses defaultdict for automatic initialization of keys to 0.

left = 0
Initializes the left pointer of the sliding window.

max_fruits = 0
Stores the maximum number of fruits that can be collected.

for right in range(len(arr)):
Iterates through the array using the right pointer.

fruit_count[arr[right]] += 1
Adds the current fruit type to the dictionary and increments its count.

while len(fruit_count) > 2:
If the number of unique fruit types in the current window exceeds 2, the window is shrunk.

fruit_count[arr[left]] -= 1
Reduces the count of the fruit type at the left pointer.

if fruit_count[arr[left]] == 0:
If the count of a fruit type becomes 0, it is removed from the dictionary.

left += 1
Moves the left pointer one step to the right to shrink the window.

max_fruits = max(max_fruits, right - left + 1)
Calculates the size of the current valid window (right - left + 1) and updates the maximum.

return max_fruits
Returns the maximum number of fruits that can be collected.

Input: [2, 1, 2]
Step-by-step:
Add 2 → fruit_count = {2: 1}. Window: [2].
Add 1 → fruit_count = {2: 1, 1: 1}. Window: [2, 1].
Add 2 → fruit_count = {2: 2, 1: 1}. Window: [2, 1, 2].
Maximum fruits: 3.
Output: 3.

Input: [3, 1, 2, 2, 2, 2]
Step-by-step:
Add 3 → fruit_count = {3: 1}. Window: [3].
Add 1 → fruit_count = {3: 1, 1: 1}. Window: [3, 1].
Add 2 → fruit_count = {3: 1, 1: 1, 2: 1}. Too many types. Shrink: [1, 2].
Add 2 → fruit_count = {1: 1, 2: 2}. Window: [1, 2, 2].
Add 2 → fruit_count = {1: 1, 2: 3}. Window: [1, 2, 2, 2].
Add 2 → fruit_count = {1: 1, 2: 4}. Window: [1, 2, 2, 2, 2].
Maximum fruits: 5.
Output: 5.
'''