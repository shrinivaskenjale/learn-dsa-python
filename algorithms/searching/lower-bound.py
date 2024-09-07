def lowerBound(arr, target):
    start = 0
    end = len(arr) - 1
    answer = -1
    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] >= target:
            answer = mid
            end = mid - 1
        else:
            start = mid + 1

    if answer == -1:
        return len(arr)
    return answer


arr = [1, 2, 3, 4, 4, 4, 5, 5, 6, 9]
print(lowerBound(arr, 4))
