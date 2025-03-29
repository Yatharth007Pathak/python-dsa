"""
Given a number n, return a list containing the first n Fibonacci numbers.
Note: The first two number of the series are 1 and 1.

Examples:

Input: n = 5
Output: [1, 1, 2, 3, 5]

Input: n = 7
Output: [1, 1, 2, 3, 5, 8, 13]

Input: n = 2
Output: [1, 1]
"""

class Solution:
    # Function to return a list containing the first n Fibonacci numbers.
    def printFibb(self, n):
        # Base cases
        if n <= 0:
            return []
        elif n == 1:
            return [1]
        
        # Initializing the first two Fibonacci numbers
        fib_sequence = [1, 1]
        
        # Generating the Fibonacci sequence up to n elements
        for i in range(2, n):
            # Next Fibonacci number is the sum of the last two numbers
            next_fib = fib_sequence[-1] + fib_sequence[-2]
            fib_sequence.append(next_fib)
        
        return fib_sequence

# Testing the function for input 5 and 7
solution = Solution()
print("First 5 Fibonacci numbers:", solution.printFibb(5))
print("First 7 Fibonacci numbers:", solution.printFibb(7))

'''
Here's a line-by-line breakdown of the code:

class Solution:
Defines a class called Solution to contain the Fibonacci sequence method.

def printFibb(self, n):
Defines a method named printFibb within the Solution class. This method:

Takes self (the instance of the class).
n: an integer representing how many Fibonacci numbers to generate.
if n <= 0:
Checks if n is less than or equal to zero.

return []
If n is zero or negative, it returns an empty list since there are no Fibonacci numbers to generate.

elif n == 1:
Checks if n is exactly one.

return [1]
If n is one, it returns a list with a single element [1], as the first Fibonacci number is 1.

fib_sequence = [1, 1]
Initializes a list fib_sequence with the first two Fibonacci numbers, [1, 1].

for i in range(2, n):
Starts a loop that goes from 2 to n-1, which will calculate the Fibonacci numbers up to the nth element.

next_fib = fib_sequence[-1] + fib_sequence[-2]
Calculates the next Fibonacci number as the sum of the last two elements in fib_sequence.

fib_sequence.append(next_fib)
Appends next_fib to the fib_sequence list, extending the sequence.

return fib_sequence
After generating n Fibonacci numbers, returns the complete fib_sequence list.

solution = Solution()
Creates an instance of the Solution class named solution.

print("First 5 Fibonacci numbers:", solution.printFibb(5))
Calls the printFibb method with n=5 and prints the first 5 Fibonacci numbers, which should be [1, 1, 2, 3, 5].

print("First 7 Fibonacci numbers:", solution.printFibb(7))
Calls the printFibb method with n=7 and prints the first 7 Fibonacci numbers, which should be [1, 1, 2, 3, 5, 8, 13].
'''