"""
Sort array containing 0s and 1s.

For such grouping problems in arrays, use n-pointer technique.

Here 2 types of elements are present so 2 pointer technique.

[0,i) => 0
[i,j] => ?
(j,n-1] => 1
"""


def sort01(arr):
    i = 0
    j = len(arr) - 1

    while i <= j:
        if arr[i] == 1 and arr[j] == 0:
            arr[i] = 0
            arr[j] = 1
            i += 1
            j -= 1
        elif arr[i] == 0:
            i += 1
        elif arr[j] == 1:
            j -= 1


if __name__ == "__main__":
    arr = [1, 1, 0, 0, 0, 0, 1, 0]

    sort01(arr)
    print(arr)
