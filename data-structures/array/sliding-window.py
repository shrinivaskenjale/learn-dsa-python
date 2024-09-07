"""
Sliding window technique

This technique shows how nested loop in some problems can be converted to single for loop to reduce time complexity.

We perform some calculation on a window of consecutive elements of array of some size k and then move forward this window till end such that size is same.
"""

"""
Example - Given an array of integers of size n, find maximum sum of k consecutive elements.

Basic approach can to use nested loop to find all possible k consecutive elements and tracking maximum sum.

Using sliding window, 
1. We create window of first k elements, find the sum of elements in the window.
2. Use loop to move window and in each iteration, subtract the removed element from sum and add newly added element. Keep track of maximum sum.
"""

n = 5
k = 3
arr = [4, 3, 1, 2, 5]


total = 0
maxTotal = float("-inf")

# Check first window
for i in range(k):
    total += arr[i]

maxTotal = max(maxTotal, total)

# Move window till end
for i in range(k, n):
    total = total + arr[i] - arr[i - k]
    maxTotal = max(maxTotal, total)


print(maxTotal)
