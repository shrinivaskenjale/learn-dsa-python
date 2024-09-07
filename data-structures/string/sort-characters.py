"""
Sort characters of string in decreasing order. (without inbuilt function)
algorithm => tromlihga
"""

s = "shrinivas"
freq = [0] * 26
answer = ""

for ch in s:
    freq[ord(ch) - 97] += 1

for i in range(25, -1, -1):
    for j in range(freq[i]):
        answer += chr(i + 97)

print(answer)


"""
Frequency array is always sorted. 
We will find frequency of characters and iterate on freq array from end to print decreasing order string.
"""
