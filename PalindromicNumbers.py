"""
Count the number of palindromic numbers less than N.

Example 1:
Input: N = 12
Output: 10
Explanation: There are 10 palindrome number less than 12. (1 2 3 4 5 6 7 8 9 11)

Example 2:
Input:
N = 104
Output: 19
Explanation: There are 19 palindrome number less than 104
"""

class Solution:
    def is_palindrome(self, num):
        # Convert the number to string and check if it is the same when reversed
        return str(num) == str(num)[::-1]

    def palindromicNumbers(self, N):
        count = 0
        for num in range(1, N):
            if self.is_palindrome(num):
                count += 1
        return count

# Example usage:
solution = Solution()

# Example 1:
N1 = 12
print(solution.palindromicNumbers(N1))  # Output: 10

# Example 2:
N2 = 104
print(solution.palindromicNumbers(N2))  # Output: 19

'''

'''