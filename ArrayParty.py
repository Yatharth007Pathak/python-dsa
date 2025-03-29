"""
A professor attended a party and classified it into two categories based on the colors of the robes. 
If all party members are wearing different colored robes, represented by positive integers in the array arr[], 
then it is a girl's only party. If there is at least one duplicate color, it is a boy's party. 
Determine the type of party by returning “true” if it's a boy's party, otherwise, return “false”.

Examples:

Input: arr[] = [1, 2, 3, 4, 7]
Output: false
Explanation: All the colors are unique so it's a GIRLS party.

Input: arr[] = [1, 3, 2, 4, 5, 1]
Output: true
Explanation: There are two colors 1. So it's a BOYS party.
"""

class Solution:
    def PartyType(self, arr):
        # Use a set to store unique colors
        unique_colors = set()
        
        # Iterate through the array to check for duplicates
        for color in arr:
            if color in unique_colors:
                return "true"  # Boy's party (duplicate found)
            unique_colors.add(color)
        
        return "false"  # Girl's party (all colors are unique)

# Example usage
sol = Solution()
print(sol.PartyType([1, 2, 3, 4, 7]))  # Output: false
print(sol.PartyType([1, 3, 2, 4, 5, 1]))  # Output: true


'''
Here's a detailed, pointwise breakdown of the given code:

Class Definition: The code starts by defining a class named Solution.

Function Definition (PartyType):
Inside the Solution class, a method named PartyType is defined, which takes one parameter: 
arr (a list representing the colors of items brought to the party).

Initialize Set for Unique Colors:
A set named unique_colors is created to store unique color values. 
Since sets in Python do not allow duplicates, they are ideal for tracking which colors have already been seen.

Iterate Through arr:
A for loop is used to iterate over each element (color) in the list arr.

Check for Duplicates:
Within the loop, if the current color is already in unique_colors, 
it means a duplicate has been found. The method returns "true", indicating it's a "Boy's party" (duplicates found).
If the color is not in the set, it is added to unique_colors.

Return Result:
If the loop completes without finding any duplicates, the method returns "false", indicating it's a "Girl's party" (all colors are unique).

Example Usage:
An instance of the Solution class is created and stored in the variable sol.

Example 1: The PartyType method is called with the list [1, 2, 3, 4, 7]. 
The output is "false", meaning it's a "Girl's party" since all colors are unique.

Example 2: The PartyType method is called with the list [1, 3, 2, 4, 5, 1]. 
The output is "true", indicating it's a "Boy's party" because there is a duplicate color (1).
Summary
'''