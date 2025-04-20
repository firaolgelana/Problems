# Problem: Word search - https://leetcode.com/problems/word-search/

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n, m = len(board), len(board[0])
        def inbound(row, col):
            return 0 <= row < n and 0 <= col < m
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def dfs(row, col, idx, visited):
            if idx == len(word):
                return True
            visited[row][col] = True
            for di, dj in directions:
                newx, newy = di + row, dj + col
                if inbound(newx, newy) and not visited[newx][newy] and board[newx][newy] == word[idx]:
                    if dfs(newx, newy, idx + 1, visited):
                        return True
            visited[row][col] = False
            return False          


        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    visited = [[False] * m for _ in range(n)]
                    if dfs(i, j, 1, visited):
                        return True
                    
        return False
        