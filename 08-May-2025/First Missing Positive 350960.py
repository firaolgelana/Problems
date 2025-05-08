# Problem: First Missing Positive - https://leetcode.com/problems/first-missing-positive/description/

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        start = 0
        while start < len(nums):
            value = nums[start]-1
            if nums[start] > 0 and nums[start] < len(nums) and nums[start] != nums[value]:
                nums[start], nums[value] = nums[value], nums[start]
            else:
                start += 1

        for i in range(len(nums)):
            if i + 1 != nums[i]:
                return i + 1
                
        return len(nums) + 1
       


        