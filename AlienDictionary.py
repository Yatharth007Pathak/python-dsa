"""
Given a sorted dictionary of an alien language having N words and k starting alphabets of standard dictionary. 
Find the order of characters in the alien language.
Note: Many orders may be possible for a particular test case, thus you may return any valid order and output will be 1 
if the order of string returned by the function is correct else 0 denoting incorrect string returned.

Examples :

Input:  n = 5, k = 4, dict = {"baa","abcd","abca","cab","cad"}
Output: 1
Explanation: Here order of characters is 'b', 'd', 'a', 'c' Note that words are sorted and in the given language "baa" comes before "abcd", 
therefore 'b' is before 'a' in output. Similarly we can find other orders.

Input: n = 3, k = 3, dict = {"caa","aaa","aab"}
Output: 1
Explanation: Here order of characters is 'c', 'a', 'b' Note that words are sorted and in the given language "caa" comes before "aaa", 
therefore 'c' is before 'a' in output. Similarly we can find other orders.
"""

from collections import defaultdict, deque
from typing import List

class Solution:
    def findOrder(self, dict: List[str], n: int, k: int) -> str:
        # Step 1: Create a graph and a in-degree count
        graph = defaultdict(set)
        in_degree = {chr(i): 0 for i in range(ord('a'), ord('a') + k)}

        # Step 2: Build the graph
        for i in range(n - 1):
            word1 = dict[i]
            word2 = dict[i + 1]
            min_length = min(len(word1), len(word2))
            for j in range(min_length):
                if word1[j] != word2[j]:
                    if word2[j] not in graph[word1[j]]:
                        graph[word1[j]].add(word2[j])
                        in_degree[word2[j]] += 1
                    break

        # Step 3: Topological Sort using Kahn's Algorithm
        # Queue for characters with no incoming edges
        queue = deque([char for char in in_degree if in_degree[char] == 0])
        order = []

        while queue:
            char = queue.popleft()
            order.append(char)
            for neighbor in graph[char]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        # Step 4: Check if we have a valid order
        if len(order) == len(in_degree):
            return ''.join(order)
        else:
            return ""  # return empty if there's a cycle or not all characters are included

# Example usage
sol = Solution()
print(sol.findOrder(["baa", "abcd", "abca", "cab", "cad"], 5, 4))  # Output: 'bdac' or any valid order
print(sol.findOrder(["caa", "aaa", "aab"], 3, 3))                  # Output: 'cab' or any valid order

'''
The findOrder method constructs a directed graph to represent character precedence based on the provided list of words. 
It then performs a topological sort using Kahn's algorithm to determine a valid character order in the alien language. 
If a valid order exists, it returns it as a string; otherwise, it returns an empty string.


Code Breakdown

from collections import defaultdict, deque
This line imports defaultdict and deque from the collections module.
defaultdict allows us to create dictionaries with default values, while deque provides an efficient double-ended queue implementation.

from typing import List
This imports the List type from the typing module, enabling us to specify that the function will accept a list of strings.

class Solution:
This defines a class named Solution, which encapsulates the functionality of the method findOrder.

def findOrder(self, dict: List[str], n: int, k: int) -> str:
This defines a method findOrder that takes three parameters:
dict: a list of strings representing the words in the alien language.
n: the number of words in the list.
k: the number of unique characters in the alien language.
The method returns a string representing the correct order of characters.

# Step 1: Create a graph and a in-degree count
This comment describes the purpose of the next lines, which set up the data structures needed for the algorithm.

graph = defaultdict(set)
This line initializes a directed graph using defaultdict where each character points to a set of characters that it precedes.

in_degree = {chr(i): 0 for i in range(ord('a'), ord('a') + k)}
This creates a dictionary that tracks the in-degree (number of incoming edges) for each character.
chr(i) generates characters from 'a' to the k-th character (e.g., if k=4, it generates 'a', 'b', 'c', 'd').

# Step 2: Build the graph
This comment indicates that the next block of code will construct the graph based on the word list.

for i in range(n - 1):
This loop iterates through the list of words, comparing each word with the next one.

word1 = dict[i]
This assigns the current word to word1.

word2 = dict[i + 1]
This assigns the next word to word2.

min_length = min(len(word1), len(word2))
This calculates the length of the shorter word between word1 and word2 to avoid index out-of-bounds errors during comparison.

for j in range(min_length):
This inner loop iterates through the characters of the two words up to the length of the shorter word.

if word1[j] != word2[j]:
This checks if the characters at the same position in both words are different.

if word2[j] not in graph[word1[j]]:
This checks if there is already a directed edge from word1[j] to word2[j].

graph[word1[j]].add(word2[j])
This adds a directed edge from word1[j] to word2[j], indicating that word1[j] precedes word2[j] in the alien language.

in_degree[word2[j]] += 1
This increments the in-degree of word2[j] since it has a new incoming edge from word1[j].

break
This breaks out of the loop after processing the first differing characters, as we only need the first difference to determine the order.

# Step 3: Topological Sort using Kahn's Algorithm
This comment indicates the beginning of the topological sorting process.

queue = deque([char for char in in_degree if in_degree[char] == 0])
This initializes a deque (double-ended queue) with characters that have an in-degree of 0, meaning they have no prerequisites.

order = []
This creates an empty list order to store the topological ordering of characters.

while queue:
This loop continues as long as there are characters in the queue.

char = queue.popleft()
This removes and returns the leftmost character from the queue.

order.append(char)
This adds the character to the order list.

for neighbor in graph[char]:
This iterates through the neighbors (characters that come after char) in the graph.

in_degree[neighbor] -= 1
This decrements the in-degree of each neighbor since we are processing char.

if in_degree[neighbor] == 0:
This checks if the in-degree of the neighbor has become 0, meaning it has no more prerequisites.

queue.append(neighbor)
If the in-degree of the neighbor is now 0, it is added to the queue for processing.

# Step 4: Check if we have a valid order
This comment indicates that we will now check if a valid ordering was found.

if len(order) == len(in_degree):
This checks if the length of the order list matches the number of unique characters (in-degree entries). 
If they are equal, it means a valid order exists.

return ''.join(order)
If a valid order is found, the method returns the characters in order concatenated into a single string.

else:
This line begins the alternative case when the order is not valid.

return ""
If a valid order cannot be formed (indicating a cycle or missing characters), the method returns an empty string.

sol = Solution()
Creates an instance of the Solution class.

print(sol.findOrder(["baa", "abcd", "abca", "cab", "cad"], 5, 4))
Calls the findOrder method with a sample list of words. 
The expected output could be 'bdac' or any valid order based on the constraints of the given words.

print(sol.findOrder(["caa", "aaa", "aab"], 3, 3))
Calls the findOrder method again with a different list of words. The expected output could be 'cab' or any valid order.
'''