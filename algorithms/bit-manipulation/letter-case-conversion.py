"""
Letter | Unicode | Binary

A = 65 = 0100 0001
a = 97 = 0110 0001

B = 66 = 0100 0010
b = 98 = 0110 0010

and so on...

If 5th bit is set then it is lowercase else uppercase.
We can use this observation to convert case of letters.

-----------------------------
1) Upper to lower

chr(ord('C') | (1 << 5)) => 'c'

Since (1 << 5) = 0100000 = 32 in decimal
32 is unicode of space character. So we can also write:

chr(ord('C') | ord(' ')) => 'c'

-----------------------------
2) Lower to upper

chr(ord('c') & ~(1 << 5)) => 'C'

Since ~(1 << 5) = 1011111 = 95 in decimal (Not exactly as MSB will be 1)
95 is unicode of underscore character. So we can also write:

chr(ord('c') & ord('_')) => 'C'


"""

# Upper to lower
print(chr(ord("C") | (1 << 5)))
print(chr(ord("C") | ord(" ")))

# Lower to upper
print(chr(ord("c") & ~(1 << 5)))
print(chr(ord("c") & ord("_")))
