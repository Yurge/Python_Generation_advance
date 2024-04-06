degree = 48
matrix = [[2, 3],
          [4, 5]]

first_matrix = [[2, 3],
                [4, 5]]

for _ in range(degree - 1):
    new_matrix = [[0, 0], [0, 0]]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            row = matrix[i]
            col = [first_matrix[x][j] for x in range(len(matrix))]
            new_matrix[i][j] = sum([x*y for x, y in zip(row, col)])
    matrix = new_matrix.copy()

for row in matrix:
    print(row)