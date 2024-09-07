"""
n=5

        1
      1 1
    1 1 1
  1 1 1 1
1 1 1 1 1

1. Total n rows. So, outer loop iterates n times.

2. In ith row first print n-i spaces then print i 1s.

3. Change line once j is over.
"""

n = 5

for i in range(n):
    for j in range(n - i - 1):
        print(" ", end=" ")

    for j in range(i + 1):
        print(1, end=" ")

    print()
