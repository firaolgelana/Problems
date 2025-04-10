# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = [[False] * m for _ in range(n)]
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def inBound(row, col):
            return 0 <= row < n and 0 <= col < m
        def dfs(row, col):
            visited[row][col] = True
            area = 0
            for di, dj in directions:
                new_row, new_col = di + row, dj + col
                if inBound(new_row, new_col) and not visited[new_row][new_col] and grid[new_row][new_col]:
                    area += 1 + dfs(new_row, new_col)
            return area

        max_area = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] and not visited[i][j]:
                    max_area = max(dfs(i, j) + 1, max_area)

        return max_area

        