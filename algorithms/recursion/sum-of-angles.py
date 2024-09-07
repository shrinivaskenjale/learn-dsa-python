"""
You are given N integers. Basically they denote angle(in degrees). You need to determine whether it is possible to assign a sign(positive/negative) to the numbers such that the sum of angles becomes 0 . 

Note that 360 also corresponds to 0 . 

Example: If the angles are 10 , 20 , 30 then assign the sign + 10 , + 20 , − 30 and we output True.
"""


def solve(array, i, j, total):
    if i > j:
        if total % 360 == 0:
            return True
        else:
            return False

    if solve(array, i + 1, j, total + array[i]):
        return True

    return solve(array, i + 1, j, total - array[i])


# array = [120, 120, 120]
array = [10, 20, 30]
n = len(array)

answer = solve(array, 0, n - 1, 0)
print(answer)
