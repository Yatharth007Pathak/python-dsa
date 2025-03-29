"""
Given an array of car numbers car[], an array of penalties fine[], and an integer value date. 
The task is to find the total fine which will be collected on the given date. 
The fine is collected from odd-numbered cars on even dates and vice versa.

Examples:

Input: date = 12, car[] = [2375, 7682, 2325, 2352], fine[] = [250, 500, 350, 200]
Output: 600
Explanation: The date is 12 (even), so we collect the fine from odd-numbered cars. 
The odd-numbered cars and the fines associated with them are as follows: 2375 -> 250 and 2325 -> 350
The sum of the fines is 250+350 = 600

Input: date = 8, car[] = [2222, 2223, 2224], fine[] = [200, 300, 400]
Output: 300
"""

class Solution:
    def totalFine(self, date, car, fine):
        total_fine = 0
        
        # If the date is even, collect fines from odd-numbered cars
        # If the date is odd, collect fines from even-numbered cars
        for i in range(len(car)):
            if (date % 2 == 0 and car[i] % 2 != 0) or (date % 2 != 0 and car[i] % 2 == 0):
                total_fine += fine[i]
                
        return total_fine

# Example usage
sol = Solution()

# Test case 1
date1 = 12
car1 = [2375, 7682, 2325, 2352]
fine1 = [250, 500, 350, 200]
output_1 = sol.totalFine(date1, car1, fine1)
print(f"Total fine collected on date {date1}: {output_1}")

# Test case 2
date2 = 8
car2 = [2222, 2223, 2224]
fine2 = [200, 300, 400]
output_2 = sol.totalFine(date2, car2, fine2)
print(f"Total fine collected on date {date2}: {output_2}")

'''
Here's a breakdown of the code in plain text:

class Solution:
Defines a class Solution. This class contains the method totalFine.

def totalFine(self, date, car, fine):
Defines a method totalFine within the class.
This method takes four arguments: self, date, car, and fine.
date: The date to determine whether to collect fines from odd or even-numbered cars.
car: A list containing the car numbers.
fine: A list containing the fine amounts corresponding to each car.

total_fine = 0
Initializes a variable total_fine to 0. This will hold the total sum of fines collected.

for i in range(len(car)):
A loop that iterates through the car list. i is the index, and it loops from 0 to the length of the car list.

if (date % 2 == 0 and car[i] % 2 != 0) or (date % 2 != 0 and car[i] % 2 == 0):
This condition is for collecting fines, it checks the following:
If the date is even (date % 2 == 0), it checks whether the car[i] is odd (car[i] % 2 != 0).
If the date is odd (date % 2 != 0), it checks whether the car[i] is even (car[i] % 2 == 0).
If either condition is satisfied, the fine for the car is added to total_fine.

total_fine += fine[i]
If the condition is met, the fine for the current car (fine[i]) is added to total_fine.

return total_fine
Once all cars have been checked, the method returns the total_fine collected.

date1 = 12: The date is 12 (even).
car1 = [2375, 7682, 2325, 2352]: List of car numbers.
fine1 = [250, 500, 350, 200]: List of corresponding fines.
output_1 = sol.totalFine(date1, car1, fine1): Calls the totalFine method with these values and stores the result in output_1.
print(f"Total fine collected on date {date1}: {output_1}"): Prints the total fine collected on date 12.
On date 12 (even), fines are collected from cars with odd numbers: 2375 and 2325. The total fine is 250 + 350 = 600.

date2 = 8: The date is 8 (even).
car2 = [2222, 2223, 2224]: List of car numbers.
fine2 = [200, 300, 400]: List of corresponding fines.
output_2 = sol.totalFine(date2, car2, fine2): Calls the totalFine method with these values and stores the result in output_2.
print(f"Total fine collected on date {date2}: {output_2}"): Prints the total fine collected on date 8.
On date 8 (even), fines are collected from cars with odd numbers: 2223. The total fine is 300.
'''