# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        start = 0
        if 0 not in nums:
            return 0
        nums.append(0)
        while start < len(nums):
            value = nums[start]
            if nums[start] != nums[value]:
                nums[start], nums[value] = nums[value], nums[start]
            else:   
                start += 1
        for i in range(len(nums)):
            if i != nums[i]:
                return i
            
        