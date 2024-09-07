"""
n=3

1         1
1 2     2 1
1 2 3 3 2 1

1. There are n rows.

2. In each row, 
    i. first print 1 to i
    ii. print (n-i)*2 spaces
    iii. print i to 1
"""

n = int(input())

for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")

    for j in range((n - i) * 2):
        print(" ", end=" ")

    for j in range(i, 0, -1):
        print(j, end=" ")

    print()
