def quickSort(arr, low, high):
    # Base case: If array size is 0 or 1 then already sorted
    if low >= high:
        return

    # Create partition in array and get pivot index
    pivotIndex = partition(arr, low, high)
    # Sort the left and right half
    quickSort(arr, low, pivotIndex - 1)
    quickSort(arr, pivotIndex + 1, high)


def partition(arr, low, high):
    # [start,i) = smaller/equal
    # [i,j] = ?
    # (j,end-1] = greater
    pivot = arr[low]
    i = low
    j = high
    while i <= j:
        while i <= high and arr[i] <= pivot:
            i += 1

        while j >= low and arr[j] > pivot:
            j -= 1

        if i < j:
            arr[i], arr[j] = arr[j], arr[i]

    # Now j is at right position.
    arr[low], arr[j] = arr[j], arr[low]
    return j


arr = [9, 8, 7, 6, 5, 4, 3, 4, 3, 2, 1]
# Sort array in range [0,n-1]
quickSort(arr, 0, len(arr) - 1)
print(arr)


"""
https://www.geeksforgeeks.org/quick-sort/

Idea here is to place pivot element at its right position such that all elements on its left are smaller and all elements on its right are greater than pivot.

Then sort left and right partitions recursively.
"""

"""
Quicksort is:
    Divide & conquer algorithm
    Not stable
    In-place
"""


"""
Time complexity

If each time partition divides array in equal halves then
T(n) = 2T(n/2) + n
=>O(nlog(n))
This is best case.

If each time partion is done as 1 and n-1 then
T(n) = T(n-1) + n 
=> O(n^2)
This is worst case.

If one partition is very small compared to other.
Ex. n/10 and 9n/10
T(n) = T(n/10) + T(9n/10) + n
By recursion tree method, time complexity will be O(nlog(n)).
This is average case.
"""
