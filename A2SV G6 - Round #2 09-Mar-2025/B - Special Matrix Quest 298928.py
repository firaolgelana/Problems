# Problem: B - Special Matrix Quest - https://codeforces.com/gym/586960/problem/B

n = int(input())
matrix = [[int(n)for n in input().split()]for i in range(n)]

main_diagonal = [0] * (n + n - 1)
antiMDiagonal = [0] * (n + n - 1)
row, col = 0, 0
for i in range(n):
    for j in range(n):
        main_diagonal[i-j] += matrix[i][j]
        antiMDiagonal[i+j] += matrix[i][j]
        if j == (n-1)//2:
            col += matrix[i][j]
        if i == (n-1)//2:
            row += matrix[i][j]
middle = matrix[(n-1)//2][(n-1)//2]
matrix_sum = main_diagonal[0] + antiMDiagonal[(2*n-1)//2] + row + col - (middle * 3)
print(matrix_sum)