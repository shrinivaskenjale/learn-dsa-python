"""
Remove adjacent duplicate characters (keep only 1) in given string.
"""


def solve(s, i, j):
    # Base case: if length of string is 1 then that string itself will be answer.
    if i == j:
        return s[i]

    # Remove adjacent duplclicates from string [i+1, j] and get result
    result = solve(s, i + 1, j)
    # If ith char is same as first character of result then we can't join them as they will create adjacent duplicates.
    if result[0] == s[i]:
        return result
    else:
        return s[i] + result


s = "abccccdeffgghcj"
# s = "aaaaaaa"
# Ask recusrsive function to remove adjacent duplicates from string s in range [0, n-1]
ans = solve(s, 0, len(s) - 1)
print(ans)
