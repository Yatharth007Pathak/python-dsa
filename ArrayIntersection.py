"""
Given two arrays a[] and b[] respectively of size n and m, the task is to print the count of elements in the 
intersection (or common elements) of the two arrays.
For this question, the intersection of two arrays can be defined as the set containing distinct common elements between the two arrays. 

Example 1:
Input: n = 5, m = 3, a[] = {89, 24, 75, 11, 23}, b[] = {89, 2, 4}
Output: 1
Explanation: 89 is the only element in the intersection of two arrays. 

Example 2:
Input: n = 6, m = 5, a[] = {1, 2, 3, 4, 5, 6}, b[] = {3, 4, 5, 6, 7} 
Output: 4
Explanation: 3 4 5 and 6 are the elements in the intersection of two arrays.
"""

class Solution:
    def NumberofElementsInIntersection(self, a, b, n, m):
        # Convert both lists to sets to remove duplicates
        set_a = set(a)
        set_b = set(b)
        
        # Find the intersection of the two sets
        intersection = set_a.intersection(set_b)
        
        # Return the count of distinct common elements
        return len(intersection)

# Test cases
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    n1, m1 = 5, 3
    a1 = [89, 24, 75, 11, 23]
    b1 = [89, 2, 4]
    result1 = sol.NumberofElementsInIntersection(a1, b1, n1, m1)
    print(f"Output for a1 = {a1} and b1 = {b1}: {result1}")  # Output should be 1

    # Test case 2
    n2, m2 = 6, 5
    a2 = [1, 2, 3, 4, 5, 6]
    b2 = [3, 4, 5, 6, 7]
    result2 = sol.NumberofElementsInIntersection(a2, b2, n2, m2)
    print(f"Output for a2 = {a2} and b2 = {b2}: {result2}")  # Output should be 4

'''
Here's a detailed breakdown of the NumberofElementsInIntersection method:

Function Definition

class Solution:
Defines the Solution class, which contains the method NumberofElementsInIntersection.

def NumberofElementsInIntersection(self, a, b, n, m):
This method takes in two lists, a and b, along with their respective sizes n and m. 
It calculates the number of distinct elements that appear in both lists.

Logic Implementation

set_a = set(a)
Converts list a into a set called set_a. This automatically removes any duplicate values from a, as sets can only contain unique elements.

set_b = set(b)
Converts list b into a set called set_b, also removing any duplicates.

intersection = set_a.intersection(set_b)
Calculates the intersection of set_a and set_b, which results in a new set containing only the elements that are present in both sets.

return len(intersection)
Returns the number of distinct common elements by calculating the length of the intersection set.

Test Cases

if __name__ == "__main__":
This block allows the test cases to run only if the script is executed directly.

Test case 1
n1, m1 = 5, 3: Specifies the sizes of the first input lists.
a1 = [89, 24, 75, 11, 23]: The first list.
b1 = [89, 2, 4]: The second list.
result1 = sol.NumberofElementsInIntersection(a1, b1, n1, m1): Calls the method to find the number of common elements.
print(f"Output for a1 = {a1} and b1 = {b1}: {result1}"): Prints the output for the first test case.

Test case 2
n2, m2 = 6, 5: Specifies the sizes of the second input lists.
a2 = [1, 2, 3, 4, 5, 6]: The first list.
b2 = [3, 4, 5, 6, 7]: The second list.
result2 = sol.NumberofElementsInIntersection(a2, b2, n2, m2): Calls the method for the second test case.
print(f"Output for a2 = {a2} and b2 = {b2}: {result2}"): Prints the output for the second test case.

Example Outputs
For a1 = [89, 24, 75, 11, 23] and b1 = [89, 2, 4], the output will be 1 because 89 is the only common element.
For a2 = [1, 2, 3, 4, 5, 6] and b2 = [3, 4, 5, 6, 7], the output will be 4 because the common elements are 3, 4, 5, and 6.

Time Complexity
The time complexity of this method is O(n + m), where n is the number of elements in list a and m is the number of elements in list b. 
This accounts for the time to convert both lists to sets and then find their intersection.
'''