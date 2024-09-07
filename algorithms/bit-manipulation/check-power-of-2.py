"""
Check whether number is power of 2

We can use 2 properties:
1) Power of 2 contains only 1 set bit.
2) n & n-1 unsets rightmost set bit.

If n is power of 2 and if we perform n & n-1 then rightmost set bit which is only set bit will be unset and result will be 0.

"""


def is2Power(n):
    result = n & (n - 1)
    if result == 0:
        return True

    return False


print(is2Power(64))
print(is2Power(35))
print(is2Power(4))
print(is2Power(31))
