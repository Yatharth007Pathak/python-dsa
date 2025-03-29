"""
For a given number n check if it is prime or not. A prime number is a number which is only divisible by 1 and itself.

Examples :

Input: n = 5
Output: 1
Explanation: 5 has 2 factors 1 and 5 only.

Input: n = 25
Output: 0
Explanation: 25 has 3 factors 1, 5, 25
"""

class Solution:
    def isPrime(self, N):
        # A prime number is greater than 1 and has no divisors other than 1 and itself
        if N <= 1:
            return 0
        # Check divisors from 2 to the square root of N
        for i in range(2, int(N ** 0.5) + 1):
            if N % i == 0:
                return 0
        else:
            # If the loop completes without finding any divisors, N is prime
            return 1


sol = Solution()
print(sol.isPrime(5))  # Output: 1
print(sol.isPrime(25)) # Output: 0

'''
Here is a line-by-line breakdown of the code:

class Solution:
This defines a class named Solution, which contains the method isPrime.

def isPrime(self, N):
This defines the method isPrime, which takes two parameters: 
self (referring to the instance of the class) and N (the number to check if it is prime).

if N <= 1:
This checks if the number N is less than or equal to 1. Any number less than or equal to 1 is not prime.

return 0
If N is less than or equal to 1, the method returns 0, indicating that N is not a prime number.

for i in range(2, int(N ** 0.5) + 1):
This loop checks for divisors of N. It iterates over possible divisors starting from 2 up to the square root of N. 
The reason we only check up to the square root is that if N is divisible by any number larger than its square root, 
it must also be divisible by a smaller number (the corresponding factor), 
so checking up to the square root is sufficient to determine if a number is prime.

if N % i == 0:
This checks if N is divisible by i. If N % i == 0, it means N has a divisor other than 1 and itself, so it is not prime.

return 0
If a divisor is found, the method returns 0, indicating that N is not prime.

else:
This else block is attached to the for loop. It is executed if the loop completes without finding any divisors, meaning N is prime.

return 1
If no divisors are found, the method returns 1, indicating that N is a prime number.

Example usage:
sol = Solution()
This creates an instance of the Solution class named sol.

print(sol.isPrime(5))
This calls the isPrime method on 5. Since 5 is a prime number (its only divisors are 1 and 5), the output is 1, indicating that 5 is prime.

print(sol.isPrime(25))
This calls the method on 25. Since 25 is not a prime number (it is divisible by 5), the output is 0, indicating that 25 is not prime.
'''