"""
Geek is organizing a birthday party, so his friends brought a cake for him. The cake consists of N chunks, whose individual sweetness 
is represented by the sweetness array. Now at the time of distribution, Geek cuts the cake into K + 1 pieces 
to distribute among his K friends. One piece he took for himself. Each piece consists of some consecutive chunks. 
He is very kind, so he left the piece with minimum sweetness for him.

You need to find the maximum sweetness that the Geek can get if he distributes the cake optimally.

Example 1:
Input: N  = 6, K = 2, sweetness[] = {6, 3, 2, 8, 7, 5}
Output: 9
Explanation: Geek can divide the cake to [6, 3], [2, 8], [7, 5] with sweetness level 9, 10 and 12 respectively.

Example 2:
Input: N  = 7, K = 3, sweetness[] = {1, 2, 4, 7, 3, 6, 9}
Output: 7
Explanation: Geek can divide the cake to [1, 2, 4], [7], [3, 6], [9] with sweetness level 7, 7, 9 and 9 respectively.
"""

class Solution:
    def maxSweetness(self, sweetness, n, k):
        def canDivide(minSweetness):
            pieces = 0
            currentSweetness = 0
            for sweet in sweetness:
                currentSweetness += sweet
                if currentSweetness >= minSweetness:
                    pieces += 1
                    currentSweetness = 0
            return pieces >= k + 1

        # Binary search
        left, right = 1, sum(sweetness) // (k + 1)
        result = 1
        while left <= right:
            mid = (left + right) // 2
            if canDivide(mid):
                result = mid
                left = mid + 1  # Try for higher sweetness
            else:
                right = mid - 1  # Reduce sweetness
        return result


# Driver code
if __name__ == "__main__":
    # Input
    N = int(input("Enter the number of chunks (N): "))
    K = int(input("Enter the number of friends (K): "))
    sweetness = list(map(int, input("Enter the sweetness array: ").split()))
    
    # Create a solution object
    solution = Solution()
    
    # Get the result
    result = solution.maxSweetness(sweetness, N, K)
    
    # Output the result
    print(f"The maximum sweetness Geek can get is: {result}")

'''
Here's a breakdown of the code:

Function Definition
class Solution:
Defines a class named Solution that contains the method maxSweetness.

def maxSweetness(self, sweetness, n, k):
A method to determine the maximum minimum sweetness Geek can get when dividing the chocolate.

Helper Function: canDivide
def canDivide(minSweetness):
Helper function to check if the chocolate can be divided into at least k + 1 pieces with each piece having a sweetness of at least minSweetness.

pieces = 0
Initializes a counter to track the number of valid pieces.

currentSweetness = 0
Tracks the accumulated sweetness of the current piece.

for sweet in sweetness:
Loops through the sweetness values of the chunks.

currentSweetness += sweet
Adds the sweetness of the current chunk to the current piece.

if currentSweetness >= minSweetness:
If the accumulated sweetness meets or exceeds minSweetness:

pieces += 1
Increases the count of valid pieces.

currentSweetness = 0
Resets the current sweetness for the next piece.

return pieces >= k + 1
Returns True if the number of pieces is at least k + 1, otherwise False.

Binary Search Implementation
left, right = 1, sum(sweetness) // (k + 1)
Initializes the binary search range.

left starts at 1 (minimum sweetness possible).
right is the maximum average sweetness achievable for k + 1 pieces.
result = 1
Initializes the result to store the maximum minimum sweetness found.

while left <= right:
Continues binary search until the range is exhausted.

mid = (left + right) // 2
Calculates the mid-point of the current range.

if canDivide(mid):
Checks if it is possible to divide the chocolate with a minimum sweetness of mid.

result = mid
Updates result to the current mid-point (valid sweetness).

left = mid + 1
Tries for higher sweetness values by moving the lower bound up.

else:
If it is not possible to divide with the current mid value:

right = mid - 1
Reduces the upper bound to try for lower sweetness values.

return result
Returns the maximum minimum sweetness Geek can get.

Driver Code
if __name__ == "__main__":
Checks if the script is being run directly.

N = int(input("Enter the number of chunks (N): "))
Reads the total number of chocolate chunks as input.

K = int(input("Enter the number of friends (K): "))
Reads the number of friends.

sweetness = list(map(int, input("Enter the sweetness array: ").split()))
Reads the sweetness array as a list of integers.

solution = Solution()
Creates an instance of the Solution class.

result = solution.maxSweetness(sweetness, N, K)
Calls the maxSweetness method with the inputs and stores the result.

print(f"The maximum sweetness Geek can get is: {result}")
Outputs the maximum minimum sweetness Geek can get.
'''