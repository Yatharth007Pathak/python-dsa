"""
Print numbers from 1 to n without the help of loops. You only need to complete the function printNos() 
that takes N as parameter and prints number from 1 to N recursively.
Don't print newline, it will be added by the driver code.

Examples

Input: n = 10
Output: 1 2 3 4 5 6 7 8 9 10
"""

class Solution:
    # Complete this function
    def printNos(self, N):
        # Base case
        if N == 0:
            return
        # Recursively call the function for N-1
        self.printNos(N-1)
        # Print the current number
        print(N, end=' ')

# Example usage
sol = Solution()
sol.printNos(10)

'''
Here's a breakdown of the code, which prints numbers from 1 to N using recursion:

class Solution:
Defines a class Solution which contains the method printNos.

def printNos(self, N):
This method prints numbers from 1 to N using recursion.

if N == 0:
The base case for recursion: If N is 0, the function returns, ending the recursive calls.

return
Stops further recursive calls when N reaches 0.

self.printNos(N - 1)
This is the recursive call that reduces N by 1. The function keeps calling itself with smaller values of N until it reaches the base case (N=0).

print(N, end=' ')
After returning from the recursive call, this statement prints the current value of N. 
The numbers are printed in ascending order because the recursive call for N-1 is executed before the print(N) statement. 
The end=' ' argument ensures that the numbers are printed on the same line with a space separating them.

sol = Solution()
Creates an instance of the Solution class.

sol.printNos(10)
Calls the printNos method with N = 10, which prints the numbers from 1 to 10 in sequence.

How It Works:
The recursion starts with N = 10. Each recursive call reduces N by 1 and moves toward the base case.
Once N reaches 0, the recursion stops and the numbers are printed in reverse order of the recursive calls, i.e., from 1 to 10.
'''