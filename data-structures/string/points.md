Unicode of char
ord('a') => 97

Char of unicode
chr(97) => 'a'

---

# Frequency array of characters

Create frequency array of size 26.
To create freq array of chars, we have to map characters to numbers in range 0 to 25 (26 characters).
a = 0, b = 1 ... z = 25

To achieve this subtract the unicode of 'a' from unicode of characters.
freq[ord('b') - ord('a')] => freq[1]

To convert index to character, add unicode of 'a' to index and then use chr() function.
chr(0 + ord('a')) => chr(97) => 'a'

---

For rotation of strings, use slicing.

---

Substring is continuous characters of string.
Subsequence is non-continuous sequence of characters.
For 'abc', 'ac' is subsequence but not a substring.

---
