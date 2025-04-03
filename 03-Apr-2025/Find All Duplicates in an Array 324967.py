# Problem: Find All Duplicates in an Array - https://leetcode.com/problems/find-all-duplicates-in-an-array/description/

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        start = 0
        while start < len(nums):
            idx = nums[start] 
            if nums[start] != nums[idx - 1]:
                nums[start], nums[idx - 1] = nums[idx - 1], nums[start]
            else:
                start += 1

        ans = []
        for i, num in enumerate(nums):
            if i + 1 != num:
                ans.append(num)
        
        return ans
