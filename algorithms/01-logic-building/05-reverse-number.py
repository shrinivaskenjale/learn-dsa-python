number = int(input())

reversedNumber = 0

while number:
    lastDigit = number % 10
    reversedNumber = reversedNumber * 10 + lastDigit
    number = number // 10

print(reversedNumber)
