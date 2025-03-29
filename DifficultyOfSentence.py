"""
Given a sentence as a string S. Calculate difficulty of a given sentence.
Difficulty of sentence is defined as 5*(number of hard words) + 3*(number of easy words). 
A word in the given string is considered hard if it has 4 consecutive consonants or number of consonants are more than number of vowels. 
Else the word is easy. 
Note: uppercase and lowercase characters are same.

Example

Input: S = "Difficulty of sentence"
Output: 13
Explanation: 2 hard words + 1 easy word 

Input: S = "I am good"
Output: 9
Explanation: 3 easy words
"""

class Solution:
    def calcDiff(self, S):
        vowels = set('aeiouAEIOU')
        words = S.split()
        hard_count = 0
        easy_count = 0

        for word in words:
            consonant_count = 0
            vowel_count = 0
            max_consecutive_consonants = 0
            current_consecutive_consonants = 0

            for char in word:
                if char.lower() in vowels:
                    vowel_count += 1
                    current_consecutive_consonants = 0
                elif char.isalpha():
                    consonant_count += 1
                    current_consecutive_consonants += 1
                    max_consecutive_consonants = max(max_consecutive_consonants, current_consecutive_consonants)

            # Check if the word is hard
            if max_consecutive_consonants >= 4 or consonant_count > vowel_count:
                hard_count += 1
            else:
                easy_count += 1

        # Calculate difficulty
        difficulty = 5 * hard_count + 3 * easy_count
        return difficulty

# Example usage
sol = Solution()
print(sol.calcDiff("Difficulty of sentence"))  # Output: 13
print(sol.calcDiff("I am good"))  # Output: 9

'''
Here's a detailed, pointwise breakdown of the given code:

Class Definition: The code starts by defining a class named Solution.

Function Definition (calcDiff):
Inside the Solution class, a method named calcDiff is defined, which takes one parameter: S (a string representing a sentence).

Define Vowels Set:
A set named vowels is created containing both lowercase and uppercase vowels (aeiouAEIOU). This set is used to check if a character is a vowel.

Split Sentence into Words:
The sentence S is split into individual words using S.split(). The words list stores all the words from the sentence.

Initialize Counters:
hard_count and easy_count are initialized to 0 to keep track of the number of hard and easy words.

Iterate Through Words:
A for loop iterates over each word in the words list.

Initialize Word-Level Counters:
For each word, consonant_count, vowel_count, max_consecutive_consonants, and current_consecutive_consonants are initialized to 0.
consonant_count keeps track of the number of consonants in the word.
vowel_count keeps track of the number of vowels in the word.
max_consecutive_consonants keeps track of the maximum number of consecutive consonants found in the word.
current_consecutive_consonants keeps track of the current streak of consecutive consonants.

Iterate Through Characters in Word:
For each character (char) in the word:
If char is a vowel (i.e., it is in vowels), increment vowel_count by 1 and reset current_consecutive_consonants to 0.
If char is an alphabetic character (checked using char.isalpha()) but not a vowel, 
increment consonant_count by 1 and increment current_consecutive_consonants by 1.
Update max_consecutive_consonants with the maximum value between max_consecutive_consonants 
and current_consecutive_consonants to track the highest number of consecutive consonants.

Determine if Word is Hard or Easy:
After processing the word, if max_consecutive_consonants is 4 or greater, or if consonant_count is greater than vowel_count, 
the word is considered "hard." Increment hard_count by 1.
Otherwise, the word is considered "easy." Increment easy_count by 1.

Calculate Difficulty:
The difficulty of the sentence is calculated using the formula 5 * hard_count + 3 * easy_count, 
where each hard word contributes 5 to the difficulty score and each easy word contributes 3.

Return Difficulty:
The calculated difficulty value is returned.

Example Usage:
An instance of the Solution class is created and stored in the variable sol.

Example 1: The calcDiff method is called with the string "Difficulty of sentence". 
The output is 13, meaning the sentence difficulty score is 13.

Example 2: The calcDiff method is called with the string "I am good". The output is 9.
'''