# Problem: Regions Cut By Slashes - https://leetcode.com/problems/regions-cut-by-slashes/description/

class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        symbol = {
            ' ': [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
            '/': [[0, 0, 1], [0, 1, 0], [1, 0, 0]],
            '\\': [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
        }

        n = len(grid)
        m = len(grid[0])
        rows = n * 3
        cols = m * 3

        big_board = [[0 for _ in range(cols)] for _ in range(rows)]

        for i in range(n):
            for j in range(m):
                char = grid[i][j]
                block = symbol[char]
                for bi in range(3):
                    for bj in range(3):
                        big_board[i * 3 + bi][j * 3 + bj] = block[bi][bj]

        directions = [0, -1, 0, 1, 0]
        n, m = len(big_board), len(big_board[0])
        def inbound(x, y):
            return 0 <= x < n and 0 <= y < m
        def dfs(row,  col):
            visited[row][col] = True
            for x, y in pairwise(directions):
                nx, ny = row + x, col + y
                if inbound(nx, ny) and not visited[nx][ny] and big_board[nx][ny] == 0:
                    dfs(nx, ny)
        
        count = 0
        visited = [[False] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if big_board[i][j] == 0 and not visited[i][j]:
                    dfs(i, j)
                    count += 1

        return count

            


                