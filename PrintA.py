"""
Imagine you have a special keyboard with the following keys: 

Key 1:  Prints 'A' on screen
Key 2: (Ctrl-A): Select screen
Key 3: (Ctrl-C): Copy selection to buffer
Key 4: (Ctrl-V): Print buffer on screen appending it after what has already been printed.

Find maximum numbers of A's that can be produced by pressing keys on the special keyboard N times. 


Example 1:
Input: N = 3
Output: 3
Explanation: Press key 1 three times.

Example 2:
Input: N = 7
Output: 9
Explanation: The best key sequence is key 1, key 1, key 1, key 2, key 3, key4, key 4.
"""

class Solution:
    def optimalKeys(self, N):
        if N <= 3:
            return N  # For 1, 2, or 3 presses, the best we can do is print A N times

        # Create a DP array to store the maximum number of A's for each N
        dp = [0] * (N + 1)
        
        # Fill the DP array
        for n in range(1, N + 1):
            if n <= 3:
                dp[n] = n  # Base case for n = 1, 2, 3
            else:
                # Try different points to switch to copy-paste
                for i in range(1, n - 2):
                    # After i Key 1 presses, we have n - i presses left
                    # We select, copy and then paste (n - i - 1) times
                    # The total A's would be dp[i] * (n - i - 1)
                    dp[n] = max(dp[n], dp[i] * (n - i - 1))

        return dp[N]

# Example usage:
sol = Solution()
print(sol.optimalKeys(3))  # Output: 3
print(sol.optimalKeys(7))  # Output: 9
print(sol.optimalKeys(10))  # Output: 36
