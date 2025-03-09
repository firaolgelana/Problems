# Problem: E - Symmetrization - https://codeforces.com/gym/586960/problem/E

t = int(input())

for _ in range(t):
    n = int(input())
    grid = [list(input())for _ in range(n)]

    operations = 0
    for i in range(n//2):
        for j in range((n + 1)//2):
            value = [grid[i][j], grid[j][n-i-1], grid[n-i-1][n-j-1], grid[n-j-1][i]]

            count_ones = value.count('1')
            count_zeros = 4 - count_ones

            operations += min(count_ones, count_zeros)
    print(operations)