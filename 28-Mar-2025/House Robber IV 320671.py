# Problem: House Robber IV - https://leetcode.com/problems/house-robber-iv/

class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def is_possible(n):
            i, count = 0, 0
            while i < len(nums):
                if nums[i] <= n:
                    count += 1
                    i += 1
                i += 1
            return count >= k

        sorted_nums = sorted(nums)
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if is_possible(sorted_nums[mid]):
                right = mid - 1
            else:
                left = mid + 1
        
        return sorted_nums[left]
      
        