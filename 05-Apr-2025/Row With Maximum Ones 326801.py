# Problem: Row With Maximum Ones - https://leetcode.com/problems/row-with-maximum-ones/

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        idx, count = 0, 0
        for i, row in enumerate(mat):
            ones = row.count(1)
            if ones > count:
                idx, count = i, ones

        return [idx, count]
        