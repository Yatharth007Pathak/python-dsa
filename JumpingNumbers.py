"""
Given a positive number X. Find the largest Jumping Number which is smaller than or equal to X. 
Jumping Number: A number is called Jumping Number if all adjacent digits in it differ by only 1. 
All single-digit numbers are considered as Jumping Numbers. For example 7, 8987 and 4343456 are Jumping numbers but 796, 677 and 89098 are not.

Example 1:
Input: X = 10
Output: 10
Explanation: 10 is the largest Jumping Number possible for X = 10.

Example 2:
Input: X = 50
Output: 45
Explanation: 45 is the largest Jumping Number possible for X = 50.
"""

from collections import deque

class Solution:
    def jumpingNums(self, X):
        # Edge case where X is a single digit number
        if X < 10:
            return X
        
        largest_jumping_num = 0
        
        # Initialize a queue for BFS with single-digit numbers
        queue = deque([i for i in range(1, 10)])  # start from 1 to 9
        
        while queue:
            # Get the front of the queue
            num = queue.popleft()
            
            # If num is less than or equal to X, update largest_jumping_num
            if num <= X:
                largest_jumping_num = max(largest_jumping_num, num)
                
                # Get the last digit of the current number
                last_digit = num % 10
                
                # Generate the next possible jumping numbers
                if last_digit > 0:  # We can append last_digit-1
                    next_num = num * 10 + (last_digit - 1)
                    if next_num <= X:
                        queue.append(next_num)
                
                if last_digit < 9:  # We can append last_digit+1
                    next_num = num * 10 + (last_digit + 1)
                    if next_num <= X:
                        queue.append(next_num)
        
        return largest_jumping_num

# Example usage
sol = Solution()
print(sol.jumpingNums(10))  # Output: 10
print(sol.jumpingNums(50))  # Output: 45

'''
Here is a line-by-line breakdown of the provided code:

from collections import deque
Imports deque from the collections module. deque is used to implement a double-ended queue, 
which allows efficient append and pop operations from both ends.

class Solution:
Defines a class named Solution, which will contain the method for solving the problem of finding the largest jumping number.

def jumpingNums(self, X):
Defines a method jumpingNums inside the Solution class. 
It takes X (a number) as input and aims to find the largest "jumping number" that is less than or equal to X.

if X < 10:
Checks if X is a single-digit number. Since all single-digit numbers are considered "jumping numbers", the largest such number is X itself.

return X
If X is less than 10, it simply returns X as the largest jumping number.

largest_jumping_num = 0
Initializes a variable largest_jumping_num to store the largest jumping number found so far. Initially set to 0.

queue = deque([i for i in range(1, 10)])
Initializes a queue (using deque) with the numbers 1 through 9, as these are the single-digit jumping numbers. 
They will be the starting points for finding larger jumping numbers.

while queue:
Starts a loop that continues as long as the queue is not empty. This loop performs a Breadth-First Search (BFS) to generate jumping numbers.

num = queue.popleft()
Removes and retrieves the number at the front of the queue. This number will be used to generate new jumping numbers.

if num <= X:
Checks if the current number (num) is less than or equal to X. Only such numbers can be considered valid jumping numbers.

largest_jumping_num = max(largest_jumping_num, num)
Updates largest_jumping_num if the current number num is larger than the previously stored largest_jumping_num.

last_digit = num % 10
Retrieves the last digit of the current number num using the modulus operator (%). 
The last digit will be used to generate the next possible jumping numbers.

if last_digit > 0:
Checks if the last digit is greater than 0. If true, it can append last_digit - 1 to form a new valid jumping number.

next_num = num * 10 + (last_digit - 1)
Creates a new number by appending last_digit - 1 to the current number. This forms the next possible jumping number.

if next_num <= X:
Checks if the newly formed number is less than or equal to X. If true, it is added to the queue for further processing.

queue.append(next_num)
Appends the new number to the queue so it can be processed in future iterations.

if last_digit < 9:
Checks if the last digit is less than 9. If true, it can append last_digit + 1 to form a new valid jumping number.

next_num = num * 10 + (last_digit + 1)
Creates a new number by appending last_digit + 1 to the current number.

if next_num <= X:
Checks if the newly formed number is less than or equal to X.

queue.append(next_num)
Appends the new number to the queue for further processing.

return largest_jumping_num
After the queue is empty and all possible jumping numbers have been processed, it returns the largest jumping number found.

Example usage
sol = Solution()
Creates an instance of the Solution class.

print(sol.jumpingNums(10))
Calls the jumpingNums method with X = 10 and prints the result. The largest jumping number less than or equal to 10 is 10.

print(sol.jumpingNums(50))
Calls the jumpingNums method with X = 50 and prints the result. The largest jumping number less than or equal to 50 is 45.
'''