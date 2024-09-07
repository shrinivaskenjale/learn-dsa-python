"""
Given a string, check if it is valid palindrome.
"""


def isPalindrome(s, i, j):
    # Base case: if length is 0 or 1, it is valid palindrome.
    if i >= j:
        return True

    # If both ends of string are not equal then not valid
    if s[i] != s[j]:
        return False

    # If both ends of string are equal then continue middle string recursively.
    return isPalindrome(s, i + 1, j - 1)


s = "aabbaac"
# Call recursive function to see if string is palindrome in index [0,n-1]
print(isPalindrome(s, 0, len(s) - 1))
