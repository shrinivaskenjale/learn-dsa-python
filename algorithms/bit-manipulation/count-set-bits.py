"""
Count the number of set bits in binary representation of a number.

n & (n-1) unsets rightmost set bit.
We will perform same operation until n becomes 0.
Each time one set bit will be removed. We can count iterations.
"""


def count1(n):
    count = 0
    while n:
        count += 1
        n = n & (n - 1)
    return count


print(count1(15))
print(count1(0))
print(count1(64))


"""
Using in-built functions:
"""

n = 15
setBits = bin(n).count("1")
print(setBits)
