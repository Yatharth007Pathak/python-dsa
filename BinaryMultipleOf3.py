"""
Given a number in its binary form find if the given binary number is a multiple of 3. 
It is recommended to finish the task using one traversal of input binary number.

Example 1:
Input: S = "0011"
Output: 1
Explanation: "0011" is 3, which is divisible by 3.

Example 2:
Input: S = "100"
Output: 0
Explanation: "100"'s decimal equivalent is 4, which is not divisible by 3.
"""

class Solution:
    def isDivisible(self, s):
        remainder = 0
        
        # Traverse each bit of the binary string
        for i in range(len(s)):
            # Shift remainder left (multiply by 2) and add current bit's value. This result is taken modulo 3
            remainder = (remainder * 2 + int(s[i])) % 3
            
        # If remainder is 0, then the binary number is divisible by 3
        return 1 if remainder == 0 else 0

# Example usage
sol = Solution()
print(sol.isDivisible("0011"))  # Output: 1
print(sol.isDivisible("100"))   # Output: 0

'''
Here's a pointwise breakdown of the code:

class Solution:
Defines a class named Solution to encapsulate the method isDivisible.

def isDivisible(self, s):
Defines a method isDivisible that takes self (to refer to the object) and a binary string s as input.

remainder = 0
Initializes a variable remainder to 0, which will be used to compute the remainder when the binary number is divided by 3.

for i in range(len(s)):
Starts a loop that iterates through each character (bit) in the binary string s.

remainder = (remainder * 2 + int(s[i])) % 3
In each iteration, the current remainder is multiplied by 2 (equivalent to shifting left in binary), 
and the current bit's value (s[i]) is added. This result is taken modulo 3 to keep track of the remainder when dividing the binary number by 3.

return 1 if remainder == 0 else 0
After the loop, if the remainder is 0, it returns 1 (indicating the binary number is divisible by 3); 
otherwise, it returns 0 (not divisible by 3).

sol = Solution()
Creates an instance of the Solution class named sol.

print(sol.isDivisible("0011"))
Calls the isDivisible method with the binary string "0011" and prints the result, 
which is 1 (since the decimal value of "0011" is 3, which is divisible by 3).

print(sol.isDivisible("100"))
Calls the isDivisible method with the binary string "100" and prints the result, 
which is 0 (since the decimal value of "100" is 4, which is not divisible by 3).

Example Walkthrough:

For input "0011":
Start with remainder = 0.
After processing the first two 0s, the remainder stays 0.
Process the third bit (1): remainder = (0 * 2 + 1) % 3 = 1.
Process the fourth bit (1): remainder = (1 * 2 + 1) % 3 = 0.
Since remainder == 0, "0011" is divisible by 3, so the output is 1.

For input "100":
Start with remainder = 0.
Process the first bit (1): remainder = (0 * 2 + 1) % 3 = 1.
Process the second bit (0): remainder = (1 * 2 + 0) % 3 = 2.
Process the third bit (0): remainder = (2 * 2 + 0) % 3 = 1.
Since remainder != 0, "100" is not divisible by 3, so the output is 0.
'''