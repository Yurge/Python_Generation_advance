# Шахматная доска
r, c = (int(i) for i in input().split())
matrix = [['.' for _ in range(c)] for _ in range(r)]

for i in range(r):
    for j in range(c):
        if (j + i) % 2 != 0:
            matrix[i][j] = '*'

for row in matrix:
    print(*row)


# Побочная диагональ
n = int(input())
matrix = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    matrix[i][n-1-i] = 1
    for j in range(n):
        if i + j + 1 > n:
            matrix[i][j] = 2


for row in matrix:
    print(*row)


# Заполнение по порядку
row, col = map(int, input().split())

nums = [i for i in range(1, row * col + 1)]
matrix = [[nums.pop(0) for _ in range(col)] for _ in range(row)]

for row in matrix:
    print(*(str(col).ljust(3) for col in row))


# Заполнение по столбцам
r, c = map(int, input().split())
matrix = []

for n in range(1, r + 1):
    row = [str(n + m * r).ljust(3) for m in range(c)]
    matrix.append(row)

for row in matrix:
    print(*row)


# Заполнение диагоналей единицами
n = int(input())
matrix = []

for i in range(n):
    row = [str([0, 1][i == j or (i + j + 1 == n)]).ljust(2) for j in range(n)]
    matrix.append(row)

for row in matrix:
    print(*row)


# Заполнение матрицы единичками как писочные часы
n = int(input())
matrix = []

for i in range(n):
    row = []
    for j in range(n):
        conditions = ((i <= j and i + j + 1 <= n) or (i >= j and i + j + 1 >= n))
        row.append(str([0, 1][conditions]).ljust(3))
    matrix.append(row)

for row in matrix:
    print(*row)


# Заполнение матрицы - новая строчка сдвигается в лево на 1 ячейку
row, col = map(int, input().split())
matrix = []

current_row = [i for i in range(1, col + 1)]

for _ in range(row):
    matrix.append(current_row)
    current_row = current_row[1:] + current_row[:1]

for row in matrix:
    print(*[str(elem).ljust(2) for elem in row])


