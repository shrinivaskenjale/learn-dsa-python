"""
Perfect number is number where sum of its divisors except the number itself is equal to the number itself.
6 is perfect => 1+2+3
"""


n = int(input())
total = 0
for i in range(1, n // 2 + 1):
    if n % i == 0:
        total += i

if total == n:
    print(True)
else:
    print(False)
