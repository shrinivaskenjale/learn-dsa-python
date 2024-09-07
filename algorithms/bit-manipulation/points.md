Bits are represented by 0 and 1.

---

# Decimal to binary

Ex. Convert 14 to binary:

| 2   | N   | Remainder |
| --- | --- | --------- |
| 2   | 14  | 0         |
| 2   | 7   | 1         |
| 2   | 3   | 1         |
| 2   | 1   | 1         |
|     | 0   |           |

Check Remainder column bottom to up.  
14 => 1110

---

# Binary to decimal

Ex. Convert 1110 to decimal:

Indexing of bits is done right to left from 0 to n-1.

| 3   | 2   | 1   | 0   |
| --- | --- | --- | --- |
| 1   | 1   | 1   | 0   |

1 x 2^3 + 1 x 2^2 + 1 x 2^1 + 0 x 2^0  
8 + 4 + 2 + 0  
14  
1110 => 14

---

# Python bitwise operators

## & - AND

1 & 1 = 1  
1 & 0 = 0  
0 & 1 = 0  
0 & 0 = 0

11011 & 10010 = 10010
|x|y|x & y|
|-|-|:-:|
|1|1|1|
|1|0|0|
|0|0|0|
|1|1|1|
|1|0|0|

## | - OR

1 | 1 = 1  
1 | 0 = 1  
0 | 1 = 1  
0 | 0 = 0

10010 | 10001 = 10011
|x|y|x \| y|
|-|-|:-:|
|1|1|1|
|0|0|0|
|0|0|0|
|1|0|1|
|0|1|1|

## ~ - NOT

~1 = 0  
~0 = 1

~5 => ~(0000 0101) = 1111 1010 => -6

Why ~5 = 6?

In python, integers are stored as signed integers.

5 => 00000101  
Here, MSB is 0.

| MSB | Number type |
| --- | ----------- |
| 0   | Positive    |
| 1   | Negative    |

Negative integers are stored using 2's complement of positive integer.  
1's complement = Invert all bits  
2's complement = 1's complement + 1

Convert -6 into binary:  
=> Find 2's complement of 6  
=> 1's complement of 6 + 1  
=> 1's complement of (0000 0110) + 1  
=> 1111 1001 + 1  
=> 1111 1010

This is same as ~5. Therefore, ~5=-6.

Note: In decimal 1+1=2. In binary, 2 is 10. So in when adding binary bits, 1+1=10. 1 should be taken as carry.

### Trick

**~x = -(x+1)**

~10 = -(10+1) = -11  
~(-10) = -(-10+1) = 9

In simple terms, ~x means add 1 to x and then invert the sign of result.  
~(-4) => -4+1 => -3 => 3

## << - Left shift

n << k  
k is no. of bits to be shifted.

1 << 1 = 2  
0000 0001 => 0000 0010

3 << 2 = 12
0000 0011 => 0000 1100

**n << k = n x 2<sup>k</sup>**

## >> - Right shift

n >> k  
k is no. of bits to be shifted.

4 >> 2 = 1
0000 0100 => 0000 0001

Bits going outside are lost.

**n >> k = n // 2<sup>k</sup>**

## ^ - XOR

x ^ y

| x   | y   | x ^ y |
| --- | --- | :---: |
| 1   | 1   |   0   |
| 1   | 0   |   1   |
| 0   | 1   |   1   |
| 0   | 0   |   0   |

If x==y then x^y=0.
x ^ 0 = x

---

# Powers of 2

All numbers which are power of 2 have only 1 set bit in the binary representation.

2<sup>k</sup> => k<sup>th</sup> bit is set.

8 => 2<sup>3</sup> => 0000 1000

# Properties

If we perform n & (n-1) then the last set bit of n gets unset.

<pre>
    14 = 1 1 1 0  
&
    13 = 1 1 0 1
         -------
         1 1 0 0
</pre>

This happens because binary representation of n-1 has all bits starting from rightmost set bit on binary representaion of n flipped.
15 = 1111
14 = 1110
13 = 1101
12 = 1100

---

No. of bits required to represent n in binary is: floor(log<sub>2</sub>n + 1) or floor(log<sub>2</sub>n) + 1.

Python has log2 function:

<pre>
import math
totalBits = math.floor(math.log2(n) + 1)
# or
totalBits = math.floor(math.log2(n)) + 1
</pre>

---

Binary number with all m bits set to 1 is 2<sup>m</sup>-1.

1111 => 2<sup>4</sup>-1 = 15

---

n & 1 returns last bit of n

---

# Tips

To create a binary no. by setting nth bits manually, start with value 0. Then set required bit using position of set bit.
