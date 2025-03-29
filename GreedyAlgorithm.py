"""
You are given timings of n meetings in the form of (start[i], end[i]) 
where start[i] is the start time of meeting i and end[i] is the finish time of meeting i. 
Return the maximum number of meetings that can be accommodated in a single meeting room, 
when only one meeting can be held in the meeting room at a particular time. 

Note: The start time of one chosen meeting can't be equal to the end time of the other chosen meeting.

Example:
Input: n = 6, start[] = [1, 3, 0, 5, 8, 5], end[] =  [2, 4, 6, 7, 9, 9]
Output: 4
Explanation: Maximum four meetings can be held with given start and end timings. The meetings are - (1, 2), (3, 4), (5,7) and (8,9)
"""

class Solution:
    def maximumMeetings(self, n, start, end):
        # Combine the start and end times into a list of tuples (start, end)
        meetings = [(start[i], end[i]) for i in range(n)]
        
        # Sort meetings by their end time
        meetings.sort(key=lambda x: x[1])
        
        # Variable to store the maximum number of meetings
        count = 1  # We can always attend at least one meeting (the first one after sorting)
        last_end_time = meetings[0][1]  # End time of the first selected meeting
        
        # Iterate over the remaining meetings
        for i in range(1, n):
            if meetings[i][0] > last_end_time:  # If the start time of the current meeting is after the last selected meeting's end time
                count += 1
                last_end_time = meetings[i][1]  # Update the end time of the last selected meeting
        
        return count

n = 6
start = [1, 3, 0, 5, 8, 5]
end = [2, 4, 6, 7, 9, 9]
solution = Solution()
print(solution.maximumMeetings(n, start, end))   # Output: 4

'''
To solve this problem, we can use a greedy algorithm. 
The idea is to always select the meeting that ends the earliest (because it leaves the maximum room for other meetings). 
Once a meeting is selected, the next meeting we select must start after the current one finishes.

Here's a detailed explanation of the code:

class Solution:
This defines a class Solution, which contains the method maximumMeetings. 
The method is designed to calculate the maximum number of meetings that can be attended without any overlap.

def maximumMeetings(self, n, start, end):
This method takes three parameters:
n: The number of meetings.
start: A list containing the start times of the meetings.
end: A list containing the end times of the meetings.

meetings = [(start[i], end[i]) for i in range(n)]
This line creates a list of tuples, where each tuple consists of the start and end times of a meeting. 
For example, if start = [1, 3, 2] and end = [2, 4, 3], the meetings list will be [(1, 2), (3, 4), (2, 3)].

meetings.sort(key=lambda x: x[1])
This line sorts the meetings list by the end time of each meeting (i.e., the second element of each tuple). 
Sorting by the earliest possible end time ensures that we can attend the maximum number of non-overlapping meetings. 
After sorting, the meetings might look like [(1, 2), (2, 3), (3, 4)].

count = 1
This initializes a counter count to 1 because at least one meeting (the first one after sorting) can always be attended.

last_end_time = meetings[0][1]
Initializes last_end_time to the end time of the first meeting in the sorted list. This keeps track of when the last selected meeting finishes.

for i in range(1, n):
Starts a loop from the second meeting (i = 1) to the nth meeting. We compare each meeting's start time with the last_end_time.

if meetings[i][0] > last_end_time:
Checks if the start time of the current meeting (meetings[i][0]) is greater than the last_end_time. 
If true, it means the current meeting does not overlap with the previous one, so we can attend this meeting.

count += 1
If the current meeting can be attended, we increment the count of meetings.

last_end_time = meetings[i][1]
Updates last_end_time to the end time of the current meeting, as it is now the most recent meeting we've attended.

return count
After iterating through all the meetings, the method returns the total count of non-overlapping meetings that can be attended.

n = 6
This represents the total number of meetings (6 meetings in this case).

start = [1, 3, 0, 5, 8, 5]
This list contains the start times of the meetings. Each value corresponds to when a meeting begins. 
For example, the first meeting starts at time 1, the second meeting starts at time 3, and so on.

end = [2, 4, 6, 7, 9, 9]
This list contains the end times of the meetings. Each value corresponds to when a meeting ends. 
For example, the first meeting ends at time 2, the second meeting ends at time 4, and so on.

solution = Solution()
Creates an instance of the Solution class.

print(solution.maximumMeetings(n, start, end))   # Output: 4
Calls the maximumMeetings method with the size n and array start and end. 
The method calculates and returns the number of possible meetings, which is 34
'''

'''
Iterating Over the Meetings:
The code then enters a loop to go through each meeting and check if it can be attended without overlapping with previously selected meetings. 

First Meeting (i = 0):
This is already selected, as it is the first meeting.
The meeting is (1, 2) with start time 1 and end time 2.
The last_end_time is set to 2 and count = 1.

Second Meeting (i = 1):
Start time: 3, End time: 4
Since 3 > last_end_time (2), this meeting can be attended.
The count is incremented to 2 and last_end_time is updated to 4.

Third Meeting (i = 2):
Start time: 5, End time: 7
Since 5 > last_end_time (4), this meeting can be attended.
The count is incremented to 3 and last_end_time is updated to 7.

Fourth Meeting (i = 3):
Start time: 0, End time: 6
Since 0 < last_end_time (7), this meeting overlaps with the last one, so it is not selected.
The count remains 3 and last_end_time remains 7.

Fifth Meeting (i = 4):
Start time: 8, End time: 9
Since 8 > last_end_time (7), this meeting can be attended.
The count is incremented to 4 and last_end_time is updated to 9.

Sixth Meeting (i = 5):
Start time: 5, End time: 9
Since 5 < last_end_time (9), this meeting overlaps with the last one, so it is not selected.
The count remains 4.
'''