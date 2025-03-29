"""
For a given non-negative integer N, find the next smallest Happy Number. A number is called Happy if it leads to 1 after a sequence of steps. 
Wherein at each step the number is replaced by the sum of squares of its digits that is, if we start with Happy Number 
and keep replacing it with sum of squares of its digits, we reach 1 at some point.
 
Example 1:

Input: N = 8
Output: 10
Explanation: Next happy number after 8 is 10 since 1*1 + 0*0 = 1

Example 2:
Input: N = 10
Output: 13
Explanation: After 10, 13 is the smallest happy number because 1*1 + 3*3 = 10, so we replace 13 by 10 and 1*1 + 0*0 = 1.
"""

class Solution:
    def nextHappy(self, N):
        # Helper function to determine if a number is happy
        def isHappy(num):
            visited = set()
            while num != 1 and num not in visited:
                visited.add(num)
                num = sum(int(digit) ** 2 for digit in str(num))
            return num == 1
        
        # Start checking from the next number
        N += 1
        while not isHappy(N):
            N += 1
        return N


# Example usage:
solution = Solution()
print(solution.nextHappy(8))   # Output: 10
print(solution.nextHappy(10))  # Output: 13

'''
Here's a breakdown of the code, line by line:

class Solution:
Defines a class named Solution that contains the method nextHappy.

def nextHappy(self, N):
A method in the Solution class to find the next "happy number" greater than N.

def isHappy(num):
Defines a helper function isHappy that checks if a number is a happy number.

visited = set()
Initializes a set visited to keep track of numbers encountered during the process to avoid cycles.

while num != 1 and num not in visited:
Runs a loop until num becomes 1 (indicating it is happy) or it forms a cycle by revisiting a number.

visited.add(num)
Adds the current number num to the visited set to track numbers already processed.

num = sum(int(digit) ** 2 for digit in str(num))
Computes the sum of squares of the digits of num. This is the core operation to determine if the number is happy.

return num == 1
Returns True if num equals 1 (indicating it's a happy number) or False otherwise.

N += 1
Increments N by 1 to start checking for the next happy number.

while not isHappy(N):
Continues incrementing N until the isHappy function returns True.

N += 1
Increments N if the current number is not happy.

return N
Returns the first happy number greater than the input N.

solution = Solution()
Creates an instance of the Solution class.

print(solution.nextHappy(8))
Calls the nextHappy method with 8 as input and prints the result. The output is 10 (the next happy number after 8).

print(solution.nextHappy(10))
Calls the nextHappy method with 10 as input and prints the result. The output is 13 (the next happy number after 10).
'''