def countingSort(array):
    n = len(array)
    # Find max element in array
    maxValue = max(array)
    # Create frequency array
    countArray = [0] * (maxValue + 1)
    for i in range(n):
        countArray[array[i]] += 1
    # Convert frequency array using prefix sum.
    # After doing this, arr[i] will be index in sorted array before which value i should be placed.
    for i in range(1, len(countArray)):
        countArray[i] = countArray[i - 1] + countArray[i]
    # Create array for output
    sortedArray = [None] * n
    # Iterate over input array from backwards to make stable sorting. Place current value in output array at correct position.
    for i in range(n - 1, -1, -1):
        index = countArray[array[i]] - 1
        sortedArray[index] = array[i]
        countArray[array[i]] = index

    return sortedArray


array = [9, 8, 7, 6, 5, 4, 3, 4, 3, 2, 1]
sortedArray = countingSort(array)
print(sortedArray)

"""
https://www.geeksforgeeks.org/counting-sort/

Counting sort is:
    Non-comparison-based sorting algorithm
    Stable
    Not in-place

Time Complexity: O(N+M) in all cases.
Space Complexity: O(N+M)
N is input array size and M is size of countArray (or maximum no. in array).

Counting sort can only be used with non-negative integers because we map array elements to array indices.
"""
