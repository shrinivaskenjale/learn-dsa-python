"""
2 POINTER TECHNIQUE

This technique is typically used for searching pairs in sorted array.
"""


"""
Problem - Given a sorted array, find if there exists any pair of elements such that their sum is equal to k. If multiple pairs present, print the one with max j index. If j are equal, print the one with smaller i.
"""

"""
Basic approach:

0. Create minI and maxJ vars to keep track of required pair.
1. Find all possible pairs using nested loops where i moves 0 to n-2 and j moves from i+1 to n-1.
2. Check sum of each pair.
3. If sum is equal to target, compare j to maxJ and i to minI to decide the pair is valid or not. 
"""

"""
Optimized approach: 2 pointer technique

Here we don't need to handle the case of min i or max j explicitly.
"""

arr = [4, 5, 7]
k = 11

# 2 pointers
i = 0
j = len(arr) - 1

total = 0

while i < j:
    total = arr[i] + arr[j]

    if total == k:
        print(i, j)
        break
    elif total > k:
        j -= 1
    else:
        i += 1
else:
    # no break => no pair
    print("Pair not present")
