"""
In Doraland, people have unique Identity Numbers called D-id. Doraemon owns the most popular gadget shop in Doraland. 
Since his gadgets are in high demand and he has only K gadgets left he has decided to sell his gadgets to his most frequent customers only. 
N customers visit his shop and D-id of each customer is given in an array array[ ]. 
In case two or more people have visited his shop the same number of time he gives priority to the customer with higher D-id. 
Find the D-ids of people he sells his K gadgets to.

Example 1:
Input: N = 6, array[] = {1, 1, 1, 2, 2, 3}, K = 2
Output: 1 2
Explanation: Customers with D-id 1 and 2 are most frequent.

Example 2:
Input: N = 8, array[] = {1, 1, 2, 2, 3, 3, 3, 4}, K = 2
Output: 3 2
Explanation: People with D-id 1 and 2 have visited shop 2 times Therefore, in this case, the answer includes the D-id 2 as 2 > 1.
"""

from collections import Counter

class Solution:
    def TopK(self, array, k):
        # Count frequencies of each D-id
        freq = Counter(array)
        
        # Sort by frequency (desc) and D-id (desc for ties in frequency)
        sorted_ids = sorted(freq.items(), key=lambda x: (-x[1], -x[0]))
        
        # Extract top K D-ids
        top_k = [d_id for d_id, _ in sorted_ids[:k]]
        return top_k

solution = Solution()

# Example 1
N = 6
array = [1, 1, 1, 2, 2, 3]
K = 2
print(solution.TopK(array, K))  # Output: [1, 2]

# Example 2
N = 8
array = [1, 1, 2, 2, 3, 3, 3, 4]
K = 2
print(solution.TopK(array, K))  # Output: [3, 2]

# Example 3
N = 7
array = [5, 5, 6, 6, 6, 7, 7]
K = 1
print(solution.TopK(array, K))  # Output: [6]

'''
Here's a detailed breakdown of the code:

Code Functionality:
The program identifies the top K most frequent elements (D-ids) from a given list, resolving ties in frequency by selecting larger D-ids.

Explanation of the Code:

from collections import Counter
Imports the Counter class from the collections module to efficiently count the frequency of elements in the array.

class Solution:
Defines a class named Solution containing the method TopK.

def TopK(self, array, k):
Defines the method TopK that takes an array and an integer k as inputs to determine the top k elements based on frequency and value.

freq = Counter(array)
Uses Counter to count the occurrences of each element in the array.
Stores the result in a dictionary-like structure where keys are elements and values are their counts.

sorted_ids = sorted(freq.items(), key=lambda x: (-x[1], -x[0]))
Converts the frequency dictionary into a list of tuples (element, count).

Sorts the list by:
Descending order of frequency: -x[1] ensures elements with higher counts come first.
Descending order of D-id (if counts are the same): -x[0] ensures larger D-ids are prioritized in case of ties.

top_k = [d_id for d_id, _ in sorted_ids[:k]]
Extracts the first k elements from the sorted list of tuples.
Retrieves only the D-ids (ignores their counts).

return top_k
Returns the list of top k D-ids.

Example 1:
Input: N = 6, array = [1, 1, 1, 2, 2, 3], K = 2
Step-by-Step:
Frequency: {1: 3, 2: 2, 3: 1}
Sorted: [(1, 3), (2, 2), (3, 1)]
Top 2 D-ids: [1, 2]
Output: [1, 2]

Example 2:
Input: N = 8, array = [1, 1, 2, 2, 3, 3, 3, 4], K = 2
Step-by-Step:
Frequency: {1: 2, 2: 2, 3: 3, 4: 1}
Sorted: [(3, 3), (2, 2), (1, 2), (4, 1)]
Top 2 D-ids: [3, 2]
Output: [3, 2]

Example 3:
Input: N = 7, array = [5, 5, 6, 6, 6, 7, 7], K = 1
Step-by-Step:
Frequency: {5: 2, 6: 3, 7: 2}
Sorted: [(6, 3), (7, 2), (5, 2)]
Top 1 D-id: [6]
Output: [6]

Summary:
The code efficiently computes the top K most frequent elements with tie-breaking rules using the 
Counter class and custom sorting with a lambda function.
'''