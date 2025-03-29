"""
A number is called faithful if you can write it as the sum of distinct powers of 7. 
e.g.,  2457 = 7 + 7^2 + 7^4 . 
If we order all the faithful numbers, we get the sequence 1 = 7^0, 7 = 7^1, 8 = 7^0 + 7^1, 49 = 7^2, 50 = 7^0 + 7^2 . . . and so on.
Given some value of N, you have to find the N'th faithful number.

Example 1:
Input: N = 3
Output: 8
Explanation: 8 is the 3rd Faithful number.

Example 2:
Input: N = 7
Output: 57
Explanation: 57 is the 7th Faithful number.
"""

class Solution:
    def nthFaithfulNum(self, N: int) -> int:
        # Initialize result
        result = 0
        power_of_seven = 1
        
        # Convert N to faithful number by examining the binary representation
        while N > 0:
            # If the current bit is set in N, add the corresponding power of 7
            if N % 2 == 1:
                result += power_of_seven
            # Update to the next power of 7
            power_of_seven *= 7
            # Move to the next bit
            N //= 2
        
        return result

# Example usage
sol = Solution()
print(sol.nthFaithfulNum(3))  # Output: 8
print(sol.nthFaithfulNum(7))  # Output: 57


'''
The code calculates the Nth "Faithful Number" where each "faithful number" is constructed by 
adding powers of 7 based on the binary representation of N. Here's a breakdown of how the code works:

How it works:

Binary Representation of N:

The approach is based on representing the number N in binary form. If a bit is set in the binary representation of N, 
the corresponding power of 7 is added to the result.

For example:
Binary of 3: 11 → Faithful number is 7^1 + 7^0 = 7 + 1 = 8
Binary of 7: 111 → Faithful number is 7^2 + 7^1 + 7^0 = 49 + 7 + 1 = 57

Explanation of Key Parts:
result = 0: Initializes the result to 0.
power_of_seven = 1: Starts from 7^0, and it will multiply by 7 at each step (like a power progression).
N % 2 == 1: Checks if the current bit in the binary representation of N is set (1). If it is, it adds the current power of 7 to the result.
N //= 2: Moves to the next bit of N by dividing by 2.

Example:

For N=3:
Binary of 3: 11
First bit (rightmost): 1 → Add 7^0 = 1
Move to the next bit → Next power of 7: 7^1 = 7
Second bit: 1 → Add 7^1 = 7
Result: 1 + 7 = 8

For N=7:
Binary of 7: 111
First bit: 1 → Add 7^0 = 1
Move to the next bit → 7^1 = 7
Second bit: 1 → Add 7^1 = 7
Move to the next bit → 7^2 = 49
Third bit: 1 → Add 7^2 = 49
Result: 1 + 7 + 49 = 57
'''