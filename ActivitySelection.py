"""
Given some activities with their start and finish day given in array start[] and end[]. 
Select the maximum number of activities that can be performed by a single person, 
assuming that a person can only work on a single activity at a given day.
Note : Duration of the activity includes both starting and ending day.

Examples:

Input: start[] = [2, 1], end[] = [2, 2]
Output: 1
Explanation: A person can perform only one of the given activities.

Input: start[] = [1, 3, 2, 5], end[] = [2, 4, 3, 6]
Output: 3
Explanation: A person can perform activities 1, 2 and 4.
"""

class Solution:
    def activitySelection(self, start, end):
        # Create a list of tuples where each tuple is (start, end) for each activity
        activities = list(zip(start, end))
        # Sort activities based on their end time
        activities.sort(key=lambda x: x[1])
        
        # The first activity will always be selected
        count = 1
        # End time of the last selected activity
        last_end_time = activities[0][1]
        
        # Iterate through the sorted activities and select non-overlapping ones
        for i in range(1, len(activities)):
            if activities[i][0] > last_end_time:
                count += 1
                last_end_time = activities[i][1]
        
        return count

# Example usage:
solution = Solution()
print(solution.activitySelection([2, 1], [2, 2]))  # Output: 1
print(solution.activitySelection([1, 3, 2, 5], [2, 4, 3, 6]))  # Output: 3

'''
Here's a line-by-line breakdown of the activitySelection function:

class Solution:
Defines the Solution class which contains the activitySelection method.

def activitySelection(self, start, end):
This function takes two lists: start, which contains the start times of activities, and end, which contains their corresponding end times. 
The goal is to select the maximum number of activities that don't overlap.

activities = list(zip(start, end)):
This line creates a list of tuples by combining the start and end times. 
Each tuple represents an activity, where the first element is the start time, and the second is the end time.

activities.sort(key=lambda x: x[1]):
The activities list is sorted by the end time of each activity in ascending order. This ensures that the activity 
that finishes the earliest is considered first, which is key to maximizing the number of non-overlapping activities.

count = 1:
Initializes count to 1, representing the first activity being selected (since we always pick the first one based on its earliest end time).

last_end_time = activities[0][1]:
Initializes last_end_time with the end time of the first activity in the sorted list. 
This keeps track of the end time of the last selected activity.

for i in range(1, len(activities)):
Loops through the remaining activities, starting from the second one (i = 1), as the first one has already been selected.

if activities[i][0] > last_end_time:
Checks if the current activity's start time is greater than the last_end_time. 
If it is, that means the current activity doesn't overlap with the previously selected one.

count += 1:
If the condition is met, increment the count since the current activity is selected.

last_end_time = activities[i][1]:
Update last_end_time to the end time of the newly selected activity.

return count:
After iterating through all activities, the function returns the total number of non-overlapping activities selected.

solution = Solution():
Creates an instance of the Solution class.

print(solution.activitySelection([2, 1], [2, 2])):
Test case where there are two activities with start times [2, 1] and end times [2, 2]. 
Since the two activities overlap, only one can be selected, so the output is 1.

print(solution.activitySelection([1, 3, 2, 5], [2, 4, 3, 6])):
Test case with start times [1, 3, 2, 5] and end times [2, 4, 3, 6]. 
Here, three non-overlapping activities can be selected, so the output is 3.
'''