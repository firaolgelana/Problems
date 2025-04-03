# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        start = 0
        while start < len(nums):
            idx = nums[start] - 1
            if nums[start] != nums[idx]:
                nums[start], nums[idx] = nums[idx], nums[start]
            else:
                start += 1

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return [nums[i], i + 1]