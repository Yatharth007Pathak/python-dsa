"""
Given 2 strings a and b consisting of lowercase characters. The task is to check whether 2 given strings are an anagram of each other or not. 
An anagram of a string is another string that contains the same characters, only the order of characters can be different. 
For example, act and tac are an anagram of each other. Strings a and b can only contain lowercase alphabets.

Note:-
If the strings are anagrams you have to return True or else return False. |s| represents the length of string s.


Example 1:
Input:a = geeksforgeeks, b = forgeeksgeeks
Output: YES
Explanation: Both the string have same characters with same frequency. So, they are anagrams.

Example 2:
Input:a = allergy, b = allergic
Output: NO
Explanation: Characters in both the strings are not same, so they are not anagrams.
"""

from collections import Counter

class Solution:
    
    # Function to check whether two strings are anagram of each other or not.
    def isAnagram(self, a, b):
        # Using Counter to compare character frequencies of both strings
        return Counter(a) == Counter(b)

# Test code
solution = Solution()
test_cases = [("geeksforgeeks", "forgeeksgeeks"), ("allergy", "allergic")]

for a, b in test_cases:
    if solution.isAnagram(a, b):
        print("YES")
    else:
        print("NO")

'''
Here's a pointwise explanation for each line of the given code:

from collections import Counter
Imports the Counter class from the collections module, which is used to count the frequency of elements in a collection.

class Solution:
Defines a class named Solution.

# Function to check whether two strings are anagram of each other or not.
Adds a comment describing the purpose of the function isAnagram.

def isAnagram(self, a, b):
Defines a function named isAnagram which takes two arguments a and b (the strings to be checked).

return Counter(a) == Counter(b)
Uses Counter to count the frequency of characters in both strings a and b, and returns True if they are equal, 
meaning the strings are anagrams, otherwise returns False.

# Test code
Adds a comment indicating the start of the test code.

solution = Solution()
Creates an instance of the Solution class.

test_cases = [("geeksforgeeks", "forgeeksgeeks"), ("allergy", "allergic")]
Defines a list test_cases containing tuples of strings to test the isAnagram function.

for a, b in test_cases:
Starts a for loop to iterate over each pair of strings (a, b) in test_cases.

if solution.isAnagram(a, b):
Calls the isAnagram function for the current pair of strings. Checks if the return value is True.

print("YES")
If the strings are anagrams (isAnagram returns True), prints "YES".

else:
If the strings are not anagrams (isAnagram returns False), executes the next statement.

print("NO")
Prints "NO" if the strings are not anagrams.
'''