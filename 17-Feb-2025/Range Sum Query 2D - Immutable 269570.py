# Problem: Range Sum Query 2D - Immutable - https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n, m = len(matrix), len(matrix[0])
        self.prefix_sum = [[0] * (m + 1) for i in range(n + 1)]
        for i in range(n):
            for j in range(m):
                self.prefix_sum[i][j] = self.prefix_sum[i-1][j] + self.prefix_sum[i][j-1] - self.prefix_sum[i-1][j-1] + matrix[i][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        submatrix = self.prefix_sum[row2][col2] - self.prefix_sum[row1-1][col2] - self.prefix_sum[row2][col1-1] + self.prefix_sum[row1-1][col1-1]
        return submatrix


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)