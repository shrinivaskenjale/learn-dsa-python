def findPeak(arr):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2
        if mid - 1 >= 0 and arr[mid] < arr[mid - 1]:
            high = mid - 1
        else:
            answer = mid
            # Try to maximize the answer
            low = mid + 1

    return answer


arr = [1, 2, 3, 4, 3, 1]
print(findPeak(arr))


"""

   .
  .  .
 .     .
.

Left line is increasing and right line is decreasing.
Assume peak exists on left line.
Any point i on left line will satisfy (arr[i]>arr[i-1]).
Any point i on right line will satisfy (arr[i]<arr[i-1]).

We run binary search on array.
If element at mid lies on right line then answer will be in range [low, mid-1].
If element at mid lies on left line then it is possible answer. But peak is maximum possible answer. So we will try to maximize our answer by further searching in range [mid+1,high].

"""
