# Problem: Longest Subarray of 1's After Deleting One Element - https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        change = False
        left = ans = 0
        for right in range(len(nums)):
            if nums[right] == 0 and not change:
                change = True
            elif nums[right] == 0 and change:
                while nums[left] != 0:
                    left += 1
                left += 1
            ans = max(ans, right - left + 1)

        return ans - 1

