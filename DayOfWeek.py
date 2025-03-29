"""
Write a program that calculates the day of the week for any particular date in the past or future. Solve using Zeller's Congruence.

Example 1:
Input: d = 28, m = 12, y = 1995
Output: Thursday
Explanation: 28 December 1995 was a Thursday.

Example 2:
Input: d = 30, m = 8, y = 2010
Output: Monday
Explanation: 30 August 2010 was a Monday.
"""

class Solution:
    def getDayOfWeek(self, d, m, y):
        # If month is January or February, treat them as 13th and 14th month of previous year
        if m == 1:
            m = 13
            y -= 1
        elif m == 2:
            m = 14
            y -= 1
        
        # Zeller's Congruence formula
        q = d
        k = y % 100
        j = y // 100
        f = q + ((13 * (m + 1)) // 5) + k + (k // 4) + (j // 4) - 2 * j
        
        # Day of the week (0 = Saturday, 1 = Sunday, ..., 6 = Friday)
        day_of_week = f % 7
        
        # Mapping the result of Zeller's Congruence to day names
        days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        
        return days[day_of_week]

# Example usage
sol = Solution()
print(sol.getDayOfWeek(28, 12, 1995))  # Output: Thursday
print(sol.getDayOfWeek(30, 8, 2010))   # Output: Monday


'''
This code uses Zeller's Congruence, an algorithm for calculating the day of the week for any given date. 
It adjusts for January and February by treating them as the 13th and 14th months of the previous year. 
The formula then provides the day of the week, which is mapped to the corresponding day name.


Here's a breakdown of the code that calculates the day of the week using Zeller's Congruence algorithm:

class Solution:
Defines the Solution class which contains the method getDayOfWeek.

def getDayOfWeek(self, d, m, y):
Defines the method getDayOfWeek, which takes three parameters: d (day), m (month), and y (year). 
This method returns the day of the week for the given date.

if m == 1: and elif m == 2:
Zeller's Congruence requires January and February to be treated as the 13th and 14th months of the previous year, respectively.
If the month is January (m == 1), it is set to 13, and the year is decremented (y -= 1).
Similarly, if the month is February (m == 2), it is treated as the 14th month of the previous year.

q = d
The variable q represents the day of the month.

k = y % 100
k is the last two digits of the year (the "year of the century").

j = y // 100
j is the century part of the year.

Zeller's Congruence formula:
The formula calculates an integer f that helps determine the day of the week:
f = q + ((13 * (m + 1)) // 5) + k + (k // 4) + (j // 4) - 2 * j
This is the core of Zeller's Congruence. It computes a number that helps us find the day of the week.

day_of_week = f % 7
The remainder when f is divided by 7 (f % 7) gives a number between 0 and 6, which corresponds to the day of the week. The day is mapped as:
0 = Saturday
1 = Sunday
2 = Monday
3 = Tuesday
4 = Wednesday
5 = Thursday
6 = Friday

days = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
This list contains the names of the days of the week in the order mapped by Zeller's Congruence.

return days[day_of_week]
Returns the day of the week corresponding to the computed day_of_week.

sol = Solution()
Creates an instance of the Solution class.

print(sol.getDayOfWeek(28, 12, 1995)) # Output: Thursday
Calls the getDayOfWeek method with the date 28th December 1995. The output is Thursday.

print(sol.getDayOfWeek(30, 8, 2010)) # Output: Monday
Calls the getDayOfWeek method with the date 30th August 2010. The output is Monday.
'''