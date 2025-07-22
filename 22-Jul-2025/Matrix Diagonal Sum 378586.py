# Problem: Matrix Diagonal Sum - https://leetcode.com/problems/matrix-diagonal-sum/description/

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        i, j = 0, n - 1
        _sum = 0
        while i < n:
            _sum += mat[i][i]
            _sum += mat[i][j]
            i += 1
            j -= 1
        if n & 1:
            _sum -= mat[n // 2][n //2]

        return _sum

        