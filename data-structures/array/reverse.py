# Array reversal
def reverseArray(arr):
    i = 0
    j = len(arr) - 1
    while i <= j:
        # Swap
        arr[i], arr[j] = arr[j], arr[i]

        i += 1
        j -= 1


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    reverseArray(arr)
    print(arr)


"""
2 pointer technique is used since we don't need once swapped values again.
"""
