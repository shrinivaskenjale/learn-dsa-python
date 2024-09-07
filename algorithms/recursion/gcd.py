"""
GCD using recursion and Euclidean Algorithm
"""


def getGcd(n, p):
    if n == 0:
        return p
    if p == 0:
        return n

    return getGcd(p, n % p)


n, p = 30, 50

print(getGcd(n, p))
