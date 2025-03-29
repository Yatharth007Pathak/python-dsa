"""
Given an integer n, your task is to complete the function convertToRoman which prints the corresponding roman number of n. 
Various symbols and their values are given below
Note:- There are a few exceptions for some numbers like 4 in roman is IV,9 in roman is IX, similarly, 
40 is XL while 90 is XC. Similarly, 400 is CD while 900 is CM

I 1          V 5          X 10          L 50          C 100          D 500          M 1000

Example 1:
Input: n = 5
Output: V
 
Example 2:
Input: n = 3
Output: III
"""

class Solution:
    def convertRoman(self, n):
        # Define a list of tuples that map integers to their Roman numeral equivalents
        roman_map = [
            (1000, 'M'),
            (900, 'CM'),
            (500, 'D'),
            (400, 'CD'),
            (100, 'C'),
            (90, 'XC'),
            (50, 'L'),
            (40, 'XL'),
            (10, 'X'),
            (9, 'IX'),
            (5, 'V'),
            (4, 'IV'),
            (1, 'I')
        ]
        
        # Initialize the result string
        result = ""
        
        # Iterate over the roman_map
        for value, symbol in roman_map:
            # While n is greater than or equal to the value, append the symbol to the result
            while n >= value:
                result += symbol
                n -= value  # Decrease n by the value
            
        return result

# Example usage:
sol = Solution()
print(sol.convertRoman(5))  # Output: V
print(sol.convertRoman(3))  # Output: III
print(sol.convertRoman(9))  # Output: IX
print(sol.convertRoman(44))  # Output: XLIV
print(sol.convertRoman(1994))  # Output: MCMXCIV

'''
ere's a pointwise explanation for each line of the given code:

class Solution:
Defines a class named Solution.

def convertRoman(self, n):
Defines a function named convertRoman that takes an integer n as an argument, which represents the number to be converted to a Roman numeral.

roman_map = [...]
Defines a list of tuples called roman_map, where each tuple contains an integer value and its corresponding Roman numeral symbol. 
This list is ordered from the largest to the smallest value to facilitate conversion.

result = ""
Initializes an empty string result to store the resulting Roman numeral as it is built.

for value, symbol in roman_map:
Starts a for loop to iterate over each tuple in roman_map, unpacking each tuple into value (the integer) and symbol (the Roman numeral).

while n >= value:
Checks if n is greater than or equal to the current value. If true, the following block executes to build the Roman numeral.

result += symbol
Appends the corresponding symbol to the result string.

n -= value
Decreases n by the value, effectively reducing the number by the amount represented by the Roman numeral just appended.

return result
Returns the final constructed Roman numeral string stored in result.

# Example usage:
Adds a comment indicating the start of example usage of the function.

sol = Solution()
Creates an instance of the Solution class.

print(sol.convertRoman(5)) # Output: V
Calls convertRoman with the integer 5 and prints the result, which is V.

print(sol.convertRoman(3)) # Output: III
Calls convertRoman with the integer 3 and prints the result, which is III.

print(sol.convertRoman(9)) # Output: IX

Calls convertRoman with the integer 9 and prints the result, which is IX.

print(sol.convertRoman(44)) # Output: XLIV
Calls convertRoman with the integer 44 and prints the result, which is XLIV.

print(sol.convertRoman(1994)) # Output: MCMXCIV
Calls convertRoman with the integer 1994 and prints the result, which is MCMXCIV.
'''