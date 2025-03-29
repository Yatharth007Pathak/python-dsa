"""
Given a number n. Count the number of digits in n which evenly divide n. Return an integer, total number of digits of n which divides n evenly.
Note :- Evenly divides means whether n is divisible by a digit i.e. leaves a remainder 0 when divided.
 
Examples :

Input: n = 12
Output: 2
Explanation: 1, 2 when both divide 12 leaves remainder 0.

Input: n = 2446
Output: 1
Explanation: Here among 2, 4, 6 only 2 divides 2446 evenly while 4 and 6 do not.

Input: n = 23
Output: 0
Explanation: 2 and 3, none of them divide 23 evenly.
"""

class Solution:
    def evenlyDivides(self, N):
        count = 0
        original = N
        
        while N > 0:
            digit = N % 10
            if digit != 0 and original % digit == 0:
                count += 1
            N //= 10
        
        return count

# Example usage:
solution = Solution()
print(solution.evenlyDivides(12))    # Output: 2
print(solution.evenlyDivides(2446))  # Output: 1
print(solution.evenlyDivides(23))    # Output: 0

'''
Here's a pointwise breakdown for each line of the code:

class Solution:
Defines a class named Solution.

def evenlyDivides(self, N):
Defines a method called evenlyDivides that takes self (reference to the object) and N (an integer) as parameters.

count = 0
Initializes a variable count to 0, which will be used to count the number of digits of N that evenly divide N.

original = N
Stores the original value of N in a variable called original to use later for calculations.

while N > 0:
Starts a while loop that runs as long as N is greater than 0.

digit = N % 10
Extracts the last digit of N by taking N modulo 10.

if digit != 0 and original % digit == 0:
Checks if the digit is not 0 and if original is divisible by digit without a remainder.

count += 1
If the condition in the previous line is true, increments the count by 1.

N //= 10
Removes the last digit from N by performing an integer division by 10.

return count
Returns the value of count, which represents the number of digits that evenly divide N.

solution = Solution()
Creates an instance of the Solution class.

print(solution.evenlyDivides(12))
Calls the evenlyDivides method with 12 as input and prints the result (2).

print(solution.evenlyDivides(2446))
Calls the evenlyDivides method with 2446 as input and prints the result (1).

print(solution.evenlyDivides(23))
Calls the evenlyDivides method with 23 as input and prints the result (0).
'''