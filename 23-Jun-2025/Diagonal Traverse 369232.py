# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        n, m = len(mat), len(mat[0])
        result = []
        i, j = 0, 0
        even = flag = 1
        while flag:
            if even:
                row, col = i, j
                while i >= 0 and j < m:
                    result.append(mat[i][j])
                    if (i, j) == (n - 1, m - 1):
                        flag = 0
                    i -= 1
                    j += 1
                even = 0
                if j >= m:
                    i, j = i + 2, m - 1
                else:
                    i = 0
                continue
            else:
                while j >= 0 and i < n:
                    result.append(mat[i][j])
                    if (i, j) == (n - 1, m - 1):
                        flag = 0
                    j -= 1
                    i += 1
                even = 1
                if i >= n:
                    j, i = j + 2, n - 1
                else:
                    j = 0

        return result


        