"""
We define f (X, Y) as number of different corresponding bits in binary representation of X and Y. 
For example, f (2, 7) = 2, since binary representation of 2 and 7 are 010 and 111, respectively. 
The first and the third bit differ, so f (2, 7) = 2.

You are given an array A of N integers, A1, A2 ,…, AN. Find sum of f(Ai, Aj) for all ordered pairs (i, j) such that 1 ≤ i, j ≤ N. 
Return the answer modulo 109+7.

Example 1:
Input: N = 2, A = {2, 4}
Output: 4
Explaintion: We return f(2, 2) + f(2, 4) + f(4, 2) + f(4, 4) = 0 + 2 + 2 + 0 = 4.

Example 2:
Input: N = 3,A = {1, 3, 5}
Output: 8
Explaination: We return f(1, 1) + f(1, 3) + f(1, 5) + f(3, 1) + f(3, 3) + f(3, 5) + f(5, 1) + f(5, 3) + f(5, 5) = 0+1+1+1+0+2+1+2+0=8.
"""

class Solution:
    def countBits(self, N, A):
        MOD = 10**9 + 7
        total_sum = 0
        
        # Loop over each bit position (0 to 31, assuming 32-bit integers)
        for bit in range(32):
            # Count how many numbers have the current bit set
            count_set_bits = sum((num >> bit) & 1 for num in A)
            count_unset_bits = N - count_set_bits
            
            # For each bit position, the contribution to the total sum is the product of pairs
            bit_contribution = (count_set_bits * count_unset_bits * 2) % MOD
            total_sum = (total_sum + bit_contribution) % MOD
        
        return total_sum
    
solution = Solution()
print(solution.countBits(2, [2, 4]))  # Output: 4
print(solution.countBits(3, [1, 3, 5]))  # Output: 8

'''
Here's a line-by-line breakdown of the code:

Define the Solution class: This class contains the countBits method, which calculates the bitwise sum difference 
for each bit position across an array A of integers.

Define the countBits method: It takes in N (number of elements in the array A) and A (the list of integers) 
and returns the total sum of bitwise differences for all bit positions.

Initialize MOD as 10^9 + 7: This modulus is used to keep the result manageable and prevent overflow, 
as required in many programming competitions.

Initialize total_sum to 0: This variable will store the cumulative sum of all bitwise differences across all bit positions.

Loop over each bit position (from 0 to 31): This assumes 32-bit integers, so we check each of the 32 bits.

Count how many numbers have the current bit set (count_set_bits): For each number in A, 
shift it right by bit positions and check if the least significant bit is 1. Sum these results to get the count of numbers with this bit set.

Calculate count_unset_bits as N - count_set_bits: This gives the count of numbers with the current bit 
unset by subtracting count_set_bits from the total number of integers N.

Calculate the contribution of the current bit to the total_sum:
For each bit position, the contribution to total_sum is the product of pairs of numbers with different values for this bit. 
Thus, count_set_bits * count_unset_bits * 2 is added to the total.
Use the modulus operation to prevent overflow by calculating (bit_contribution % MOD).

Add bit_contribution to total_sum (mod MOD).

Return total_sum: The function finally returns the cumulative bitwise difference sum.

Example Usage and Output

Input:
N = 2
A = [2, 4]

Output: 4

Explanation: The array [2, 4] has two elements, and for each bit position, the bitwise differences contribute to the total sum of 4.
'''