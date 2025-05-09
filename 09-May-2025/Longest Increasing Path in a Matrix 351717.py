# Problem: Longest Increasing Path in a Matrix - https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n, m = len(matrix), len(matrix[0])
        directions = (-1, 0, 1, 0, -1)
        @cache
        def dfs(row, col):
            ans = 1
            for di, dj in pairwise(directions):
                nx, ny = di + row, dj + col
                if 0 <= nx < n and 0 <= ny < m and matrix[row][col] < matrix[nx][ny]:
                    ans = max(ans, 1 + dfs(nx, ny))

            return ans



        ans = 1
        for i in range(n):
            for j in range(m):
                ans = max(ans, dfs(i, j))

        return ans
        