# Problem: Longest Nice Subarray - https://leetcode.com/problems/longest-nice-subarray/

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left = bit = max_count = 0     
        
        for right in range(len(nums)):
            while bit & nums[right] != 0:
                bit ^= nums[left]
                left += 1
                
            bit |= nums[right]
            max_count = max(max_count, right - left + 1)

        return max_count
        