# Problem: H - Dominoes - https://codeforces.com/gym/589822/problem/H

from collections import defaultdict, deque, Counter
import sys, math
 
input = sys.stdin.readline
 
def iin():return int(input())
 
def sin():return input().strip()
 
def lin():return list(map(int, input().split()))
  
def minp(): return map(int, input().split())

def prefix(matrix, n, m):
    prefix = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            prefix[i+1][j+1] = prefix[i][j+1] + prefix[i+1][j] - prefix[i][j] + matrix[i][j]
    return prefix
def get_sum(prefix, r1, c1, r2, c2):
    return prefix[r2+1][c2+1] - prefix[r1][c2+1] - prefix[r2+1][c1] + prefix[r1][c1]

def main():
    row, col = minp()
    grid = [sin() for _ in range(row)]
    row_D = [[0] * (col) for _ in range(row)]
    col_D = [[0] * (col + 1) for _ in range(row + 1)]
    
    for i in range(row):
        col_count = 0
        for j in range(col):
            col_count = col_count + 1 if grid[i][j] == '.' else 0
            if col_count >= 2:
                row_D[i][j] = 1
    for i in range(col):
        row_count = 0
        for j in range(row):
            row_count = row_count + 1 if grid[j][i] == '.' else 0
            if row_count >= 2:
                col_D[j][i] = col_D[j][i] + 1
    prefix_row = prefix(row_D, row, col)
    prefix_col = prefix(col_D, row, col)
    q = iin()
    for _ in range(q):
        r1, c1, r2, c2 = minp()
        row = get_sum(prefix_row, r1 - 1, c1, r2 - 1, c2 - 1)
        col = get_sum(prefix_col, r1, c1 - 1, r2 - 1, c2 - 1)
        print(row + col)

if __name__ == "__main__":
    t = 1
    for i in range(t):
        main()
