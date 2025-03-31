# Problem: N-Queens II - https://leetcode.com/problems/n-queens-ii/description/

class Solution:
    def totalNQueens(self, n: int) -> int:
        grid = [[0] * n for _ in range(n)]
        def is_valid(x, y):
            for i in range(y, -1, -1):
                if grid[x][i]:
                    return False
            i, j = x, y
            while i >= 0 and j >= 0:
                if grid[i][j]:
                    return False
                i -= 1
                j -= 1

            i, j = x, y
            while i < n and j >= 0:
                if grid[i][j]:
                    return False
                j -= 1
                i += 1
            return True
        count = 0
        def backtrack(idx):
            nonlocal count
            if idx == n:
                count += 1
                return 

            for i in range(n):
                if is_valid(i, idx):
                    grid[i][idx] = 1
                    backtrack(idx + 1)
                    grid[i][idx] = 0

            return count

        return backtrack(0)


                