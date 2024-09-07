"""
Optimized approach: reversal algo.

A. Right rotate k times:
    1. reverse last k items
    2. reverse rest of the items
    3. reverse whole array

B. Left rotate k times:
    1. reverse first k items
    2. reverse rest of the items
    3. reverse whole array

If k >= n then k = k%n
"""


def leftRotate(arr, k):
    n = len(arr)
    k = k % n
    reverse(arr, 0, k - 1)
    reverse(arr, k, n - 1)
    reverse(arr, 0, n - 1)


def rightRotate(arr, k):
    n = len(arr)
    k = k % n
    reverse(arr, n - k, n - 1)
    reverse(arr, 0, n - k - 1)
    reverse(arr, 0, n - 1)


def reverse(arr, i, j):
    while i <= j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6]
    rightRotate(a, 2)
    print("After right rotation:", a)

    b = [1, 2, 3, 4, 5, 6]
    leftRotate(b, 8)
    print("After left rotation", b)


"""
When we right rotate array k times, we put last k items in the beginning.
When we left rotate array k times, we put first k items at the end.
"""


"""
Basic approach 1:
Ex. Right rotate k times

For k times, perform rotate right operation.

One right rotate operation:
    1. Store last array item in temp var.
    2. Shift all other items to right by one place by iterating over array
    3. Put temp var in the first place.
"""


"""
Basic approach 2:

1. Create new array of same size
2. Iterate over original array
3. Place element at `i` index into new array at `(i+k)%n` index.
"""
