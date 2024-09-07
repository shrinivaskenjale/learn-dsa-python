# Linear search
def linearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            # Found
            return i

    # Not found
    return -1


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    target = 43

    print(linearSearch(arr, target))
