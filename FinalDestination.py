"""
Consider a 2d plane and a Robot which is located at (0,0) who can move only one unit step at a time in any direction i.e. 
if its initial position is (x,y), he can go to positions (x+1,y), (x-1,y), (x,y+1) or (x,y-1). 
Now Given three integers a,b (denoting the final position where the robot has to reach), and x. 
Find out if the Robot can reach the final position in exactly x steps.

Example 1:
Input: a = 5, b = 5, x = 11
Output: 0
Explanation: No matter how the Robot moves, the Robot won't be able to reach point (5,5) in exactly 11 moves.

Example 2:
Input: a = 10, b = 15, x = 25
Output: 1
Explanation: The Robot can move 10 times towards positive x-axis and then 15 times towards positive y-axis to reach (10,15).
"""

class Solution:
    def canReach(self, a, b, x):
        # Calculate the minimum number of steps needed to reach (a, b)
        min_steps = abs(a) + abs(b)

        # Check if the robot can reach the point (a, b) in exactly x steps
        # 1. The robot cannot reach if the minimum steps exceed x
        # 2. The difference between x and min_steps should be an even number (to balance extra steps)
        if min_steps > x:
            return 0
        elif (x - min_steps) % 2 == 0:
            return 1
        else:
            return 0

# Example usage:
solution = Solution()
print(solution.canReach(5, 5, 11))  # Output: 0
print(solution.canReach(10, 15, 25))  # Output: 1

'''
In this code, the goal is to determine whether a robot starting at the origin (0, 0) can reach the point (a,b) in exactly x steps. 
Here's how the logic works:

Key Concepts:

Minimum Steps Calculation:
The robot needs to take at least |a| + |b| steps to reach the point (a,b), which is referred to as min_steps. 
This is because the robot needs to move horizontally |a| units and vertically |b| units.

Conditions to Reach in Exactly x Steps:
Condition 1: The robot cannot reach (a,b) if the minimum number of steps (min_steps) exceeds x. 
If min_steps>x, it returns 0, meaning it is impossible.
Condition 2: If the difference between x and min_steps is even, the robot can take extra steps to exactly match x steps. 
This is because the robot can move back and forth to balance any extra steps 
(e.g., take 2 steps in one direction and return to the same position). Therefore, if (x - min_steps)%2==0, it returns 1, meaning it is possible.

Why Even Steps Matter:
The robot can "waste" steps by moving back and forth in place. However, these wasted steps must come in pairs 
(2 steps: 1 forward and 1 backward), which is why the difference between x and min_steps must be even.

Example Walkthrough:

Example 1: canReach(5, 5, 11)
The robot needs at least |5| + |5| = 10 steps to reach (5,5).
x=11, so the robot has 1 extra step.
Since 1 is odd, the robot cannot take exactly 11 steps and return to (5,5) after reaching it. Therefore, the output is 0.

Example 2: canReach(10, 15, 25)
The robot needs at least |10| + |15| = 25 steps to reach (10,15).
x=25, so there are exactly enough steps to reach (10,15), and no extra steps are needed.
Since there is no extra step to "waste," the robot can reach (10,15) in exactly 25 steps. Therefore, the output is 1.

Code Summary:
Input: Two integers a and b representing the target coordinates, and x representing the exact number of steps allowed.
Output: 1 if it's possible to reach (a,b) in exactly x steps, otherwise 0.
'''