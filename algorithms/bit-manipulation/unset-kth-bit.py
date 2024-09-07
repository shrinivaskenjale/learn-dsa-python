"""
Unset kth bit of number

Ex. n=107 and k=3
107 is 1101011
Output will be 1100011

We want to keep other bits as it is and only change kth bit. So, we can use AND operator because:
    1) otherBit | 1 = otherBit
    2) targetBit | 0 = 0

So, to unset we perform AND with binary no. whose kth bit is set to 0 and other bits are 1.
We can get this no. by performing ~(1 << k).

    1 1 0 1 0 1 1
AND
    1 1 1 0 1 1 1
    -------------
    1 1 0 0 0 1 1

So answer will be: 
------------
n & ~(1 << k)
------------
"""


n = 107
k = 3

answer = n & ~(1 << k)

print(answer)
print(bin(n))
print(bin(answer))
