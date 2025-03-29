"""
Given a string of characters, find the length of the longest proper prefix which is also a proper suffix.

Note: Prefix and suffix can be overlapping but they should not be equal to the entire string.

Examples :

Input: str = "abab"
Output: 2
Explanation: "ab" is the longest proper prefix and suffix.

Input: str = "aaaa"
Output: 3
Explanation: "aaa" is the longest proper prefix and suffix. 

Input: s = "aabcdaabc"
Output: 4
Explanation: The string "aabc" is the longest prefix and suffix.
"""

class Solution:
    def lps(self, s):
        n = len(s)
        
        # Create an array to store the length of the longest prefix suffix for each substring
        lps_array = [0] * n
        
        # Start with the first character, no proper prefix for a single character
        length = 0  # length of the previous longest prefix suffix
        i = 1

        # Build the lps_array
        while i < n:
            if s[i] == s[length]:
                length += 1
                lps_array[i] = length
                i += 1
            else:
                if length != 0:
                    # Fall back to the last matching position
                    length = lps_array[length - 1]
                else:
                    lps_array[i] = 0
                    i += 1
        
        # The value in the last index of lps_array will give the length of
        # the longest proper prefix that is also a suffix.
        return lps_array[n - 1]

sol = Solution()

# Test Case 1
s1 = "abab"
print(sol.lps(s1))  # Output: 2 ("ab" is the longest prefix-suffix)

# Test Case 2
s2 = "aaaa"
print(sol.lps(s2))  # Output: 3 ("aaa" is the longest prefix-suffix)

'''
The code is an implementation of the Longest Prefix Suffix (LPS) algorithm, 
which is used in the KMP (Knuth-Morris-Pratt) pattern matching algorithm. Here's a breakdown of the code line by line:

class Solution:
This line defines a Python class called Solution. It's a container for the method lps() that follows.

def lps(self, s):
This line defines a method named lps inside the Solution class. It takes two arguments: 
self (referring to the instance of the class) and s, the input string for which the LPS array needs to be computed.

n = len(s)
This line calculates the length of the input string s and stores it in the variable n.

lps_array = [0] * n
This creates an array called lps_array of length n where each element is initialized to 0. 
This array will store the length of the longest prefix suffix for each substring of s.

length = 0
Initializes the variable length to 0, which keeps track of the current length of the longest proper prefix that is also a suffix.

i = 1
Sets the index i to 1 because the first character of the string has no proper prefix.

while i < n:
Starts a while loop that iterates over the string from index 1 to n-1.

if s[i] == s[length]:
This checks if the current character (s[i]) matches the character at the length position (i.e., the next character in the current prefix).

length += 1
If the characters match, increment length by 1 because the current prefix has increased.

lps_array[i] = length
Store the updated length in lps_array[i] to indicate the length of the longest prefix suffix for the substring ending at index i.

i += 1
Move to the next character by incrementing i.

else:
If the characters do not match, the else block handles this case.

if length != 0:
If length is not zero, fall back to the previous longest prefix suffix.

length = lps_array[length - 1]
Set length to the value of the LPS at the previous position (length - 1), which helps avoid unnecessary re-checking of characters.

else:
If length is zero, it means there is no matching prefix for the current substring.

lps_array[i] = 0
Set lps_array[i] to 0, indicating no prefix suffix match for this character.

i += 1
Move to the next character by incrementing i.

return lps_array[n - 1]
After completing the loop, the method returns the value at the last index of lps_array, 
which represents the length of the longest prefix suffix for the entire string s.

sol = Solution()
This line creates an instance of the Solution class.

s1 = "abab"
Assigns the string "abab" to the variable s1.

print(sol.lps(s1))
Calls the lps() method with the input s1 and prints the result. For "abab", the expected output is 2, as "ab" is the longest prefix suffix.

s2 = "aaaa"
Assigns the string "aaaa" to the variable s2.

print(sol.lps(s2))
Calls the lps() method with the input s2 and prints the result. For "aaaa", the expected output is 3, as "aaa" is the longest prefix suffix.
'''