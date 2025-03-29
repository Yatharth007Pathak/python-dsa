"""
Given a list of words followed by two words, the task to find the minimum distance between the given two words in the list of words

Example 1:
Input: 
S = { "the", "quick", "brown", "fox",     "quick"}
word1 = "the", word2 = "fox"
Output: 3
Explanation: Minimum distance between the words "the" and "fox" is 3

Example 2:
Input:
S = {"geeks", "for", "geeks", "contribute", "practice"}
word1 = "geeks", word2 = "practice"
Output: 2
Explanation: Minimum distance between the words "geeks" and "practice" is 2
"""

class Solution:
    def shortestDistance(self, s, word1, word2):
        # Initialize positions of the two words to -1 (not found yet)
        pos1, pos2 = -1, -1
        min_distance = float('inf')  # Initialize with infinity
        
        # Iterate through the list of words
        for i in range(len(s)):
            # If word1 is found, update pos1
            if s[i] == word1:
                pos1 = i
                
            # If word2 is found, update pos2
            if s[i] == word2:
                pos2 = i
            
            # If both positions are found, calculate the distance
            if pos1 != -1 and pos2 != -1:
                min_distance = min(min_distance, abs(pos1 - pos2))
        
        return min_distance

# Example usage:

# Example 1:
s = ["the", "quick", "brown", "fox", "quick"]
word1 = "the"
word2 = "fox"
solution = Solution()
print(solution.shortestDistance(s, word1, word2))  # Output: 3

# Example 2:
s = ["geeks", "for", "geeks", "contribute", "practice"]
word1 = "geeks"
word2 = "practice"
print(solution.shortestDistance(s, word1, word2))  # Output: 2

'''
Here's a line-by-line breakdown of the code:

class Solution:
Defines a class Solution, which contains a method to find the shortest distance between two words in a list.

def shortestDistance(self, s, word1, word2):
Defines a method shortestDistance that takes three parameters: s (a list of words), word1, and word2.

pos1, pos2 = -1, -1
Initializes the positions of word1 (pos1) and word2 (pos2) to -1, indicating that they have not been found yet.

min_distance = float('inf')
Initializes min_distance to infinity (float('inf')) as the initial minimum distance, because we are looking for the smallest possible distance.

for i in range(len(s)):
Starts a loop that iterates through the list s, using i as the index.

if s[i] == word1:
Checks if the current word (s[i]) is equal to word1. If true, the position of word1 (pos1) is updated.

pos1 = i
Updates pos1 to the current index i where word1 was found.

if s[i] == word2:
Checks if the current word (s[i]) is equal to word2. If true, the position of word2 (pos2) is updated.

pos2 = i
Updates pos2 to the current index i where word2 was found.

if pos1 != -1 and pos2 != -1:
Checks if both word1 and word2 have been found (i.e., pos1 and pos2 are not -1).

min_distance = min(min_distance, abs(pos1 - pos2))
Calculates the distance between the current positions of word1 and word2, 
and updates min_distance to the smaller value between the previous min_distance and the current distance abs(pos1 - pos2).

return min_distance
After the loop finishes, it returns the shortest distance between word1 and word2.

Example usage:
Example 1:
s = ["the", "quick", "brown", "fox", "quick"]
Defines the list of words s.

word1 = "the"
Specifies word1 as "the".

word2 = "fox"
Specifies word2 as "fox".

solution = Solution()
Creates an instance of the Solution class.

print(solution.shortestDistance(s, word1, word2))
Calls the shortestDistance method with the list s and the two words. 
The output is 3, because the shortest distance between "the" (index 0) and "fox" (index 3) is 3.

Example 2:
s = ["geeks", "for", "geeks", "contribute", "practice"]
Defines a different list of words s.

word1 = "geeks"
Specifies word1 as "geeks".

word2 = "practice"
Specifies word2 as "practice".

print(solution.shortestDistance(s, word1, word2))
Calls the shortestDistance method with this new list and words. 
The output is 2, because the shortest distance between "geeks" (index 2) and "practice" (index 4) is 2.
'''