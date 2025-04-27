# Problem: D - Lakes in Bahirdar - https://codeforces.com/gym/602812/problem/D

from collections import defaultdict, deque, Counter
from bisect import bisect_left, bisect_right
from math import ceil, floor, pow
import sys, threading
input = sys.stdin.readline
def iin():return int(input())
def sin():return input().strip()
def lin():return list(map(int, input().split()))  
def main():
    n, m, k = lin()
    grid = [list(sin()) for _ in range(n)]
    def inbound(row, col):
        return 0 <= row < n and 0 <= col < m
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [[False] * m for _ in range(n)]
    def dfs(row, col):
        visited[row][col] = True
        for di, dj in directions:
            newx, newy = row + di, col + dj
            if inbound(newx, newy) and not visited[newx][newy] and grid[newx][newy] == '.':
                dfs(newx, newy)

    for i in range(n):
        if grid[i][0] == '.' and not visited[i][0]:
            dfs(i, 0)
        if grid[i][m - 1] == '.' and not visited[i][m - 1]:
            dfs(i, m - 1)
    for i in range(m):
        if grid[0][i] == '.' and not visited[0][i]:
            dfs(0, i)
        if grid[n - 1][i] == '.' and not visited[n - 1][i]:
            dfs(n - 1, i)
    group_lakes = []
    def dfs(row, col, count):
        count.append((row, col))
        visited[row][col] = True
        for di, dj in directions:
            newx, newy = row + di, col + dj
            if inbound(newx, newy) and not visited[newx][newy] and grid[newx][newy] == '.':
                dfs(newx, newy, count)
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and grid[i][j] == '.':
                count = []
                dfs(i, j, count)
                group_lakes.append(count)
    group_lakes.sort(key=len)
    min_cells = 0
    for i in range(len(group_lakes) - k):
        min_cells += len(group_lakes[i])
        for j in range(len(group_lakes[i])):
            row, col = group_lakes[i][j]
            grid[row][col] = '*'
    
    print(min_cells)
    for row in grid:
        print("".join(row))

if __name__ == "__main__":
    
    sys.setrecursionlimit(1 << 30)
    threading.stack_size(1 << 27)

    main_thread = threading.Thread(target=main)
    main_thread.start()
    main_thread.join()
