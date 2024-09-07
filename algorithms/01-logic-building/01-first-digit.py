number = int(input())
lastDigit = number % 10

while number > 0:
    lastDigit = number % 10
    number = number // 10

print(lastDigit)

"""
Technique of extracting digits from number

n % 10 => Last digit of n
n // 10 => Number after removing last digit of n
"""
