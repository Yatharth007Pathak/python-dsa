"""
You are given a set of N types of rectangular 3-D boxes, where the ith box has height h, width w and length l. 
Your task is to create a stack of boxes which is as tall as possible, but you can only stack a box on top of another box 
if the dimensions of the 2-D base of the lower box are each strictly larger than those of the 2-D base of the higher box. 
Of course, you can rotate a box so that any side functions as its base.It is also allowable to use multiple instances of the same type of box. 
Your task is to complete the function maxHeight which returns the height of the highest possible stack so formed.

Note: 
Base of the lower box should be strictly larger than that of the new box we're going to place. 
This is in terms of both length and width, not just in terms of area. So, two boxes with same base cannot be placed one over the other.

Example 1:
Input: n = 4, height[] = {4,1,4,10}, width[] = {6,2,5,12}, length[] = {7,3,6,32}
Output: 60
Explanation: One way of placing the boxes is as follows in the bottom to top manner: (Denoting the boxes in (l, w, h) manner) 
(12, 32, 10) (10, 12, 32) (6, 7, 4) 
(5, 6, 4) (4, 5, 6) (2, 3, 1) (1, 2, 3)
Hence, the total height of this stack is 10 + 32 + 4 + 4 + 6 + 1 + 3 = 60.
No other combination of boxes produces a height greater than this.

Example 2:
Input: n = 3, height[] = {1,4,3}, width[] = {2,5,4}, length[] = {3,6,1}
Output: 15
Explanation: One way of placing the boxes is as follows in the bottom to top manner: (Denoting the boxes in (l, w, h) manner)
(5, 6, 4) (4, 5, 6) (3, 4, 1), (2, 3, 1) 
(1, 2, 3).
Hence, the total height of this stack is 4 + 6 + 1 + 1 + 3 = 15
No other combination of boxes produces a height greater than this.
"""

class Solution:
    def maxHeight(self, height, width, length, n):
        # Step 1: Generate all possible box rotations
        boxes = []
        for i in range(n):
            h, w, l = height[i], width[i], length[i]
            # All rotations of the current box
            boxes.append((max(w, l), min(w, l), h))  # Base: (w, l), Height: h
            boxes.append((max(h, l), min(h, l), w))  # Base: (h, l), Height: w
            boxes.append((max(w, h), min(w, h), l))  # Base: (w, h), Height: l

        # Step 2: Sort boxes by base area in descending order (length * width)
        boxes.sort(key=lambda x: x[0] * x[1], reverse=True)

        # Step 3: Initialize DP array to store the maximum height achievable with each box as the top box
        m = len(boxes)
        dp = [0] * m
        for i in range(m):
            dp[i] = boxes[i][2]  # The initial height is just the box's own height

        # Step 4: Build up the maximum stack height using DP
        for i in range(1, m):
            for j in range(i):
                # If box i can sit on box j
                if boxes[i][0] < boxes[j][0] and boxes[i][1] < boxes[j][1]:
                    dp[i] = max(dp[i], dp[j] + boxes[i][2])

        # Step 5: The answer is the maximum value in dp array
        return max(dp)

# Test cases
solution = Solution()

# Example 1
height1 = [4, 1, 4, 10]
width1 = [6, 2, 5, 12]
length1 = [7, 3, 6, 32]
print(solution.maxHeight(height1, width1, length1, len(height1)))  # Expected Output: 60

# Example 2
height2 = [1, 4, 3]
width2 = [2, 5, 4]
length2 = [3, 6, 1]
print(solution.maxHeight(height2, width2, length2, len(height2)))  # Expected Output: 15

'''
Here's a line-by-line breakdown of the maxHeight method:

Define maxHeight function: The goal is to find the maximum stack height of boxes by rotating and stacking them optimally.
Parameters:
height, width, length: lists of dimensions for each box.
n: total number of boxes.

Initialize boxes list: This list will store all rotations of each box.

Loop through each box: For each box with dimensions (height, width, length):

Get values h, w, and l for height[i], width[i], and length[i].

Generate all rotations: Append three rotations:
(max(w, l), min(w, l), h): Base is the larger of w and l, with height h.
(max(h, l), min(h, l), w): Base is the larger of h and l, with height w.
(max(w, h), min(w, h), l): Base is the larger of w and h, with height l.

Sort boxes by base area: Sort boxes in descending order of base area, calculated as length * width.

Initialize dp array: Create a DP array dp where dp[i] represents the maximum achievable height with boxes[i] as the top box.

Set initial heights in dp: Initialize each dp[i] with the height of boxes[i], which represents the height if the box stands alone.

Calculate maximum stack height using DP:
Nested loop through boxes: For each box i (starting from the second box):
Check each previous box j (from 0 to i-1).
Condition for stacking: If boxes[i] has a smaller base area (both length and width) than boxes[j].
Update dp[i]: If boxes[i] can sit on boxes[j], update dp[i] to max(dp[i], dp[j] + height[i]).

Return the result: The answer is the maximum value in the dp array, representing the tallest possible stack height.

Test Cases Explanation:
Test Case 1: For boxes with dimensions [4, 1, 4, 10] (height), [6, 2, 5, 12] (width), and [7, 3, 6, 32] (length), the expected output is 60.
Test Case 2: For dimensions [1, 4, 3] (height), [2, 5, 4] (width), and [3, 6, 1] (length), the expected output is 15.

This solution leverages dynamic programming and rotation permutations to maximize stack height by allowing flexibility in stacking rules.
'''