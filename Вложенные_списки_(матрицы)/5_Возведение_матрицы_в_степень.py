row_col = int(input())          # квадратная матрица
matrix = [[int(i) for i in input().split()] for _ in range(row_col)]
degree = int(input())           # степень
first_matrix = matrix.copy()    # сохраняем первоначальные данные


for _ in range(degree - 1):
    new_matrix = [[0 for _ in range(row_col)] for _ in range(row_col)]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            row = matrix[i]
            col = [first_matrix[x][j] for x in range(len(matrix))]
            new_matrix[i][j] = sum([x*y for x, y in zip(row, col)])
    matrix = new_matrix.copy()

for row in matrix:
    print(*row)