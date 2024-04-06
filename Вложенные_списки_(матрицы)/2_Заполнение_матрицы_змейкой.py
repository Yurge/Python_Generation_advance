row, col = map(int, input().split())
matrix = []

for num in range(row):
    min, max = num * col, num * col + col
    current_row = list(range(min + 1, max + 1))
    matrix.append([reversed(current_row), current_row][num % 2 == 0])


for row in matrix:
    print(*[str(elem).ljust(3) for elem in row])
