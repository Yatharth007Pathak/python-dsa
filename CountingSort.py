"""
Given a string arr consisting of lowercase english letters, arrange all its letters in lexicographical order using Counting Sort.

Example 1:

Input: N = 5, S = "edsab"
Output: abdes
Explanation: In lexicographical order, string will be abdes.

Example 2:
Input: N = 13, S = "geeksforgeeks"
Output: eeeefggkkorss
Explanation: In lexicographical order, string will be eeeefggkkorss.

Counting Sort
Concept: Counts the occurrences of each distinct element and uses this count to place elements directly into their correct positions. 
It's a non-comparative sorting algorithm.
Pros: Very efficient with O(n + k) time complexity when the range of the input values is not too large.
Cons: Not suitable for large ranges or non-integer values.
"""

class Solution:
    def countSort(self, arr):
        # The counting sort array for all lowercase English letters
        # There are 26 lowercase English letters
        count = [0] * 26
        
        # Count the frequency of each character in the input string
        for char in arr:
            count[ord(char) - ord('a')] += 1
        
        # Build the sorted string based on the frequency array
        sorted_string = []
        for i in range(26):
            if count[i] > 0:
                # Append the character corresponding to the current index
                sorted_string.append(chr(i + ord('a')) * count[i])
        
        # Join the list to form the final sorted string
        return ''.join(sorted_string)

# Example usage:
sol = Solution()

# Example 1:
S1 = "edsab"
print(sol.countSort(S1))  # Output: abdes

# Example 2:
S2 = "geeksforgeeks"
print(sol.countSort(S2))  # Output: eeeefggkkorss

'''
Here's a detailed breakdown of the Count Sort code:

class Solution:
Defines a class named Solution, which will contain sorting methods.

def countSort(self, arr):
Defines a method countSort within the Solution class. It takes one parameter arr, which is the input string to be sorted.

# The counting sort array for all lowercase English letters
A comment indicating that the next array will be used to count the occurrences of each lowercase English letter.

# There are 26 lowercase English letters
A comment specifying that there are 26 lowercase English letters in the alphabet.

count = [0] * 26
Initializes a list count of size 26 (one for each letter of the alphabet), with all elements set to 0. 
This list will be used to count the frequency of each character.

# Count the frequency of each character in the input string
A comment explaining that the following loop will count how many times each character appears in the input string.

for char in arr:
Starts a for loop to iterate through each character char in the input string arr.

count[ord(char) - ord('a')] += 1
Uses the ord function to get the ASCII value of char and calculates the index in the count list by subtracting the ASCII value of 'a'. 
This index corresponds to the position of the character in the alphabet (0 for 'a', 1 for 'b', etc.). Increments the count at that index.

# Build the sorted string based on the frequency array
A comment indicating that the next step is to build the sorted string from the frequency array.

sorted_string = []
Initializes an empty list sorted_string to store the characters in sorted order.

for i in range(26):
Starts a for loop to iterate over the indices of the count list (from 0 to 25).

if count[i] > 0:
Checks if the count at index i is greater than 0. This means that the character corresponding to this index is present in the input string.

# Append the character corresponding to the current index
A comment explaining that the following line will add the character corresponding to the current index to the sorted string.

sorted_string.append(chr(i + ord('a')) * count[i])
Uses the chr function to convert the index i back to a character by adding it to the ASCII value of 'a'. 
Appends the character multiplied by its frequency (i.e., the character repeated count[i] times) to the sorted_string list.

# Join the list to form the final sorted string
A comment explaining that the next step is to join the list into a single string.

return ''.join(sorted_string)
Joins the elements of the sorted_string list into a single string and returns it.

# Example usage:
A comment indicating the start of examples demonstrating how to use the countSort method.

sol = Solution()
Creates an instance of the Solution class named sol.

# Example 1:
A comment introducing the first example.

S1 = "edsab"
Initializes a string S1 with the sample value "edsab".

print(sol.countSort(S1)) # Output: abdes
Calls the countSort method on sol with S1 and prints the result. The expected output is "abdes".

# Example 2:
A comment introducing the second example.

S2 = "geeksforgeeks"
Initializes a string S2 with the sample value "geeksforgeeks".

print(sol.countSort(S2)) # Output: eeeefggkkorss
Calls the countSort method on sol with S2 and prints the result. The expected output is "eeeefggkkorss".
'''