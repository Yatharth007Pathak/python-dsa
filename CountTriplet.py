"""
Given an array Arr consisting of N distinct integers. 
The task is to count all the triplets such that sum of two elements equals the third element.
 
Example 1:
Input: N = 4, arr[] = {1, 5, 3, 2}
Output: 2 
Explanation: There are 2 triplets:  1 + 2 = 3 and 3 +2 = 5

Example 2:
Input: N = 3, arr[] = {2, 3, 4}
Output: 0
Explanation: No such triplet exits
"""

class Solution:
    def countTriplet(self, arr, n):
        # Sort the array
        arr.sort()
        count = 0
        
        # Start from the last element and look for pairs
        for k in range(n-1, 1, -1):
            i = 0
            j = k - 1
            # Use two-pointer technique to find pairs with sum arr[k]
            while i < j:
                if arr[i] + arr[j] == arr[k]:
                    count += 1
                    i += 1
                    j -= 1
                elif arr[i] + arr[j] < arr[k]:
                    i += 1
                else:
                    j -= 1
                    
        return count

# Example usage:
sol = Solution()

# Test case 1
arr1 = [1, 5, 3, 2]
n1 = len(arr1)
print(sol.countTriplet(arr1, n1))  # Output: 2

# Test case 2
arr2 = [2, 3, 4]
n2 = len(arr2)
print(sol.countTriplet(arr2, n2))  # Output: 0


'''
This method uses sorting and a two-pointer approach to efficiently count triplets where the sum of two numbers equals the third number. 
The time complexity is O(n^2) due to the nested loops after sorting the array.


Here's a line-by-line breakdown of the countTriplet method, 
which counts how many triplets in the array satisfy the condition where the sum of two numbers equals a third number.

class Solution:
Defines the Solution class that contains the method countTriplet.

def countTriplet(self, arr, n):
Defines the method countTriplet, which takes two arguments:
arr: the input list of integers.
n: the length of the array.

arr.sort()
Sorts the array in non-decreasing order. Sorting helps to use the two-pointer technique efficiently.

count = 0
Initializes a variable count to 0, which will store the number of triplets found.

for k in range(n-1, 1, -1):
A for loop iterates over the array in reverse order starting from the last index (n-1) down to 2. 
Here, arr[k] is considered as the third number of the triplet.

i = 0
Initializes the pointer i to 0, representing the start of the array. This will be the index of the first element of the triplet.

j = k - 1
Initializes the pointer j to k - 1, which represents the second element of the triplet. The j pointer will move from k-1 toward i.

while i < j:
A while loop runs as long as i is less than j. The loop looks for two elements (arr[i] and arr[j]) whose sum equals arr[k].

if arr[i] + arr[j] == arr[k]:
If the sum of arr[i] and arr[j] equals arr[k], a valid triplet has been found.

count += 1
Increments count by 1 since a valid triplet has been found.

i += 1 and j -= 1
Moves both pointers inward, i.e., increases i and decreases j, to continue looking for more pairs in the same loop.

elif arr[i] + arr[j] < arr[k]:
If the sum of arr[i] and arr[j] is less than arr[k], it means i needs to move to a larger element to potentially find a match.

i += 1
Moves the i pointer to the right to consider a larger element.

else:
If the sum of arr[i] and arr[j] is greater than arr[k], the j pointer is moved left to consider a smaller element.

j -= 1
Moves the j pointer to the left to try and reduce the sum.

return count
After the loops complete, the method returns the total count of valid triplets.

sol = Solution()
Creates an instance of the Solution class.

arr1 = [1, 5, 3, 2]
Defines the first test case where the input array is [1, 5, 3, 2].

n1 = len(arr1)
Gets the length of the array arr1.

print(sol.countTriplet(arr1, n1)) # Output: 2
Calls countTriplet on the array arr1, which outputs 2 because there are two valid triplets: (1, 2, 3) and (3, 2, 5).

arr2 = [2, 3, 4]
Defines the second test case with array [2, 3, 4].

n2 = len(arr2)
Gets the length of the array arr2.

print(sol.countTriplet(arr2, n2)) # Output: 0
Calls countTriplet on arr2, which outputs 0 since no valid triplets are present.
'''