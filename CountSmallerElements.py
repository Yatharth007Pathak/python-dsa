"""
Given an array arr containing non-negative integers. Count and return an array ans where ans[i] denotes the number of 
smaller elements on right side of arr[i].

Examples:

Input: arr[] = [12, 1, 2, 3, 0, 11, 4]
Output: [6, 1, 1, 1, 0, 1, 0]
Explanation: There are 6 smaller elements right after 12. There is 1 smaller element right after 1. And so on.

Input: arr[] = [1, 2, 3, 4, 5]
Output: [0, 0, 0, 0, 0]
Explanation: There are 0 smaller elements right after 1. There are 0 smaller elements right after 2. And so on.
"""

class Solution:
    def constructLowerArray(self, arr):
        # Coordinate compression to handle large range of numbers
        sorted_arr = sorted(set(arr))
        rank_map = {val: idx + 1 for idx, val in enumerate(sorted_arr)}
        
        # Fenwick Tree (BIT) for range queries
        def update(bit, idx, value, n):
            while idx <= n:
                bit[idx] += value
                idx += idx & -idx
        
        def query(bit, idx):
            sum_val = 0
            while idx > 0:
                sum_val += bit[idx]
                idx -= idx & -idx
            return sum_val
        
        # Initialize Fenwick Tree
        n = len(arr)
        bit = [0] * (len(sorted_arr) + 1)
        ans = [0] * n
        
        # Traverse from right to left
        for i in range(n - 1, -1, -1):
            rank = rank_map[arr[i]]
            ans[i] = query(bit, rank - 1)
            update(bit, rank, 1, len(sorted_arr))
        
        return ans

sol = Solution()

arr = [12, 1, 2, 3, 0, 11, 4]
print(sol.constructLowerArray(arr))  # Output: [6, 1, 1, 1, 0, 1, 0]

arr = [1, 2, 3, 4, 5]
print(sol.constructLowerArray(arr))  # Output: [0, 0, 0, 0, 0]

arr = [5, 4, 3, 2, 1]
print(sol.constructLowerArray(arr))  # Output: [4, 3, 2, 1, 0]

'''
Here's a line-by-line breakdown of the code:

class Solution:
Defines a class named Solution.

def constructLowerArray(self, arr):
Defines a method constructLowerArray in the Solution class. It takes a list arr as input and calculates, 
for each element in the array, how many smaller elements are to its right.

Coordinate Compression
sorted_arr = sorted(set(arr))
Creates a sorted list of unique values from arr. This is done to compress the range of numbers for efficient processing using the Fenwick Tree.

rank_map = {val: idx + 1 for idx, val in enumerate(sorted_arr)}
Assigns a rank to each unique value in arr based on its position in sorted_arr. Each value maps to an index starting from 1.

Fenwick Tree (BIT) Utility Functions
def update(bit, idx, value, n):
Defines a function to update the Fenwick Tree (bit array). 
This function adds value to the Fenwick Tree at index idx and updates all relevant positions.

while idx <= n:
Keeps updating the Fenwick Tree as long as the index idx is within bounds.

bit[idx] += value
Adds value to the current index of the Fenwick Tree.

idx += idx & -idx
Moves to the next index that needs to be updated, based on the binary representation of idx.

def query(bit, idx):
Defines a function to query the cumulative sum from the Fenwick Tree up to index idx.

sum_val = 0
Initializes a variable to store the cumulative sum.

while idx > 0:
Loops while the index is greater than 0.

sum_val += bit[idx]
Adds the value at the current index of the Fenwick Tree to sum_val.

idx -= idx & -idx
Moves to the parent index in the Fenwick Tree.

return sum_val
Returns the cumulative sum up to the specified index.

Main Algorithm
n = len(arr)
Stores the length of the input array arr.

bit = [0] * (len(sorted_arr) + 1)
Initializes a Fenwick Tree (bit array) with zeros. Its size is one more than the number of unique values in arr.

ans = [0] * n
Initializes the result array ans with zeros.

for i in range(n - 1, -1, -1):
Traverses the input array arr from right to left.

rank = rank_map[arr[i]]
Gets the rank of the current element in arr using the rank_map.

ans[i] = query(bit, rank - 1)
Queries the Fenwick Tree to count how many elements with ranks less than rank have been seen so far (i.e., elements smaller than arr[i]).

update(bit, rank, 1, len(sorted_arr))
Updates the Fenwick Tree to include the current element's rank. Adds 1 to the tree at the position corresponding to rank.

return ans
After processing all elements, returns the ans array, which contains the count of smaller elements to the right for each element in arr.
Example Usage
sol = Solution()
Creates an instance of the Solution class.

arr = [12, 1, 2, 3, 0, 11, 4]
Defines the first test case input.

print(sol.constructLowerArray(arr))
Prints the output for the first test case: [6, 1, 1, 1, 0, 1, 0].

arr = [1, 2, 3, 4, 5]
Defines the second test case input.

print(sol.constructLowerArray(arr))
Prints the output for the second test case: [0, 0, 0, 0, 0].

arr = [5, 4, 3, 2, 1]
Defines the third test case input.

print(sol.constructLowerArray(arr))
Prints the output for the third test case: [4, 3, 2, 1, 0].
'''