"""
Given a number N. Check if it is a Kaprekar number or not.
Note:- A Kaprekar number is a number whose square when divided into two parts the 
sum of those parts is equal to the original number and none of the parts has value 0. 
Now given a number, your task is to check if it is Kaprekar number or not.

Example 1:
Input: N=45
Output: 1
Explanation: 45*45=2025. Now, 20+25=45. Thus, 45 is a kaprekar number.

Example 2:
Input: N=20
Output: 0
Explanation: 20*20=400.There is no way to divide 400 into two parts such that their sum is equal to 20.So, 20 is not a kaprekar number.
"""

class Solution:
    def isKaprekar(self, N):
        # Square the number
        sqr = N * N
        sqr_str = str(sqr)
        
        # Get the number of digits in N
        num_digits = len(str(N))
        
        # Split the square into two parts
        left_part = sqr_str[:-num_digits] or "0"
        right_part = sqr_str[-num_digits:]

        # Sum the two parts
        total = int(left_part) + int(right_part)
        
        # Check if the sum is equal to N
        if total == N:
            return 1
        else:
            return 0

# Example usage:
solution = Solution()
print(solution.isKaprekar(45))  # Output: 1 (Kaprekar number)
print(solution.isKaprekar(20))  # Output: 0 (Not a Kaprekar number)

'''
Here's a line-by-line breakdown of the code:

class Solution:
This defines a class named Solution. The class will contain the method isKaprekar.

def isKaprekar(self, N):
This defines the method isKaprekar, which takes two parameters: 
self (referring to the class instance) and N (the number to check if it is a Kaprekar number).

sqr = N * N
This calculates the square of N and stores it in the variable sqr.

sqr_str = str(sqr)
This converts the square sqr into a string sqr_str to make it easier to split into parts.

num_digits = len(str(N))
This calculates the number of digits in the original number N by converting N to a string and finding its length. 
The number of digits is stored in num_digits.

left_part = sqr_str[:-num_digits] or "0"
This extracts the left part of the square by slicing the string sqr_str from the start up to the last num_digits. 
If there is no left part (when the slice is empty), it assigns "0" as the default.

right_part = sqr_str[-num_digits:]
This extracts the right part of the square by slicing the last num_digits characters from sqr_str.

total = int(left_part) + int(right_part)
This converts both left_part and right_part from strings to integers, then sums them to get total.

if total == N:
This checks if the sum of left_part and right_part (i.e., total) is equal to the original number N.

return 1
If the sum equals N, the method returns 1, indicating that N is a Kaprekar number.

else:
If the sum does not equal N, the else block is executed.

return 0
The method returns 0, indicating that N is not a Kaprekar number.

Example usage:
solution = Solution()
This creates an instance of the Solution class named solution.

print(solution.isKaprekar(45))
This calls the isKaprekar method on the number 45. The square of 45 is 2025, which splits into 20 and 25, and their sum equals 45. 
So, the output is 1, indicating that 45 is a Kaprekar number.

print(solution.isKaprekar(20))
This calls the method on 20. The square of 20 is 400, which splits into 4 and 00, and their sum equals 4, which is not equal to 20. 
Therefore, the output is 0, indicating that 20 is not a Kaprekar number.

Example Breakdown:
Let's say N = 45:
sqr = N * N = 2025
sqr_str = "2025" (string form of 2025)
num_digits = len(str(N)) = 2 (since N = 45 has 2 digits)
left_part = sqr_str[:-2] → "20" (this extracts everything except the last 2 characters)
right_part = sqr_str[-2:] → "25" (this extracts the last 2 characters)
So now, left_part = "20" and right_part = "25". The next steps would sum these two parts as integers (20 + 25 = 45),
which equals N, confirming that 45 is a Kaprekar number.
'''