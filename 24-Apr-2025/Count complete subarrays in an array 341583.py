# Problem: Count complete subarrays in an array - https://leetcode.com/problems/count-complete-subarrays-in-an-array/

class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        distinct = len(set(nums))
        maps = defaultdict(int)
        left = ans = 0
        for right in range(len(nums)):
            maps[nums[right]] += 1
            while len(maps) >= distinct:
                ans += len(nums) - right
                maps[nums[left]] -= 1
                if maps[nums[left]] == 0:
                    del maps[nums[left]]
                left += 1
                
        return ans

        