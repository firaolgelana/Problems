# Problem: Toeplitz matrix - https://leetcode.com/problems/toeplitz-matrix/description/

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        for i in range(n-1):
            row = matrix[i][:-1]
            row1 = matrix[i+1][1:]
            if row != row1:
                return False

        return True




        