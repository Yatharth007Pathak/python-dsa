"""
Given a number n. The task is to find the nth catalan number.
The first few Catalan numbers for n = 0, 1, 2, 3, … are 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, …
Catalan Number for n is equal to the number of expressions containing n pairs of parenthesis that are correctly matched, i.e., 
for each of the n(' there exist n ')' on there right and vice versa.
Since answer can be huge return answer modulo 1e9+7.
Note: Positions start from 0 as shown above.

Examples:

Input: n = 3
Output: 5
Explanation: Possible expressions are, ((())), (()()), ()(()), (())(), ()()()

Input: n = 4
Output: 14
Explantions: There are total 14 valid combinations which can be formed using 4 parenthesis.
"""

MOD = int(1e9+7)

class Solution:
    def findCatalan(self, n: int) -> int:
        # Function to compute factorial modulo MOD
        def factorial_mod(n, MOD):
            fact = [1] * (2 * n + 1)
            for i in range(2, 2 * n + 1):
                fact[i] = fact[i - 1] * i % MOD
            return fact
        
        # Function to compute modular inverse using Fermat's Little Theorem
        def mod_inverse(x, MOD):
            return pow(x, MOD - 2, MOD)
        
        # Precompute factorials and their inverses
        fact = factorial_mod(n, MOD)
        inverse_n_factorial = mod_inverse(fact[n], MOD)
        inverse_n_plus_1_factorial = mod_inverse(fact[n + 1], MOD)
        
        # Catalan number formula: C_n = (2n)! / (n! * (n+1)!)
        catalan_n = fact[2 * n] * inverse_n_factorial % MOD
        catalan_n = catalan_n * inverse_n_plus_1_factorial % MOD
        
        return catalan_n

# Example usage:
solution = Solution()
print(solution.findCatalan(3))  # Output: 5
print(solution.findCatalan(4))  # Output: 14

'''
Let's go through the code step by step:

MOD = int(1e9+7)
This defines a constant MOD with a value of 10^9 + 7 = 1000000007, 
which is a large prime number. This is used to perform operations under modulo arithmetic to prevent overflow and keep numbers manageable.

class Solution:
A class named Solution is defined, which will contain the method for calculating the Catalan number.

def findCatalan(self, n: int) -> int:
This defines a method findCatalan that takes an integer n as input and returns an integer result. 
The method is responsible for computing the n-th Catalan number.

def factorial_mod(n, MOD):
Inside findCatalan, another function factorial_mod is defined to compute the factorial of numbers modulo MOD. 
This helps in reducing the size of factorial results.

fact = [1] * (2 * n + 1)
An array fact is initialized with 2 * n + 1 elements, all set to 1. This will store the factorial values for numbers from 0 to 2n modulo MOD.

for i in range(2, 2 * n + 1):
This loop iterates through all numbers from 2 to 2 * n. The goal is to compute the factorial for each number from 2 to 2 * n.

fact[i] = fact[i - 1] * i % MOD
For each number i, the factorial is calculated as fact[i] = (fact[i-1] * i) % MOD. 
The previous factorial value (fact[i-1]) is multiplied by i, and the result is taken modulo MOD to keep it manageable.

return fact
After computing all factorials, the function returns the fact array containing factorials modulo MOD up to 2 * n.

def mod_inverse(x, MOD):
A helper function mod_inverse is defined to compute the modular inverse of a number x under modulo MOD. 
The modular inverse is needed to divide numbers in modular arithmetic.

return pow(x, MOD - 2, MOD)
Fermat's Little Theorem is used to compute the modular inverse. 
The theorem states that for a prime MOD, the modular inverse of x is x^(MOD-2) % MOD. 
This is done using Python's pow function, which efficiently computes powers with modulo.

fact = factorial_mod(n, MOD)
The factorial_mod function is called with n and MOD to precompute all factorials up to 2 * n.

inverse_n_factorial = mod_inverse(fact[n], MOD)
The modular inverse of n! (stored in fact[n]) is computed using the mod_inverse function. This value will be used in the Catalan number formula.

inverse_n_plus_1_factorial = mod_inverse(fact[n + 1], MOD)
The modular inverse of (n + 1)! (stored in fact[n + 1]) is also computed using mod_inverse.

catalan_n = fact[2 * n] * inverse_n_factorial % MOD
The first part of the Catalan number formula C_n = (2n)! / (n! * (n+1)!) is calculated. 
The numerator is (2n)! (stored in fact[2 * n]), and it's multiplied by the modular inverse of n! modulo MOD. The result is taken modulo MOD.

catalan_n = catalan_n * inverse_n_plus_1_factorial % MOD
The second part of the Catalan formula involves dividing by (n+1)!. 
This is done by multiplying the result with the modular inverse of (n + 1)!, again taken modulo MOD.

return catalan_n
The computed Catalan number C_n is returned as the result.

solution = Solution()
An instance of the Solution class is created.

print(solution.findCatalan(3)) # Output: 5
The findCatalan method is called with n = 3. It computes the 3rd Catalan number, which is 5.

print(solution.findCatalan(4)) # Output: 14
Similarly, the findCatalan method is called with n = 4. It computes the 4th Catalan number, which is 14.
'''