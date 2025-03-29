"""
You are given a string str in the form of an IPv4 Address. 
Your task is to validate an IPv4 Address, if it is valid return true otherwise return false.

IPv4 addresses are canonically represented in dot-decimal notation, which consists of four decimal numbers, 
each ranging from 0 to 255, separated by dots, e.g., 172.16.254.1

A valid IPv4 Address is of the form x1.x2.x3.x4 where 0 <= (x1, x2, x3, x4) <= 255. 
Thus, we can write the generalized form of an IPv4 address as (0-255).(0-255).(0-255).(0-255)

Note: Here we are considering numbers only from 0 to 255 and any additional leading zeroes will be considered invalid.

Examples :

Input: str = 222.111.111.111
Output: true
Explanation: Here, the IPv4 address is as per the criteria mentioned and also all four decimal numbers lies in the mentioned range.

Input: str = 5555..555
Output: false
Explanation: 5555..555 is not a valid. IPv4 address, as the middle two portions are missing.

To validate an IPv4 address, we need to check the following conditions:
The string should consist of exactly four decimal numbers separated by dots.
Each decimal number should be in the range 0 to 255.
Each decimal number should not have leading zeroes, except for "0" itself.
The string must not contain any extra characters, such as spaces or extra dots.
"""

class Solution:
    def isValid(self, ip_str):
        # Split the string by dots
        parts = ip_str.split('.')
        
        # There should be exactly 4 parts
        if len(parts) != 4:
            return False
        
        # Check each part
        for part in parts:
            # Check if the part is a number
            if not part.isdigit():
                return False
            
            # Convert the part to an integer
            num = int(part)
            
            # Check if the number is in the range [0, 255]
            if num < 0 or num > 255:
                return False
            
            # Check for leading zeros
            if part != str(num):
                return False
        
        return True

# Example usage:
solution = Solution()

# Test cases
print(solution.isValid("222.111.111.111"))  # Output: True
print(solution.isValid("5555..555"))        # Output: False
print(solution.isValid("0.0.0.0"))          # Output: True
print(solution.isValid("172.16.254.1"))     # Output: True
print(solution.isValid("256.256.256.256"))  # Output: False

'''
Here's a breakdown of the code, line by line:

class Solution:
A class named Solution is defined to hold the method that checks the validity of an IP address.

def isValid(self, ip_str):
Defines a method isValid inside the Solution class.
It takes two arguments: self (instance of the class) and ip_str (the string representing the IP address to validate).

parts = ip_str.split('.')
Splits the input string ip_str by the dot . character and stores the resulting parts in a list called parts.

if len(parts) != 4:
Checks if the resulting list parts contains exactly 4 elements (since a valid IPv4 address should have 4 parts).
If not, it returns False, indicating an invalid IP address.

for part in parts:
Loops through each part of the parts list.

if not part.isdigit():
Checks if the current part is composed entirely of digits. If not, it returns False.

num = int(part)
Converts the string part to an integer num.

if num < 0 or num > 255:
Checks if the integer num is within the valid range of [0, 255] (the range for each part of an IPv4 address).
If num is out of this range, it returns False.

if part != str(num):
Converts the integer num back to a string and checks if it matches the original part. This ensures there are no leading zeros. 
For example, '01' should not be considered valid because converting it to an integer results in 1, not '01'.
If there's a mismatch, it returns False.

return True
If all parts pass the checks, the method returns True, indicating a valid IP address.

solution = Solution()
Creates an instance of the Solution class.

print(solution.isValid("222.111.111.111"))
Calls the isValid method with the IP "222.111.111.111" and prints the result. This IP is valid, so the output is True.

print(solution.isValid("5555..555"))
Calls the isValid method with the IP "5555..555". This IP has fewer than 4 parts, so the output is False.

print(solution.isValid("0.0.0.0"))
Calls the isValid method with the IP "0.0.0.0". This is a valid IP, so the output is True.

print(solution.isValid("172.16.254.1"))
Calls the isValid method with the IP "172.16.254.1". This is a valid IP, so the output is True.

print(solution.isValid("256.256.256.256"))
Calls the isValid method with the IP "256.256.256.256". Since each part exceeds the range [0, 255], the output is False.


Let's break down the output for the example solution.isValid("172.16.254.1") step by step.

The input string is "172.16.254.1".

Execution Steps:
Calling the Method: The method isValid is called with ip_str set to "172.16.254.1".

Splitting the String: parts = ip_str.split('.'): This splits the string by the dot (.) character.
The result is: parts = ['172', '16', '254', '1'].

Checking Number of Parts: if len(parts) != 4:: Checks if the number of parts is exactly 4.
Since len(parts) is 4, this check passes.

Validating Each Part: The method enters a loop to validate each part in parts.

Iteration 1 (part = '172'):
if not part.isdigit():: Checks if '172' is all digits. This is True.
num = int(part): Converts '172' to integer 172.
if num < 0 or num > 255:: Checks if 172 is in the range [0, 255]. This is True.
if part != str(num):: Checks for leading zeros. '172' is equal to str(172), so this check passes.

Iteration 2 (part = '16'):
if not part.isdigit():: Checks if '16' is all digits. This is True.
num = int(part): Converts '16' to integer 16.
if num < 0 or num > 255:: Checks if 16 is in the range [0, 255]. This is True.
if part != str(num):: Checks for leading zeros. '16' is equal to str(16), so this check passes.

Iteration 3 (part = '254'):
if not part.isdigit():: Checks if '254' is all digits. This is True.
num = int(part): Converts '254' to integer 254.
if num < 0 or num > 255:: Checks if 254 is in the range [0, 255]. This is True.
if part != str(num):: Checks for leading zeros. '254' is equal to str(254), so this check passes.

Iteration 4 (part = '1'):
if not part.isdigit():: Checks if '1' is all digits. This is True.
num = int(part): Converts '1' to integer 1.
if num < 0 or num > 255:: Checks if 1 is in the range [0, 255]. This is True.
if part != str(num):: Checks for leading zeros. '1' is equal to str(1), so this check passes.

All Checks Passed:
Since all parts passed the checks, the method proceeds to return True.
Output: The output of print(solution.isValid("172.16.254.1")) is True, indicating that the IP address "172.16.254.1" is valid.
'''