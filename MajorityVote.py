"""
You are given an array of integer nums[] where each number represents a vote to a candidate. 
Return the candidates that have votes greater than one-third of the total votes, If there's not a majority vote, return -1. 

Examples:

Input: nums = [2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]
Output: [5, 6]
Explanation: 5 and 6 occur more n/3 times.

Input: nums = [1, 2, 3, 4, 5]
Output: [-1]
Explanation: no candidate occur more than n/3 times.
"""

class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        n = len(arr)
        
        if n == 0:
            return -1
        
        # Step 1: Identifying candidates using Boyer-Moore Voting Algorithm
        candidate1, candidate2, count1, count2 = None, None, 0, 0
        
        for num in arr:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1
        
        # Step 2: Validation by counting the occurrences
        count1, count2 = 0, 0
        for num in arr:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
        
        # Prepare the result list
        result = []
        if count1 > n // 3:
            result.append(candidate1)
        if count2 > n // 3:
            result.append(candidate2)
        
        # Step 3: Return result in increasing order or -1 if no majority
        if result:
            return sorted(result)
        else:
            return [-1]

# Test cases
sol = Solution()

# Example 1
arr1 = [2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]
print(sol.findMajority(arr1))  # Output: [5, 6]

# Example 2
arr2 = [1, 2, 3, 4, 5]
print(sol.findMajority(arr2))  # Output: [-1]


'''
Here's a pointwise breakdown for each line of the code:

Class and Function Definition

class Solution:
Defines the class Solution which contains methods to solve problems related to arrays.

def findMajority(self, arr):
Defines the function findMajority within the class, which finds elements that appear more than n // 3 times in the array arr.

n = len(arr)
Calculates the length of the array and stores it in n.

if n == 0:
Checks if the array is empty.

return -1
If the array is empty, returns -1 indicating that there is no majority element.

Boyer-Moore Voting Algorithm (Candidate Identification)

candidate1, candidate2, count1, count2 = None, None, 0, 0
Initializes two candidates (candidate1 and candidate2) and their corresponding counts (count1 and count2) to None and 0, respectively. 
These will be used to track potential majority elements.

for num in arr:
Starts iterating through each number in the array.

if candidate1 == num:
If the current number num matches candidate1, increment count1.

count1 += 1
Increases the count for candidate1.

elif candidate2 == num:
If the current number num matches candidate2, increment count2.

count2 += 1
Increases the count for candidate2.

elif count1 == 0:
If count1 is zero, it means there is no active candidate1, so assign num to candidate1 and reset its count to 1.

candidate1, count1 = num, 1
Assigns the current number num as the new candidate1 and sets count1 to 1.

elif count2 == 0:
If count2 is zero, similarly assign num to candidate2 and set its count to 1.

candidate2, count2 = num, 1
Assigns the current number num as the new candidate2 and sets count2 to 1.

else:
If num does not match either candidate and both counts are non-zero, decrement both counts.

count1 -= 1
Decreases the count for candidate1.

count2 -= 1
Decreases the count for candidate2.

Validating the Candidates

count1, count2 = 0, 0
Resets both counts to zero to validate the actual occurrences of candidate1 and candidate2 in the array.

for num in arr:
Starts a loop to count the occurrences of candidate1 and candidate2 in the array.

if num == candidate1:
If num matches candidate1, increase count1.

count1 += 1
Increases the count for candidate1.

elif num == candidate2:
If num matches candidate2, increase count2.

count2 += 1
Increases the count for candidate2.

Preparing and Returning the Result

result = []
Initializes an empty list result to store the majority elements.

if count1 > n // 3:
Checks if candidate1 occurs more than n // 3 times. If true, add candidate1 to the result list.

result.append(candidate1)
Adds candidate1 to the result list if it satisfies the majority condition.

if count2 > n // 3:
Similarly, checks if candidate2 occurs more than n // 3 times.

result.append(candidate2)
Adds candidate2 to the result list if it satisfies the majority condition.

if result:
Checks if the result list is not empty (i.e., if there are majority elements).

return sorted(result)
Returns the sorted result list in increasing order.

else:
If there are no majority elements, return [-1].

return [-1]
Returns [-1] to indicate no majority element was found.

Testing the findMajority function
sol = Solution()
Creates an instance of the Solution class to call the findMajority method.

arr1 = [2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]
Defines the first test array arr1 with majority elements 5 and 6.

print(sol.findMajority(arr1))
Calls findMajority on arr1 and prints the result. Expected output: [5, 6].

arr2 = [1, 2, 3, 4, 5]
Defines the second test array arr2, where no element appears more than n // 3 times.

print(sol.findMajority(arr2))
Calls findMajority on arr2 and prints the result. Expected output: [-1].


Summary:
The algorithm uses the Boyer-Moore Voting Algorithm to identify two potential majority candidates.
It then validates these candidates by counting their occurrences in the array.
Finally, it returns the candidates that appear more than n // 3 times, or [-1] if no such element exists.
'''