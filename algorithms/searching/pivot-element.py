def getPivot(arr):
    low = 0
    high = len(arr) - 1

    while low < high:
        mid = low + (high - low) // 2

        if arr[mid] >= arr[0]:
            low = mid + 1
        else:
            high = mid

    return low


arr = [2, 3, 7, 9, 1]
print(getPivot(arr))


"""
Find pivot element in sorted then rotated array.
Pivot element is smallest element in sorted rotated array.
In [7,9,1,2,3], 1 is the pivot element.
Draw lines to understand the logic

while start<end:
1. if arr[mid]>=arr[0] means mid lies on first half.
We find on right half

2. else mid lies on second half and mid could be pivot as well.
We find on left half but including mid element.

answer is start/end/mid
"""

# This question type can be solved linearly.
