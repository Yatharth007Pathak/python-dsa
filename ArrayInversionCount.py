"""
Given an array of integers. Find the Inversion Count in the array.  
Two elements arr[i] and arr[j] form an inversion if arr[i] > arr[j] and i < j.

Inversion Count: For an array, inversion count indicates how far (or close) the array is from being sorted. 
If the array is already sorted then the inversion count is 0.
If an array is sorted in the reverse order then the inversion count is the maximum. 

Examples:

Input: arr[] = [2, 4, 1, 3, 5]
Output: 3
Explanation: The sequence 2, 4, 1, 3, 5 has three inversions (2, 1), (4, 1), (4, 3).

Input: arr[] = [2, 3, 4, 5, 6]
Output: 0
Explanation: As the sequence is already sorted so there is no inversion count.

Input: arr[] = [10, 10, 10]
Output: 0
Explanation: As all the elements of array are same, so there is no inversion count.
"""

class Solution:
    # Function to count inversions in the array.
    def merge(self, arr, temp_arr, left, mid, right):
        i = left    # Starting index for left subarray
        j = mid + 1 # Starting index for right subarray
        k = left    # Starting index to be sorted
        inv_count = 0

        # Merge the two subarrays while counting inversions
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp_arr[k] = arr[i]
                i += 1
            else:
                temp_arr[k] = arr[j]
                inv_count += (mid - i + 1)  # Count the inversions
                j += 1
            k += 1

        # Copy the remaining elements of left subarray if any
        while i <= mid:
            temp_arr[k] = arr[i]
            i += 1
            k += 1

        # Copy the remaining elements of right subarray if any
        while j <= right:
            temp_arr[k] = arr[j]
            j += 1
            k += 1

        # Copy the sorted subarray into original array
        for i in range(left, right + 1):
            arr[i] = temp_arr[i]

        return inv_count

    # Function to sort the array and count inversions using merge sort
    def mergeSort(self, arr, temp_arr, left, right):
        inv_count = 0
        if left < right:
            mid = (left + right) // 2

            inv_count += self.mergeSort(arr, temp_arr, left, mid)
            inv_count += self.mergeSort(arr, temp_arr, mid + 1, right)

            inv_count += self.merge(arr, temp_arr, left, mid, right)

        return inv_count

    def inversionCount(self, arr):
        # Create a temporary array
        temp_arr = [0] * len(arr)
        return self.mergeSort(arr, temp_arr, 0, len(arr) - 1)

# Example usage:
solution = Solution()
print(solution.inversionCount([2, 4, 1, 3, 5]))  # Output: 3
print(solution.inversionCount([2, 3, 4, 5, 6]))  # Output: 0
print(solution.inversionCount([10, 10, 10]))     # Output: 0

'''
Here’s a line-by-line breakdown of the code that counts inversions in an array using the merge sort algorithm:

class Solution:
This defines a class named Solution, which contains methods for counting inversions in an array.

def merge(self, arr, temp_arr, left, mid, right):
This defines the merge method, which merges two subarrays while counting the inversions. 
It takes the array arr, a temporary array temp_arr, and three indices: left, mid, and right.

i = left
This initializes i to the starting index of the left subarray.

j = mid + 1
This initializes j to the starting index of the right subarray.

k = left
This initializes k to the starting index where the sorted elements will be placed in the temp_arr.

inv_count = 0
This initializes inv_count to zero, which will keep track of the number of inversions.

while i <= mid and j <= right:
This begins a loop that continues as long as there are elements in both subarrays.

if arr[i] <= arr[j]:
This checks if the current element in the left subarray is less than or equal to the current element in the right subarray.

temp_arr[k] = arr[i]
If the condition is true, it places the element from the left subarray into the temp_arr.

i += 1
This increments i to the next element in the left subarray.

else:
If the current element in the left subarray is greater than the current element in the right subarray, the code in this block executes.

temp_arr[k] = arr[j]
This places the current element from the right subarray into the temp_arr.

inv_count += (mid - i + 1)
This counts the number of inversions. Since the left subarray is sorted, 
all remaining elements from i to mid in the left subarray will form inversions with the current element from the right subarray.

j += 1
This increments j to the next element in the right subarray.

k += 1
This increments k to the next position in temp_arr.

while i <= mid:
This loop copies any remaining elements from the left subarray into temp_arr.

temp_arr[k] = arr[i]
This places the current element from the left subarray into temp_arr.

i += 1
This increments i.

k += 1
This increments k.

while j <= right:
This loop copies any remaining elements from the right subarray into temp_arr.

temp_arr[k] = arr[j]
This places the current element from the right subarray into temp_arr.

j += 1
This increments j.

k += 1
This increments k.

for i in range(left, right + 1):
This loop copies the sorted elements back from temp_arr to the original array arr.

arr[i] = temp_arr[i]
This assigns the sorted element from temp_arr back to arr.

return inv_count
This returns the count of inversions found during the merging process.

def mergeSort(self, arr, temp_arr, left, right):
This defines the mergeSort method, which recursively divides the array and counts inversions. 
It takes the array arr, a temporary array temp_arr, and two indices: left and right.

inv_count = 0
This initializes inv_count to zero for this call of the method.

if left < right:
This checks if the current range is valid for sorting. If not, the recursion stops.

mid = (left + right) // 2
This calculates the middle index of the current range.

inv_count += self.mergeSort(arr, temp_arr, left, mid)
This recursively calls mergeSort on the left subarray and adds the inversions found to inv_count.

inv_count += self.mergeSort(arr, temp_arr, mid + 1, right)
This recursively calls mergeSort on the right subarray and adds the inversions found to inv_count.

inv_count += self.merge(arr, temp_arr, left, mid, right)
This calls the merge method to merge the two subarrays and adds any inversions counted during the merge.

return inv_count
This returns the total count of inversions found.

def inversionCount(self, arr):
This defines the inversionCount method, which initializes the process of counting inversions.

temp_arr = [0] * len(arr)
This creates a temporary array of the same length as arr to assist with merging.

return self.mergeSort(arr, temp_arr, 0, len(arr) - 1)
This calls the mergeSort method with the entire array, and returns the total count of inversions.

solution = Solution()
This creates an instance of the Solution class.

print(solution.inversionCount([2, 4, 1, 3, 5]))
This calls the inversionCount method with the array [2, 4, 1, 3, 5]. 
The output is 3, as there are three inversions: (2, 1), (4, 1), and (4, 3).

print(solution.inversionCount([2, 3, 4, 5, 6]))
This calls the inversionCount method with the array [2, 3, 4, 5, 6]. The output is 0, as there are no inversions.

print(solution.inversionCount([10, 10, 10]))
This calls the inversionCount method with the array [10, 10, 10]. The output is 0, as all elements are the same, resulting in no inversions.
'''