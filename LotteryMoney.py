"""
There is a game "Choose a number and win money", in which, a person playing a game has to select a number N and 
he/she will be awarded some money in Rupees accordingly. Some of the observations of selecting a number N and money awarded(M) are:-
N: 1   2   3   4   5   6   7   8   9   10   11   12   13   14   15   16   17   18   19   20   21   22   23   24 ..........
M: 3   2   1   6   5   4   3   2   1   12   11   10   9     8     7      6      5     4     3    2     1    24  23  22...............
i.e. if you selects a number N=1,she gets M=Rs 3,if N=2,M=Rs 2,if N=3 ,M=Rs 1 and so on..

Example 1:
Input: N = 30
Output: 16
Explanation: As per the distribution, you earn Rs 16.
"""

class Solution:
    def totalMoney (ob,N):
        sum=3
        while sum<N:
            sum=sum*2 + 3
        return sum+1-N

solution = Solution()
print(solution.totalMoney(30))  # Output: 16
print(solution.totalMoney(1))   # Output: 3

'''
Code Explanation:

class Solution:
Defines the Solution class, which contains the method totalMoney.

def totalMoney(ob, N):
Defines the method totalMoney inside the Solution class. It takes two parameters:
ob: A reference to the instance of the class (self).
N: The target value to calculate against.

sum = 3
Initializes the variable sum to 3. This acts as the starting value for calculations.

while sum < N:
Starts a while loop that runs as long as sum is less than N.

sum = sum * 2 + 3
Updates the value of sum in each iteration. The formula doubles the current sum and then adds 3 to it.

return sum + 1 - N
Once the loop ends, the method calculates the result by adding 1 to sum, subtracting N, and returning the final value.
'''