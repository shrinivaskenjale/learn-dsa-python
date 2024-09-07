"""
Toggle kth bit of number

Ex. n=107 and k=2
107 is 1101011
Output will be 1101111

We want to keep other bits as it is and only change kth bit. So, we can use XOR operator because:
    1) otherBit ^ 0 = otherBit
    2) targetBit | 1 = ~targetBit

So, to toggle we perform XOR with binary no. whose kth bit is set to 1.
We can get this no. by performing (1 << k).

    1 1 0 1 0 1 1
XOR
    0 0 0 0 1 0 0
    -------------
    1 1 0 1 1 1 1

So answer will be: 
------------
n ^ (1 << k)
------------
"""


n = 107
k = 2

answer = n ^ (1 << k)

print(answer)
print(bin(n))
print(bin(answer))
