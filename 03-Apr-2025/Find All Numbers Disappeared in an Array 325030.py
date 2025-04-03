# Problem: Find All Numbers Disappeared in an Array - https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        start = 0
        while start < len(nums):
            idx = nums[start] - 1
            if nums[start] != nums[idx]:
                nums[start], nums[idx] = nums[idx], nums[start]
            else:
                start += 1

        ans = []
        for i in range(len(nums)):
            if i != nums[i] - 1:
                ans.append(i + 1)
            
        return ans
        