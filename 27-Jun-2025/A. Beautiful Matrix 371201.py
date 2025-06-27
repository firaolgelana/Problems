# Problem: A. Beautiful Matrix - https://codeforces.com/problemset/problem/263/A

matrix = [list(map(int, input().split())) for _ in range(5)]
x, y = 0, 0
for i in range(5):
    for j in range(5):
        if matrix[i][j]:
            x, y = i + 1, j + 1
print(abs(3 - x) + abs(y - 3))