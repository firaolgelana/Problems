# Problem: B - The Ethiopian Lakes - https://codeforces.com/gym/602812/problem/B

from collections import defaultdict, deque, Counter
from bisect import bisect_left, bisect_right
from math import ceil, floor, pow
import sys, threading
sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)

input = lambda: sys.stdin.readline().strip()
def iin():return int(input())
def sin():return input().strip()
def lin():return list(map(int, input().split()))  
def main():
    n, m = lin()
    grid = [lin() for _ in range(n)]
    def inbound(row, col):
        return 0 <= row < n and 0 <= col < m
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [[False] * m for _ in range(n)]
    def dfs(row, col):
        visited[row][col] = True
        ans = grid[row][col]
        for di, dj in directions:
            newx, newy = di + row, dj + col
            if inbound(newx, newy) and grid[newx][newy] and not visited[newx][newy]:
                ans += dfs(newx, newy)

        return ans
    ans = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and grid[i][j]:
                ans = max(ans, dfs(i, j))
    
    print(ans)
if __name__ == "__main__":
    t = iin()
    # t = 1
    for i in range(t):
        main()
    
