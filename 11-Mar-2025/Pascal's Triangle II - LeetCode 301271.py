# Problem: Pascal's Triangle II - LeetCode - https://leetcode.com/problems/pascals-triangle-ii/

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def triangle(idx, row):
            nums = [1] * (idx + 1)
            for i in range(1, idx):
                nums[i] = row[i-1] + row[i]
            if idx == rowIndex:
                return nums
            return triangle(idx + 1, nums)

        return triangle(0, [])



