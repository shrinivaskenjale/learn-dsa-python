if __name__ == "__main__":
    n = 3
    m = 4

    # -----------------------------------
    # Creating empty matrix

    # Option 1
    emptyMatrix1 = [[None for j in range(m)] for i in range(n)]

    # Option 2
    emptyMatrix2 = []
    for i in range(n):
        emptyMatrix2.append([None] * m)

    # -------------------------------------

    matrix = []
    # Taking input row-wise
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    print("-----------------------")
    # Output
    for i in range(n):
        for j in range(m):
            print(matrix[i][j], end=" ")
        print()
