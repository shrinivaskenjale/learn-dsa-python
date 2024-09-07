def insertionSort(arr):
    n = len(arr)

    for i in range(n):
        value = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > value:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = value


arr = [5, 3, 7, 3, 4, 2, 3, 7, 2]
insertionSort(arr)
print(arr)

"""
Insertion sort is:
    1. Stable
    2. In place

------------------------------

The array is virtually split into a sorted and unsorted part. Values from unsorted part are picked and placed at the correct position in the sorted part.

Remember card example. You are given card one by one, you insert them in sorted order as you get one. You keep sorted cards in left hand and unknown cards in right hand.

------------------------------

Space complexity = O(1)

------------------------------
Time complexity

Best case = O(n)
Worst case = O(n^2)

Worst case: when array is reverse sorted. In ith pass we do i comparisons.
1 + 2 + 3 ... + n-1 => n(n-1)/2 => (n^2 - n)/2 
=> O(n^2)

Best case: When array is sorted. In ith pass we do only 1 comparison.
1 + 1 + ... n times = n
=> O(n) 

------------------------------
Applications:
    1. When size of array is small.
    2. When array is partially sorted as it is a ADAPTIVE ALGORITHM.
"""
