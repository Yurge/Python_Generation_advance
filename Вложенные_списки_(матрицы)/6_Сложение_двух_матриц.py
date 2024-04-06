r, c = map(int, input().split())
matrix_a = [[int(i) for i in input().split()] for _ in range(r)]
input()
matrix_b = [[int(i) for i in input().split()] for _ in range(r)]

matrix_c = [[0 for _ in range(c)] for _ in range(r)]
for i in range(r):
    for j in range(c):
        matrix_c[i][j] = matrix_a[i][j] + matrix_b[i][j]

for row in matrix_c:
    print(*row)