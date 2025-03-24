# Problem: N-Queens - https://leetcode.com/problems/n-queens/description/

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]
        def is_valid(x, y):
            for i in range(y, -1, -1):
                if board[x][i] == 'Q':
                    return False
            i, j = x, y
            while i >= 0 and j >= 0:
                if board[i][j] == "Q":
                    return False
                i -= 1
                j -= 1
            i, j = x, y
            while i < n and y >= 0:
                if board[i][j] == "Q":
                    return False
                i += 1
                j -= 1
            return True

        ans = []
        def backtrack(idx):
            if idx == n:
                arr = ["".join(row) for row in board]
                ans.append(arr)
                return

            for i in range(n):
                if is_valid(i, idx):
                    board[i][idx] = "Q"
                    backtrack(idx + 1)
                    board[i][idx] = "."

        backtrack(0)
        return ans
        