"""
Check kth bit is set or unset

Ex. n=107 and k=2
107 is 1101011
Output will be "UNSET"

We will make other bits 0 and only check kth bit. So, we can use AND operator because:
    1) otherBit & 0 = 0
    2) targetBit & 1 = targetBit

We perform AND with binary no. whose kth bit is set to 1.
We can get this no. by performing (1 << k).

    1 1 0 1 0 1 1
AND
    0 0 0 0 1 0 0
    -------------
    0 0 0 0 0 0 0

So answer will be: 
------------
If n ^ (1 << k) == 0 then "UNSET"
Else "SET"
------------
"""

n = 107
k = 3

value = n & (1 << k)

if value == 0:
    print("UNSET")
else:
    print("SET")
