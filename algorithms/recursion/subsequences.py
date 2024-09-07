"""
Given the array of integers of length n and integer k, print all subsequences of array of length k.
"""


# In this approach - Move over arr and we have 2 choices
# 1. Pick current element
# 2. Skip current element
def solve(n, arr, k, i, seq, j):
    if k == 0:
        print(seq)
        return

    if i == n:
        return

    # take arr[i]
    seq[j] = arr[i]
    solve(n, arr, k - 1, i + 1, seq, j + 1)
    # Ignore arr[i]
    seq[j] = None
    solve(n, arr, k, i + 1, seq, j)


# In this approach - Move over seq and we have choices to pick from arr for current position of seq.
def solve2(arr, i, j, seq, a, b):
    if a > b:
        print(" ".join(map(str, seq)))
        return

    for index in range(i, j + 1):
        seq[a] = arr[index]
        solve2(arr, index + 1, j, seq, a + 1, b)


n = 4
arr = [1, 2, 3, 4]
k = 2

seq = [None] * k

# solve(n, arr, k, 0, seq, 0)
solve2(arr, 0, n - 1, seq, 0, k - 1)
