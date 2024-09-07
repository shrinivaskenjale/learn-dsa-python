def mergeSort(arr, low, high):
    # Base case: If size is 0 or 1 then already sorted
    if low >= high:
        return

    # Find mid
    mid = low + (high - low) // 2
    # Sort left half
    mergeSort(arr, low, mid)
    # Sort right half
    mergeSort(arr, mid + 1, high)

    # Merge sorted arrays
    merge(arr, low, mid, high)


def merge(arr, low, mid, high):
    # Create array for each half
    left = arr[low : mid + 1]
    right = arr[mid + 1 : high + 1]

    # Now merge these 2 arrays in original array in range [low,high]
    i = j = 0
    k = low

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            k += 1
            i += 1
        else:
            arr[k] = right[j]
            k += 1
            j += 1

    while i < len(left):
        arr[k] = left[i]
        k += 1
        i += 1

    while j < len(right):
        arr[k] = right[j]
        k += 1
        j += 1


arr = [6, 4, 2, 8, 5, 6, 8, 2]
# Sort array in range [0,n-1]
mergeSort(arr, 0, len(arr) - 1)
print(arr)


"""
Merge sort is:
    1. Stable
    2. Not in-place
    3. Divide & conquer algorithm

-------------------------------------

Steps:
    1. Find the middle point to divide the array into 2 halves.
    2. Call merge sort on first half 
    3. Call merge sort on second half
    4. Merge the two sorted halves


-------------------------------------

Time complexity: O(nlog(n))

Recurrence relation: T(n) = 2T(n/2) + n

-------------------------------------

Space complexity: O(n)


-------------------------------------

Read this
https://www.geeksforgeeks.org/merge-sort/

"""
