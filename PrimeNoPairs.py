"""
Find all pairs (sets) of prime numbers (p,q) such that p*q <= n, where n is given number.
 
Example 1:
Input: n = 4
Output: 2 2
Explanation: Pair (2, 2) which has both prime numbers as well as satisfying the condition 2*2 <= 4.

Example 2:
Input: n = 8
Output: 2 2 2 3 3 2
Explanation: Pairs(2, 2), (2, 3) and (3, 2) which has both prime numbers and satisfying the given condition.
"""

class Solution:
    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    def prime_pairs(self, n):
        primes = []
        # Find all primes less than or equal to n
        for i in range(2, n + 1):
            if self.is_prime(i):
                primes.append(i)
        
        result = []
        # Check all pairs of primes
        for i in primes:
            for j in primes:
                if i * j <= n:
                    result.append((i, j))
        
        return result

# Example usage
sol = Solution()
n1 = 4
print(sol.prime_pairs(n1))  # Output: [(2, 2)]

n2 = 8
print(sol.prime_pairs(n2))  # Output: [(2, 2), (2, 3), (3, 2)]

'''
Here is the line-by-line breakdown of the code in pointwise format:

Class Definition:
The class Solution is defined, which contains two methods: 
is_prime to check if a number is prime and prime_pairs to find prime pairs whose product is less than or equal to n.

is_prime Method:
This method checks if a given number num is a prime number.

Check if num is Less Than 2:
The first condition checks if num is less than 2 (if num < 2:). 
Since prime numbers are greater than or equal to 2, the method returns False for numbers less than 2.

Check for Divisors:
A for loop iterates from 2 to int(num**0.5) + 1. This range is efficient because a factor larger than the 
square root of num would already have a corresponding factor smaller than the square root.
If num is divisible by any number in this range (if num % i == 0:), it is not prime, and the method returns False.

Return True for Prime Numbers:
If no divisors are found in the loop, the method returns True, indicating that num is a prime number.

prime_pairs Method:
The prime_pairs method takes an integer n and finds all pairs of prime numbers whose product is less than or equal to n.

Finding All Primes Less Than or Equal to n:
A list primes is initialized to store prime numbers. A for loop iterates from 2 to n, and for each number, 
the is_prime method is called to check if it is prime. If true, the prime number is appended to the primes list.

Finding Valid Prime Pairs:
A list result is initialized to store pairs of primes. Two nested loops go through each combination of primes from the primes list.
For each pair (i, j), the method checks if their product is less than or equal to n (if i * j <= n:). If true, the pair is added to result.

Returning the Result:
After all prime pairs have been checked, the method returns the result list, 
containing all prime pairs whose product is less than or equal to n.

Example Usage:
An instance of the Solution class is created using sol = Solution().

Test Case 1 (n = 4):
The prime_pairs method is called with n = 4. The primes less than or equal to 4 are [2, 3].
The prime pairs whose product is less than or equal to 4 are [(2, 2)].
The output is [(2, 2)].

Test Case 2 (n = 8):
The prime_pairs method is called with n = 8. The primes less than or equal to 8 are [2, 3, 5, 7].
The prime pairs whose product is less than or equal to 8 are [(2, 2), (2, 3), (3, 2)].
The output is [(2, 2), (2, 3), (3, 2)].
'''