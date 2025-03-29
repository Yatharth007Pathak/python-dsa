"""
Given coordinates of four points in a plane. Find if the four points form a square or not.

Example 1:
Input: points=(0,0),(0,1),(1,0),(1,1)
Output: 1
Explanation: These points form a square. 

Example 2:
Input: points=(0,0),(1,1),(1,0),(0,2)
Output: 0
Explanation: These four points do not form a square.
"""

class Solution:
    def distance(self, p1, p2):
        # Squared distance to avoid floating point precision issues
        return (p2[0] - p1[0])**2 + (p2[1] - p1[1])**2
    
    def fourPointSquare(self, points):
        # There are 6 pairwise distances between 4 points
        dists = []
        
        # Get all the points
        p1, p2, p3, p4 = points
        
        # Calculate squared distances between all pairs of points
        dists.append(self.distance(p1, p2))
        dists.append(self.distance(p1, p3))
        dists.append(self.distance(p1, p4))
        dists.append(self.distance(p2, p3))
        dists.append(self.distance(p2, p4))
        dists.append(self.distance(p3, p4))
        
        # Sort the distances
        dists.sort()
        
        # A square must have 4 equal sides and 2 equal diagonals
        # So, the first 4 distances should be equal and the last 2 should be equal
        # And the diagonal should be longer than the sides
        return 1 if dists[0] > 0 and dists[0] == dists[1] == dists[2] == dists[3] and dists[4] == dists[5] and dists[4] > dists[0] else 0

# Example usage
sol = Solution()

points1 = [(0, 0), (0, 1), (1, 0), (1, 1)]
print(sol.fourPointSquare(points1))  # Output: 1 (These points form a square)

points2 = [(0, 0), (1, 1), (1, 0), (0, 2)]
print(sol.fourPointSquare(points2))  # Output: 0 (These points do not form a square)

'''
Here is the line-by-line breakdown of the code in pointwise format:

Class Definition:
The class Solution is defined, containing two methods: 
distance to calculate the squared distance between two points and fourPointSquare to check if four given points form a square.

distance Method:
This method calculates the squared distance between 2 points p1 and p2 to avoid floating point precision issues when working with square roots.

Squared Distance Calculation:
The squared distance between two points p1(x1, y1) and p2(x2, y2) is calculated using the formula:

squared_distance = (x2 - x1)^2 + (y2 - y1)^2
The method returns the squared distance.

fourPointSquare Method:
This method takes a list of four points and determines whether they form a square.

Initialize List for Distances:
A list dists is initialized to store the squared distances between all pairs of points.

Unpacking Points:
The four points are unpacked as p1, p2, p3, and p4 from the points list.

Calculate Pairwise Distances:
The distance method is called for each pair of points, and their squared distances are appended to the dists list.
Pairs: (p1, p2), (p1, p3), (p1, p4), (p2, p3), (p2, p4), (p3, p4).

Sort the Distances:
The distances are sorted in ascending order to easily compare the sides and diagonals of the potential square.

Condition to Check Square:
A square must satisfy the following conditions:
The first four sorted distances (representing sides) should be equal.
The last two sorted distances (representing diagonals) should be equal.
The diagonal's length should be greater than the side's length.
The method returns 1 if these conditions are met, indicating the points form a square; otherwise, it returns 0.

Example Usage:
An instance of the Solution class is created using sol = Solution().

Test Case 1:
The fourPointSquare method is called with points1 = [(0, 0), (0, 1), (1, 0), (1, 1)].
The squared distances between the points are [1, 1, 1, 1, 2, 2]. These distances satisfy the square conditions.
The output is 1, indicating that the points form a square.

Test Case 2:
The fourPointSquare method is called with points2 = [(0, 0), (1, 1), (1, 0), (0, 2)].
The squared distances between the points are [1, 1, 2, 2, 5, 5]. These distances do not satisfy the square conditions.
The output is 0, indicating that the points do not form a square.
'''