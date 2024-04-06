row, col = map(int, input().split())
matrix = [[0 for _ in range(col)] for _ in range(row)]

digit = 1
num = 0
while digit < row * col:
    for c in range(num, col - 1 - num):         # верх
        matrix[0 + num][c] = digit
        digit += 1
    for r in range(num, row - 1 - num):         # право
        matrix[r][col - 1 - num] = digit
        digit += 1
    for c in range(col - 1 - num, num, -1):     # низ
        if matrix[row - 1 - num][c] == 0:
            matrix[row - 1 - num][c] = digit
            digit += 1
    for r in range(row - 1 - num, num, -1):     # лево
        if matrix[r][0 + num] == 0:
            matrix[r][0 + num] = digit
            digit += 1
    num += 1

for i in range(row):
    for j in range(col):
        if matrix[i][j] == 0:
            matrix[i][j] = row * col

for row in matrix:
    print(*[str(elem).ljust(2) for elem in row])
