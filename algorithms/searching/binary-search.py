"""
https://www.geeksforgeeks.org/binary-search/
https://www.geeksforgeeks.org/binary-search-in-java/
"""


# O(log n)
def binarySearch(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == target:
            # Found
            return mid

        if arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

    # Not found
    return -1


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(binarySearch(arr, 2))


"""
Elements should be in sorted order.

[low,high] is our search range.

Our condition is low<=high

First we need to find mid element
int mid = low + (high - low)/2;

Compare target with mid value:
1. If equal then we found answer and we stop our search
2. If target is greater than mid then continue search in right half
3. Else search in left half
"""


"""
Time complexity: O(log(n))
n => n/2 => n/4 .... => n/2^k
n/2^k=1
2^k=n
k=log(n) ...(base 2)
"""
