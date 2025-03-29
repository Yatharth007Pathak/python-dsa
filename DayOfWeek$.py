"""
Write a program that calculates the day of the week for any particular date in the past or future.

Example 1:
Input: d = 28, m = 12, y = 1995
Output: Thursday
Explanation: 28 December 1995 was a Thursday.

Example 2:
Input: d = 30, m = 8, y = 2010
Output: Monday
Explanation: 30 August 2010 was a Monday.
"""

from datetime import datetime

class Solution:
    def getDayOfWeek(self, d: int, m: int, y: int) -> str:
        # Create a datetime object
        date = datetime(y, m, d)
        # Return the day of the week
        return date.strftime("%A")

# Example usage
sol = Solution()
print(sol.getDayOfWeek(28, 12, 1995))  # Output: Thursday
print(sol.getDayOfWeek(30, 8, 2010))   # Output: Monday


'''
To calculate the day of the week for any given date, we can use Zeller's Congruence or Python's built-in datetime module. 
Zeller's Congruence is a well-known algorithm for finding the day of the week for any date in the past or future.

However, Python's datetime module is simpler and more accurate since it's built-in and takes care of leap years and other calendar specifics.


Code Breakdown

from datetime import datetime
This imports the datetime class from Python's datetime module, which provides functions to work with dates and times.

class Solution:
Defines a class Solution that encapsulates the method getDayOfWeek.

def getDayOfWeek(self, d: int, m: int, y: int) -> str:
This defines the method getDayOfWeek, which takes three arguments:
d: an integer representing the day.
m: an integer representing the month.
y: an integer representing the year.
The method returns a string that indicates the day of the week for the provided date.

date = datetime(y, m, d)
This creates datetime object using the provided year (y), month (m), and day (d). The datetime object automatically calculates the correct date.

return date.strftime("%A")
This line converts the datetime object into a formatted string that represents the day of the week.
strftime("%A") formats the date to return the full name of the day of the week (e.g., "Monday", "Tuesday").

sol = Solution()
Creates an instance of the Solution class.

print(sol.getDayOfWeek(28, 12, 1995)) # Output: Thursday
Calls the getDayOfWeek method with the date 28th December 1995. The expected output is Thursday.

print(sol.getDayOfWeek(30, 8, 2010)) # Output: Monday
Calls the getDayOfWeek method with the date 30th August 2010. The expected output is Monday.
'''