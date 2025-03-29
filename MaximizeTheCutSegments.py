"""
Given an integer n denoting the Length of a line segment. You need to cut the line segment in such a way that the cut length 
of a line segment each time is either x , y or z. Here x, y, and z are integers.
After performing all the cut operations, your total number of cut segments must be maximum. Return the maximum number of cut segments possible.

Note: if no segment can be cut then return 0.

Examples:

Input: n = 4, x = 2, y = 1, z = 1
Output: 4
Explanation: Total length is 4, and the cut lengths are 2, 1 and 1.  We can make maximum 4 segments each of length 1.

Input: n = 5, x = 5, y = 3, z = 2
Output: 2
Explanation: Here total length is 5, and the cut lengths are 5, 3 and 2. We can make two segments of lengths 3 and 2.

Input: n = 7, x = 8, y = 9, z = 10
Output: 0
Explanation: Here the total length is 7, and the cut lengths are 8, 9, and 10. 
We cannot cut the segment into lengths that fully utilize the segment, so the output is 0.
"""

class Solution:
    def maximizeTheCuts(self, n, x, y, z):
        # Initialize a dp array with -1, meaning no cuts possible initially
        dp = [-1] * (n + 1)
        
        # Base case: no cuts needed for length 0
        dp[0] = 0
        
        # Iterate over all lengths from 1 to n
        for i in range(1, n + 1):
            # Check if we can make a cut of length x
            if i >= x and dp[i - x] != -1:
                dp[i] = max(dp[i], dp[i - x] + 1)
                
            # Check if we can make a cut of length y
            if i >= y and dp[i - y] != -1:
                dp[i] = max(dp[i], dp[i - y] + 1)
                
            # Check if we can make a cut of length z
            if i >= z and dp[i - z] != -1:
                dp[i] = max(dp[i], dp[i - z] + 1)
        
        # If no cuts are possible for length n, return 0
        return max(dp[n], 0)

solution = Solution()
print(solution.maximizeTheCuts(4, 2, 1, 1))  # Output: 4
print(solution.maximizeTheCuts(5, 5, 3, 2))  # Output: 2
print(solution.maximizeTheCuts(7, 8, 9, 10)) # Output: 0

'''

Here's a breakdown of the code for finding the maximum number of cuts possible for a given length n with available cut lengths x, y, and z:

Class Solution:
Defines a class Solution containing the method maximizeTheCuts to find the maximum number of cuts possible for a rod of length n.

Method maximizeTheCuts:
Takes four parameters: n (total length of the rod), and x, y, z (possible lengths for each cut).

Dynamic Programming Array dp:
Initializes a dynamic programming array dp of size n + 1, where dp[i] will store the maximum number of cuts possible for a rod of length i.
Sets each element initially to -1, representing that no cuts are possible.
Sets dp[0] = 0, as no cuts are needed for a rod of length 0.

Iterate Over All Lengths from 1 to n:
Loops through each rod length i from 1 to n to determine the maximum number of cuts possible at each length.

Check and Update Possible Cuts for Each Length:
Cut of length x: If the current length i is at least x and dp[i - x] is not -1 (indicating that cuts are possible for i - x), 
then it updates dp[i] to be the maximum of dp[i] and dp[i - x] + 1.
Cut of length y: Similar to the x check, updates dp[i] if cuts are possible for i - y.
Cut of length z: Updates dp[i] if cuts are possible for i - z.

Result:
Once the loop completes, dp[n] holds the maximum number of cuts possible for a rod of length n.
If no cuts are possible, dp[n] will be -1, so the method returns 0 in such cases using max(dp[n], 0).

Example Usage:
Creates an instance of Solution and calls maximizeTheCuts with different values to demonstrate the results:
For maximizeTheCuts(4, 2, 1, 1), the output is 4.
For maximizeTheCuts(5, 5, 3, 2), the output is 2.
For maximizeTheCuts(7, 8, 9, 10), the output is 0.

Explanation of Example Outputs:
Input: n = 4, x = 2, y = 1, z = 1
The rod can be cut four times with cuts of 1, achieving the maximum possible cuts of 4.
Input: n = 5, x = 5, y = 3, z = 2
The rod can be cut into two pieces of lengths 3 and 2.
Input: n = 7, x = 8, y = 9, z = 10
Since all cut lengths are larger than 7, no cuts are possible, so the output is 0.
'''