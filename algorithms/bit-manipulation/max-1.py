"""
Find the N , such that L <= N <= R , and the number of set bits ( 1 bits) in the binary representation of the non-negative integer N is maximum possible.

Ex. L = 1 and R = 10

( 1 ) 10 = ( 1 ) 2

( 2 ) 10 = ( 10 ) 2

( 3 ) 10 = ( 11 ) 2

( 4 ) 10 = ( 100 ) 2

( 5 ) 10 = ( 101 ) 2

( 6 ) 10 = ( 110 ) 2

( 7 ) 10 = ( 111 ) 2

( 8 ) 10 = ( 1000 ) 2

( 9 ) 10 = ( 1001 ) 2

( 10 ) 10 = ( 1010 ) 2


As there are maximum number of set bits in 7 , so the answer is 7 .


-------------------------------
Approach:

We will generate binary no. with all set bits and check if those numbers lie in 
"""

L, R = map(int, input().split())
