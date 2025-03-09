# Problem: D - Bomb Detection Validation - https://codeforces.com/gym/586960/problem/D


n, m = map(int, input().split())
s = [input()for i in range(n)]
def isValid(n, m, x, y):
    return 0 <= x < n and 0 <= y < m
matrix = []
for row in s:
    m_row = []
    for i in row:
        m_row.append(i)
    matrix.append(m_row)

directions = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
for i in range(n):
    for j in range(m):
        bombs = 0
        if matrix[i][j].isdigit():
            k = matrix[i][j]
            for di, dj in directions:
                newX, newY = i + di, j + dj
                if isValid(n, m, newX, newY):
                    if matrix[newX][newY] == '*':
                        bombs += 1
            if bombs != int(k):
                print("NO")
                exit()
        elif matrix[i][j] == '.':
            for di, dj in directions:
                newX, newY = i + di, j + dj
                if isValid(n, m, newX, newY):
                    if matrix[newX][newY] == '*':
                        bombs += 1
            if bombs > 0:
                print("NO")
                exit()
print("YES")

