"""
Merge 2 sorted arrays into one array.

2 pointer technique because we don't need to worry about once placed values again.

We scan both arrays left to right, compare current values and put smaller value in solution array. And then update pointers.

It may happen that, all values from one array are scanned but values in other arrays are remaining. In that case we put that array's values at the end of solution array.
"""


def merge(arr1, arr2):
    # Solution array size will be equal to sum of sizes of 2 arrays
    result = [None] * (len(arr1) + len(arr2))

    # Pointers
    i = 0  # arr1
    j = 0  # arr2
    k = 0  # result

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result[k] = arr1[i]
            i += 1
            k += 1
        else:
            result[k] = arr2[j]
            j += 1
            k += 1

    while i < len(arr1):
        result[k] = arr1[i]
        i += 1
        k += 1

    while j < len(arr2):
        result[k] = arr2[j]
        j += 1
        k += 1

    return result


if __name__ == "__main__":
    arr1 = [1, 3, 5, 7]
    arr2 = [2, 4, 6]

    result = merge(arr1, arr2)

    print(result)
