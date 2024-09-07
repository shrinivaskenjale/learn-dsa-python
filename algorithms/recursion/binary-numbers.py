"""
Print all binary numbers of length n without consecutive 1s.
"""


def solve(num, i, j):
    # Base case: There is nothing to fill so print answer
    if i > j:
        print("".join(map(str, num)))
        return

    # There is no restriction on filling 0 at any index.
    num[i] = 0
    solve(num, i + 1, j)

    # We can pick 1 only if its first index or previous value was not 1.
    if i == 0 or num[i - 1] != 1:
        num[i] = 1
        solve(num, i + 1, j)


n = 3
num = [None] * n
solve(num, 0, n - 1)


"""
Choice pattern problem.

We create array of size n which represents valid binary number of length n with no consecutive 1s.

We iterate over index one by one either from start to end or vice-versa and for each index we will try all correct options among 0 and 1. 
"""
