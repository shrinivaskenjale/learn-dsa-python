def selectionSort(arr):
    n = len(arr)

    for i in range(n):
        minValueIndex = i
        for j in range(i + 1, n):
            if arr[j] < arr[minValueIndex]:
                minValueIndex = j

        arr[i], arr[minValueIndex] = arr[minValueIndex], arr[i]


arr = [4, 2, 4, 2, 7, 2, 9, 1]
selectionSort(arr)
print(arr)


"""
Selection sort is:
    1. Not stable: Ex. [2,2,1], 2 will not retain relative order.
    2. In place

--------------------------------

The selection sort sorts an array by repeatedly finding the minimum element (for ascending order) and swapping it to its correct position.

There are n-i comparisons in ith pass.
There is only 1 swap in each pass. This is better than bubble sort where n-i swaps in worst case.

--------------------------------

Space complexity = O(1)

--------------------------------

Time complexity = O(n^2)

There is no best case because even if array is sorted, we have to do n-i comparisons in ith pass. But there will be no swaps.

 
n-1 + n-2 + ... + 1 = n(n-1)/2 = (n^2 - n)/2 
=> O(n^2)

--------------------------------

Applications:
    1. When size of array is small.
"""
