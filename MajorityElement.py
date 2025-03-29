"""
Given an array arr. Find the majority element in the array. If no majority exists, return -1.
A majority element in an array is an element that appears strictly more than arr.size()/2 times in the array.

Examples:

Input: arr[] = [3, 1, 3, 3, 2]
Output: 3
Explanation: Since, 3 is present more than n/2 times, so it is the majority element.

Input: arr[] = [7]
Output: 7
Explanation: Since, 7 is single element and present more than n/2 times, so it is the majority element.

Input: arr[] = [2, 13]
Output: -1
Explanation: Since, no element is present more than n/2 times, so there is no majority element.
"""

class Solution:
    def majorityElement(self, arr):
        # Step 1: Use the Boyer-Moore Voting Algorithm to find a candidate for majority element
        candidate = None
        count = 0
        
        for num in arr:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        
        # Step 2: Verify if the candidate is actually the majority element
        if arr.count(candidate) > len(arr) // 2:
            return candidate
        else:
            return -1

# Example usage:
solution = Solution()
print(solution.majorityElement([3, 1, 3, 3, 2]))  # Output: 3
print(solution.majorityElement([7]))              # Output: 7
print(solution.majorityElement([2, 13]))          # Output: -1

'''
Let's break down the code line by line:

class Solution:
This line defines a class called Solution. In Python, classes are used to group related methods (functions) together.

def majorityElement(self, arr):
This line defines a method (function) named majorityElement within the Solution class. It takes two arguments: 
self (a reference to the instance of the class) and arr (an array of numbers).

candidate = None
This initializes the candidate variable to None. This variable will hold the potential majority element from the array.

count = 0
This initializes the count variable to 0. 
The count will be used to track how often the current candidate appears as the loop iterates through the array.

for num in arr:
This starts a loop that iterates over each number num in the array arr.

if count == 0:
This checks if count is zero. If it is, the code will set a new candidate.

candidate = num
If the count is zero, this line sets the current number num as the new candidate for the majority element.

count += 1 if num == candidate else -1
This line updates the count. If the current number num is the same as the current candidate, it increments the count by 1. 
Otherwise, it decrements the count by 1.

if arr.count(candidate) > len(arr) // 2:
This line checks if the candidate is actually the majority element. It does this by counting how many times the candidate appears in arr 
and comparing it to half the length of the array (len(arr) // 2). If the candidate appears more than half the time, it's the majority element.

return candidate
If the candidate is the majority element, this line returns it as the result.

else:
If the candidate is not the majority element, the code moves to this part.

return -1
This line returns -1 if no majority element is found, indicating that there is no valid majority element.

solution = Solution()
This line creates an instance of the Solution class and stores it in the variable solution.

print(solution.majorityElement([3, 1, 3, 3, 2]))
This line calls the majorityElement method on the array [3, 1, 3, 3, 2], which outputs 3, as 3 is the majority element in this array.

print(solution.majorityElement([7]))
This line calls the majorityElement method on the array [7]. The output is 7, as the single element is considered the majority.

print(solution.majorityElement([2, 13]))
This line calls the majorityElement method on the array [2, 13]. Since neither element appears more than half the time, it returns -1.
'''