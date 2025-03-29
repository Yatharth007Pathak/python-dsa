"""
Given two numbers as strings s1 and s2. Calculate their Product.
Note: The numbers can be negative and You are not allowed to use any built-in function or convert the strings to integers. 
There can be zeros in the begining of the numbers. You don't need to specify '+' sign in the begining of positive numbers.

Example 1:
Input: s1 = "0033", s2 = "2"
Output: 66

Example 2:
Input: s1 = "11", s2 = "23"
Output: 253
"""

class Solution:
    def multiplyStrings(self, s1: str, s2: str) -> str:
        # Check for negative numbers
        negative = (s1[0] == '-') ^ (s2[0] == '-')
        s1 = s1.lstrip('-0') or "0"
        s2 = s2.lstrip('-0') or "0"

        if s1 == "0" or s2 == "0":
            return "0"

        # Initialize result array
        result = [0] * (len(s1) + len(s2))

        # Multiply each digit
        for i in range(len(s1) - 1, -1, -1):
            for j in range(len(s2) - 1, -1, -1):
                mul = (ord(s1[i]) - ord('0')) * (ord(s2[j]) - ord('0'))
                sum_ = mul + result[i + j + 1]

                result[i + j + 1] = sum_ % 10
                result[i + j] += sum_ // 10

        # Convert result to string
        result_str = ''.join(map(str, result)).lstrip('0')

        # Add negative sign if necessary
        if negative:
            result_str = '-' + result_str

        return result_str

# Example usage
solution = Solution()
print(solution.multiplyStrings("0033", "2"))  # Output: 66
print(solution.multiplyStrings("11", "23"))   # Output: 253

        

'''
Here is a line-by-line breakdown of the code:

class Solution:
Defines a class named Solution.

def multiplyStrings(self, s1: str, s2: str) -> str:
Defines a function named multiplyStrings inside the Solution class. It takes two strings (s1 and s2) as input and returns a string.

negative = (s1[0] == '-') ^ (s2[0] == '-')
Checks if the result of multiplication will be negative. The XOR (^) operator returns True if only one of the numbers is negative, 
and False otherwise.

s1 = s1.lstrip('-0') or "0"
Strips leading '-' and '0' from s1. If the resulting string is empty, assigns "0" to s1.

s2 = s2.lstrip('-0') or "0"
Similarly, strips leading '-' and '0' from s2. If the resulting string is empty, assigns "0" to s2.

if s1 == "0" or s2 == "0":
Checks if either s1 or s2 is "0". If true, returns "0" because multiplying by zero results in zero.

result = [0] * (len(s1) + len(s2))
Initializes an array result of size len(s1) + len(s2) with all elements as 0. This array will store intermediate results of multiplication.

for i in range(len(s1) - 1, -1, -1):
Iterates through s1 from the last digit to the first digit.

for j in range(len(s2) - 1, -1, -1):
Iterates through s2 from the last digit to the first digit for each digit of s1.

mul = (ord(s1[i]) - ord('0')) * (ord(s2[j]) - ord('0'))
Converts the characters s1[i] and s2[j] to their corresponding integer values by subtracting '0' and calculates the product.

sum_ = mul + result[i + j + 1]
Adds the product (mul) to the value at result[i + j + 1] (previous carry value if any).

result[i + j + 1] = sum_ % 10
Stores the last digit of sum_ at result[i + j + 1].

result[i + j] += sum_ // 10
Adds the carry (if any) to result[i + j].

result_str = ''.join(map(str, result)).lstrip('0')
Joins the result list into a single string and strips leading zeros.

if negative:
Checks if the result should be negative.

result_str = '-' + result_str
Adds a negative sign to the result_str if necessary.

return result_str
Returns the final result as a string.

solution = Solution()
Creates an instance of the Solution class.

print(solution.multiplyStrings("0033", "2"))
Calls the multiplyStrings method with "0033" and "2" and prints the result. Output: 66.

print(solution.multiplyStrings("11", "23"))
Calls the multiplyStrings method with "11" and "23" and prints the result. Output: 253.
'''