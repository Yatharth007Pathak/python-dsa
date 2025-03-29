"""
Given a string str of lowercase alphabets and a number k, the task is to print the minimum value of the string after removal of k characters. 
The value of a string is defined as the sum of squares of the count of each distinct character present in the string. 
Return the minimum possible required value.

Examples :

Input: str = abccc, k = 1
Output: 6
Explaination: We remove c to get the value as 1^2 + 1^2 + 2^2

Input: str = aabcbcbcabcc, k = 3
Output: 27
Explaination: We remove two 'c' and one 'b'. Now we get the value as 3^2 + 3^2 + 3^2.
"""

from collections import Counter
import heapq

class Solution:
    def minValue(self, s, k):
        # Step 1: Count the frequency of each character
        freq = Counter(s)
        
        # Step 2: Use a max-heap (negative of frequencies to simulate max-heap)
        max_heap = [-count for count in freq.values()]
        heapq.heapify(max_heap)
        
        # Step 3: Perform k removals
        while k > 0 and max_heap:
            # Pop the most frequent character (negative value, so we add 1)
            max_freq = heapq.heappop(max_heap)
            max_freq += 1  # Decrease the frequency by 1 (since it's negative)
            k -= 1
            # If the reduced frequency is still greater than 0, push it back
            if max_freq < 0:
                heapq.heappush(max_heap, max_freq)
        
        # Step 4: Calculate the sum of squares of the remaining frequencies
        result = 0
        for freq in max_heap:
            result += freq ** 2  # freq is negative, so squaring it makes it positive
        
        return result

# Example usage:
sol = Solution()
print(sol.minValue("abccc", 1))  # Output: 6
print(sol.minValue("aabcbcbcabcc", 3))  # Output: 27

'''
Here is a line-by-line breakdown of the provided code:

from collections import Counter
Imports the Counter class from the collections module. Counter is used to count the occurrences of elements in a collection.

import heapq
Imports the heapq module, which provides an implementation of the heap queue algorithm, also known as the priority queue algorithm.

class Solution:
Defines a class named Solution, which contains the method to solve the problem of minimizing the value 
derived from the frequencies of characters in a string.

def minValue(self, s, k):
Defines the method minValue inside the Solution class. It takes two parameters: s (the input string) and k (the number of characters to remove).

freq = Counter(s)
Counts the frequency of each character in the string s and stores the result in freq, which is a Counter object.

max_heap = [-count for count in freq.values()]
Initializes a list of negative frequencies from the freq values to simulate a max-heap. 
This is necessary because Python's heapq implements a min-heap by default.

heapq.heapify(max_heap)
Transforms the list max_heap into a heap, ensuring that the largest negative frequency is at the root.

while k > 0 and max_heap:
Starts a loop that continues as long as k is greater than 0 and the heap is not empty. 
This loop will perform k removals of the most frequent characters.

max_freq = heapq.heappop(max_heap)
Pops the largest (most negative) frequency from the heap. This represents the most frequent character in terms of positive frequency.

max_freq += 1
Increases max_freq by 1 (since it was stored as a negative value, this effectively decreases the frequency by 1).

k -= 1
Decreases k by 1, indicating that one removal has been performed.

if max_freq < 0:
Checks if the modified frequency is still negative, meaning that the character still has occurrences left after the removal.

heapq.heappush(max_heap, max_freq)
If the frequency is still valid (negative), it pushes the modified frequency back onto the heap.

result = 0
Initializes a variable result to store the sum of the squares of the remaining frequencies.

for freq in max_heap:
Starts a loop that iterates over each frequency in the max_heap.

result += freq ** 2
Squares each frequency (which is negative, so squaring it makes it positive) and adds it to result.

return result
Returns the final calculated value, which is the sum of the squares of the remaining frequencies after k removals.

Example Usage
sol = Solution()
Creates an instance of the Solution class.

print(sol.minValue("abccc", 1))
Calls the minValue method with the string "abccc" and k = 1. The expected output is 6, 
as removing one occurrence of 'c' results in the frequencies being 1 (a), 1 (b), and 2 (c), leading to 1^2 + 1^2 + 2^2 = 6.

print(sol.minValue("aabcbcbcabcc", 3))
Calls the minValue method with the string "aabcbcbcabcc" and k = 3. The expected output is 27,
which is derived from the frequencies after three removals.
'''
