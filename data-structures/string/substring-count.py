"""
Find count of substrings in given string that contain word 'aman' at least once
"""


def solve(s):
    count = 0
    for i in range(len(s) - 3):
        subStr = s[i:]
        index = subStr.find("aman")
        if index == -1:
            break
        count += len(subStr) - (index + 3)

    print(count)


solve("amanmgnaa")
solve("amanaaamanc")
