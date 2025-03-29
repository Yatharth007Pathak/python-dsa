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
        return self.josephus_helper(n, k) + 1  # Convert from zero-based to one-based indexing

    def josephus_helper(self, n: int, k: int) -> int:
        # Base case: only one person left
        if n == 1:
            return 0
        # Recursive case: (position + k) % n gives the new position after eliminating a person
        return (self.josephus_helper(n - 1, k) + k) % n

# Example usage
sol = Solution()
print(sol.josephus(3, 2))  # Output: 3
print(sol.josephus(5, 3))  # Output: 4

'''
Explanation:

Recursive Approach: If there is only one person left (n == 1), the safe position is 0 (since we are using zero-based indexing).
Otherwise, the safe position can be determined by recursively finding the position for n-1 people and adding k to it, 
then taking modulo n to keep it within bounds. This approach ensures that after each elimination, we correctly adjust the position.

Base Case: When n is 1, the person at index 0 is the survivor.

Final Adjustment: Since the problem statement uses one-based indexing,
we add 1 to the result of the recursive calculation to get the correct position.


Recursive Josephus Solution:

class Solution:
Defines a class called Solution.

def josephus(self, n: int, k: int) -> int:
    return self.josephus_helper(n, k) + 1  # Convert from zero-based to one-based indexing
The josephus function is the main function to solve the problem.
It calls a helper function josephus_helper, which works with zero-based indexing. 
After getting the result, it adds 1 to convert it to one-based indexing.

def josephus_helper(self, n: int, k: int) -> int:
    if n == 1:
        return 0
    return (self.josephus_helper(n - 1, k) + k) % n
The helper function josephus_helper calculates the position of the last remaining person using recursion.
Base Case:
When n == 1, i.e., only one person remains, the position is 0 (in zero-based indexing).
Recursive Case:
For more than one person (n > 1), the next position is calculated using the formula (previous position + k) % n.
The function calls itself with n - 1, reducing the problem size by 1 until it reaches the base case.

sol = Solution()
print(sol.josephus(3, 2))  # Output: 3
print(sol.josephus(5, 3))  # Output: 4

josephus(3, 2):
We have n = 3 people standing in a circle, and we count every 2nd person.
The output is 3 (one-based index), which means the last remaining person is at position 3.

josephus(5, 3):
We have n = 5 people, and we count every 3rd person.
The output is 4 (one-based index), which means the last remaining person is at position 4.
'''