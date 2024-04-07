r1, c1 = map(int, input().split())
matrix_a = [[int(i) for i in input().split()] for _ in range(r1)]
input()
r2, c2 = map(int, input().split())
matrix_b = [[int(i) for i in input().split()] for _ in range(r2)]

matrix_c = [[0 for _ in range(c2)] for _ in range(r1)]

for i in range(len(matrix_c)):
    for j in range(len(matrix_c[0])):
        row = matrix_a[i]
        col = [matrix_b[x][j] for x in range(len(matrix_b))]
        matrix_c[i][j] = sum([x*y for x, y in zip(row, col)])

for row in matrix_c:
    print(*row)
