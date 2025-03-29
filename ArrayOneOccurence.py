"""
Given a sorted array arr[] of n positive integers having all the numbers occurring exactly twice, 
except for one number which will occur only once. Find the number occurring only once.

Examples :

Input: n = 5, arr[] = {1, 1, 2, 5, 5}
Output: 2
Explanation: Since 2 occurs once, while other numbers occur twice, 2 is the answer.

Input: n = 7, arr[] = {2, 2, 5, 5, 20, 30, 30}
Output: 20
Explanation: Since 20 occurs once, while other numbers occur twice, 20 is the answer.
"""

class Solution:
    def search(self, n, arr):
        result = 0
        
        # XOR all elements in the array
        for num in arr:
            result ^= num
            
        return result

# Example usage:
solution = Solution()
print(solution.search(5, [1, 1, 2, 5, 5]))  # Output: 2
print(solution.search(7, [2, 2, 5, 5, 20, 30, 30]))  # Output: 20

'''
Here's a line-by-line breakdown of the code:

class Solution:
Defines a class named Solution containing a method to find the element that appears 
only once in an array where every other element appears twice.

def search(self, n, arr):
Defines a method search within the Solution class. It takes three parameters: 
self (instance of the class), n (the number of elements in the array), and arr (the list of numbers).

result = 0
Initializes a variable result to zero. This variable will store the result of XOR-ing all elements in the array.

for num in arr:
Begins a loop to iterate over each element (num) in the array arr.

result ^= num
Applies the XOR operation between result and num, updating result. Since XOR-ing a number with itself results in 0 
and XOR-ing with 0 results in the number itself, pairs of identical numbers cancel each other out, leaving only the unique number in result.

return result
Returns result, which now holds the unique element in the array that appears only once.

Example Usage:
solution = Solution()
Creates an instance of the Solution class named solution.

print(solution.search(5, [1, 1, 2, 5, 5])) # Output: 2
Calls search on an array where the unique number is 2 and prints the result. The expected output is 2.

print(solution.search(7, [2, 2, 5, 5, 20, 30, 30])) # Output: 20
Calls search on another array where the unique number is 20 and prints the result. The expected output is 20.
'''