# This example takes only n*n matrix.
# For multiplication, matrices must be a*b and b*c and result will be a*c


def add(m1, m2, n):
    result = []
    for i in range(n):
        result.append([None] * n)

    for i in range(n):
        for j in range(n):
            result[i][j] = m1[i][j] + m2[i][j]

    output(result, n)


def multiply(m1, m2, n):
    result = []
    for i in range(n):
        result.append([None] * n)

    for i in range(n):
        for j in range(n):
            total = 0

            for k in range(n):
                total += m1[i][k] * m2[k][j]

            result[i][j] = total

    output(result, n)


def output(matrix, n):
    for row in matrix:
        print(row)


if __name__ == "__main__":
    n = 3
    matrix1 = []
    for i in range(3):
        matrix1.append(list(map(int, input().split())))

    print("-------------------------------")

    matrix2 = []
    for i in range(3):
        matrix2.append(list(map(int, input().split())))

    print("-------------------------------")

    add(matrix1, matrix2, n)

    print("-------------------------------")

    multiply(matrix1, matrix2, n)
