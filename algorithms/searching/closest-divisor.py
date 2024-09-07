import math


# O(log N)
def getLowerBound(arr, target):
    low = 0
    high = len(arr) - 1
    answer = -1
    while low <= high:
        mid = low + (high - low) // 2

        if arr[mid] >= target:
            answer = mid
            high = mid - 1
        else:
            low = mid + 1

    if answer == -1:
        return len(arr)
    return answer


# O(sqrt(n) + mlog(m) + log(m)) where m is count of divisors
def getClosestDivisor(n, k):
    # O(sqrt(n))
    divisors = getDivisors(n)
    divisors.sort()

    # O(log(m))
    lowerBound = getLowerBound(divisors, k)

    if divisors[lowerBound] == k:
        return k

    if lowerBound == len(divisors):
        return divisors[-1]

    if lowerBound == 0:
        return divisors[0]

    if abs(k - divisors[lowerBound]) < abs(k - divisors[lowerBound - 1]):
        return divisors[lowerBound]
    else:
        # In case previous divisor has same difference or lower difference.
        return divisors[lowerBound - 1]


def getDivisors(n):
    divisors = []
    for i in range(1, math.floor(math.sqrt(n) + 1)):
        if n % i == 0:
            divisors.append(i)

            j = n // i
            if i != j:
                divisors.append(j)

    return divisors


n = 30
k = 13
print(getClosestDivisor(n, k))
