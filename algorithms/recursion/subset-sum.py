"""
Find the sum of all subsets of the array.

Ex. [1,2,3]
[1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]
answer = 24
"""


def solve(arr, i, j, subset):
    # Base case: If there is nothing to pick from then subset will be empty. Return its sum.
    if i > j:
        return sum(subset)

    # Include first element of sub-arr in subset and get sum of all subsets that include this element.
    subset.append(arr[i])
    withFirstElement = solve(arr, i + 1, j, subset)

    # Exclude first element of sub-arr in subset and get sum of all subsets that exclude this element.
    subset.pop()
    withoutFirstElement = solve(arr, i + 1, j, subset)

    # Answer will be sum of subsets that include and exclude first element of array.
    return withFirstElement + withoutFirstElement


arr = [1, 2, 3]
n = len(arr)
# Array/stack to track subset of given array
subset = []
# Recursive function to find sum of all subsets of array within range [0,n-1]
ans = solve(arr, 0, n - 1, subset)
print(ans)


"""
Optimized answer
https://www.geeksforgeeks.org/sum-of-the-sums-of-all-possible-subsets/
"""
