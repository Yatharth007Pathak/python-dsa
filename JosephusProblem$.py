"""
A total of n people are standing in a circle, and you are one of them playing a game. 
Starting from a person, k persons will be counted in order along the circle, and the kth person will be killed. 
Then the next k persons will be counted along the circle, and again the kth person will be killed. 
This cycle will continue until only a single person is left in the circle.

If there are 5 people in the circle in the order A, B, C, D, and E, you will choose k=3. 
Starting from A, you will count A, B and C. C will be the 3rd person and will be killed. 
Then you will continue counting from D, E and then A. A will be third person and will be killed. 

You will be given an array where the first element is the first person from whom the counting will start 
and the subsequent order of the people. You want to be the last one standing. 
Determine the index at which you should stand to survive the game. Return an integer denoting safe position. 

Examples :

Input: n = 3, k = 2
Output: 3
Explanation: There are 3 persons so skipping 1 person i.e 1st person 2nd person will be killed. Thus the safe position is 3.

Input: n = 5, k = 3
Output: 4
Explanation: There are 5 persons so skipping 2 person i.e 3rd person will be killed. Thus the safe position is 4.
"""

class Solution:
    def josephus(self, n: int, k: int) -> int:
        safe_position = 0  # Start with zero-based indexing for one person

        # Compute the safe position for each number of people from 2 to n
        for i in range(2, n + 1):
            safe_position = (safe_position + k) % i

        # Convert from zero-based to one-based indexing
        return safe_position + 1

# Example usage
sol = Solution()
print(sol.josephus(3, 2))  # Output: 3
print(sol.josephus(5, 3))  # Output: 4

'''
Explanation:

Initialization: We start by setting safe_position to 0 (since with 1 person, the safe position is always 0).

Iterative Calculation: We iterate from 2 to n people, updating the safe_position for each value.
(safe_position + k) % i computes the new safe position after adding k and taking modulo i 
(to keep it within the bounds of the current number of people).

One-Based Conversion: Since the final answer should be one-based, we add 1 to safe_position.


Iterative Josephus Solution:

class Solution:
This defines a class called Solution.

def josephus(self, n: int, k: int) -> int:
    safe_position = 0  # Start with zero-based indexing for one person

    # Compute the safe position for each number of people from 2 to n
    for i in range(2, n + 1):
        safe_position = (safe_position + k) % i

    # Convert from zero-based to one-based indexing
    return safe_position + 1

Initialization: The variable safe_position is initialized to 0, 
representing the last person standing when there is only one person left (using zero-based indexing).
Iteration:The for loop iterates over the number of people, starting from 2 up to n. 
This allows us to compute the safe position as the number of participants increases. The formula used is (safe_position + k) % i. 
It recalculates the safe position at each step by adding the step size k and then taking the remainder when divided 
by the current number of participants (i). This is equivalent to eliminating every k-th person in the sequence.
Index Conversion: The function returns safe_position + 1 to convert the result from zero-based to one-based indexing.

sol = Solution()
print(sol.josephus(3, 2))  # Output: 3
print(sol.josephus(5, 3))  # Output: 4

josephus(3, 2):
With n = 3 and k = 2, the output is 3. This means that the last remaining person is at position 3 (in one-based indexing).

josephus(5, 3):
With n = 5 and k = 3, the output is 4. This means that the last remaining person is at position 4 (in one-based indexing).
'''