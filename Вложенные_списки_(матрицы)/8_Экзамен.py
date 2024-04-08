# Каждый n-ый элемент во вложенный список
s = 'a b c d e f g h i j k l m n'.split(' ')
digit = 3

matrix = [[s[i] for i in range(num, len(s), digit)] for num in range(digit)]

print(matrix)


# Транспонирование матрицы
rows = int(input())
matrix = [[int(c) for c in input().split()] for r in range(rows)]

for i in range(rows):
    row = []
    for j in range(rows):
        row.append(matrix[j][i])
    print(*row)


# Снежинка
n = 11
matrix = [['.' for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        conditions = i == j or i + j + 1 == n or i == n // 2 or j == n // 2
        if conditions:
            matrix[i][j] = '*'


for row in matrix:
    print(*row)


# Симметричная матрица относительно побочной диагонали
n = int(input())
matrix = [[int(j) for j in input().split()] for i in range(n)]

def simmetry(matrix):
    for i in range(n):
        for j in range(n):
            if matrix[i][j] != matrix[n-j-1][n-i-1]:
                return 'NO'
    return 'YES'

print(simmetry(matrix))


# Латинский квадрат
n = int(input())
matrix = [[int(j) for j in input().split()] for i in range(n)]

def latin(matrix):
    for i in range(n):
        row, col = sorted(matrix[i]), sorted([matrix[j][i] for j in range(n)])
        standart = [i for i in range(1, n+1)]
        if standart != row or standart != col:
            return 'NO'
    return 'YES'

print(latin(matrix))


# Ходы ферзя
c, r = 'd5'
rows = ['1', '2', '3', '4', '5', '6', '7', '8']
columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

current_row, current_col = 7 - rows.index(r), columns.index(c)

matrix = [['.' for _ in range(8)] for _ in range(8)]

for row in range(8):
    for col in range(8):
        conditions = any([row == current_row or col == current_col,
                          abs(row - current_row) == abs(col - current_col)])
        if conditions:
            matrix[row][col] = '*'

matrix[current_row][current_col] = 'Q'

for row in matrix:
    print(*row)


# Диагонали, параллельные главной
n = 5
matrix = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i == j:
            for x in range(1, n - i):
                matrix[i][j + x] = x
                matrix[j + x][i] = x

for row in matrix:
    print(*row)
