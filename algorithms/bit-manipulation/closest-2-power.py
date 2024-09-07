"""
Find the highest power of 2 which is less than or equal to the given number.

n=30 => 16
n=70 => 64

Manually checking each no. from n to 1 is inefficient.
It is better to find powers of 2 and then find the closest one.
"""


# O(1)
def getClosest2Power(n):
    for i in range(31):
        value = 1 << i
        if value <= n:
            # Possible answer.
            # Since we want to maximize the answer, we continue.
            answer = value
        else:
            break
    return answer


print(getClosest2Power(30))
print(getClosest2Power(70))
print(getClosest2Power(666))
