# Problem: Surrounded Regions - https://leetcode.com/problems/surrounded-regions/

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        n, m = len(board), len(board[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def inBound(row, col):
            return 0 <= row < n and 0 <= col < m

        visited = [[False] * m for _ in range(n)]
        def dfs(row, col):
            visited[row][col] = True
            for di, dj in directions:
                new_row, new_col = di + row, dj + col
                if inBound(new_row, new_col) and not visited[new_row][new_col] and board[new_row][new_col] == 'O':
                    dfs(new_row, new_col)

        for i in range(n):
            if board[i][0] == 'O':
                dfs(i, 0)
            if board[i][m - 1] == 'O':
                dfs(i, m - 1)
        for i in range(m):
            if board[0][i] == 'O':
                dfs(0, i)
            if board[n - 1][i] == 'O':
                dfs(n - 1, i)

        for i in range(n):
            for j in range(m):
                if not visited[i][j] and board[i][j] == 'O':
                    board[i][j] = 'X'