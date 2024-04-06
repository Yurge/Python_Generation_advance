n, m = map(int, input().split())
matrix = [[0 for _ in range(m)] for _ in range(n)]

digit = 1
for r in range(n):
    for c in range(m):
        if matrix[r][c] == 0:
            row = r
            col = c
            while col >= 0 and row < n:
                matrix[row][col] = digit
                digit += 1
                row += 1
                col -= 1


for row in matrix:
    print(*[str(elem).ljust(3) for elem in row])