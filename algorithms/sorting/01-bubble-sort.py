def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 2, -1, -1):
        swapped = False
        for j in range(0, i + 1):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                swapped = True

        if not swapped:
            break


arr = [5, 3, 7, 3, 4, 2, 3, 7, 2]
bubbleSort(arr)
print(arr)


"""
Bubble sort is:
    1. Stable
    2. In place


------------------------------
    

Iterate over subarray (0,i) to place maximum element at last position in each iteration. Compare current element with next element, swap if required.
    round 1: [0,n-1)
    round 2: [0,n-2)
    round 3: [0,n-3)
    round i: [0,n-i)

For ith pass, we do n-i comparisons.
Since each pass places the next largest value in place, the total no. of iterations required will be n-1.

------------------------------

Optimization: If there are 0 swaps in current pass then it means array is sorted and we can break the loop to avoid unnecessary comparisons.

------------------------------

Time complexity

Best case: O(n)
Worst case: O(n^2)


Worst case: When array is reverse sorted, in each ith pass, there will be n-i comparisons and swaps.
(n-1) + (n-2) + ... + 2 + 1 = sum of n-1 natural numbers.
=> O(n^2)

Best case: When array is already sorted only (n-1) comparisons will be made (using optimization).
=> O(n)

------------------------------

Space complexity = O(1)

------------------------------

Applications:
    1. We place kth largest element at right position.
"""
