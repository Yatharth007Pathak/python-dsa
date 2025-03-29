"""
Calculate the angle between the hour hand and minute hand.

Note: There can be two angles between hands; we need to print a minimum of two. 
Also, we need to print the floor of the final result angle. For example, if the final angle is 10.61, we need to print 10.

Example 1:
Input: H = 9 , M = 0
Output: 90
Explanation: The minimum angle between hour and minute hand when the time is 9 is 90 degress.
"""

class Solution:
    def getAngle(self, H, M):
        # Calculate the positions of hour and minute hands
        minute_angle = 6 * M
        hour_angle = 30 * H + 0.5 * M
        
        # Calculate the absolute difference between the two angles
        diff = abs(hour_angle - minute_angle)
        
        # There are two possible angles: `diff` and `360 - diff`
        return min(int(diff), int(360 - diff))

# Example usage
sol = Solution()

# Test case 1
H1, M1 = 9, 0
print(sol.getAngle(H1, M1))  # Output: 90

# Test case 2
H2, M2 = 3, 30
print(sol.getAngle(H2, M2))  # Output: 75

# Test case 3
H3, M3 = 12, 45
print(sol.getAngle(H3, M3))  # Output: 112


'''
Key points:
Minute hand movement: The minute hand moves 6 degrees per minute (360 degrees in 60 minutes).
Hour hand movement: The hour hand moves 0.5 degrees per minute (30 degrees per hour, which is 30/60 degrees per minute).
We need to compute both possible angles (clockwise and counterclockwise) between the two hands and return the minimum.

Formula:
The minute hand moves at 6 * M degrees.
The hour hand moves at 30 * H + 0.5 * M degrees.
The absolute difference between the two gives the angle.
The other possible angle is 360 - this_angle.

Code Breakdown:
class Solution:
This defines the class Solution. The method getAngle will be defined inside this class.

def getAngle(self, H, M):
This defines the method getAngle that takes two parameters:

H: the hour on the clock (from 1 to 12).
M: the minute on the clock (from 0 to 59).
self refers to the instance of the class.
minute_angle = 6 * M
The minute hand moves 6 degrees per minute because a full circle (360 degrees) is divided into 60 minutes.

For example, at M = 30, the minute hand would be at 30 * 6 = 180 degrees.
hour_angle = 30 * H + 0.5 * M
The hour hand moves 30 degrees per hour (360 degrees / 12 hours = 30 degrees per hour). In addition to the base movement, 
the hour hand also moves 0.5 degrees per minute as time progresses (since 30 degrees per hour divided by 60 minutes = 0.5 degrees per minute).

For example, at H = 3 and M = 30, the hour hand would be at 3 * 30 + 0.5 * 30 = 90 + 15 = 105 degrees.
diff = abs(hour_angle - minute_angle)
This calculates the absolute difference between the positions of the hour and minute hands.

This difference gives one possible angle between the two hands.
return min(int(diff), int(360 - diff))
There are two possible angles between the hour and minute hands:

The direct difference diff.
The angle in the opposite direction, which is 360 - diff.
The function returns the smaller of the two angles.
Example Usage:
Test case 1: H1, M1 = 9, 0

The hour hand is at 9 * 30 + 0.5 * 0 = 270 degrees.
The minute hand is at 6 * 0 = 0 degrees.
The absolute difference is |270 - 0| = 270.
The smaller angle is min(270, 360 - 270) = 90.
Output: 90.
Test case 2: H2, M2 = 3, 30

The hour hand is at 3 * 30 + 0.5 * 30 = 105 degrees.
The minute hand is at 6 * 30 = 180 degrees.
The absolute difference is |105 - 180| = 75.
Output: 75.
Test case 3: H3, M3 = 12, 45

The hour hand is at 12 * 30 + 0.5 * 45 = 360 + 22.5 = 22.5 degrees (since 360 degrees is equivalent to 0 for the hour hand).
The minute hand is at 6 * 45 = 270 degrees.
The absolute difference is |22.5 - 270| = 247.5.
The smaller angle is min(247.5, 360 - 247.5) = 112.
Output: 112.
'''