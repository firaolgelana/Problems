# Problem: Longest-consecutive-sequence/ - https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        unique_nums = set(nums)
        longest = 0
        for num in unique_nums:
            if num - 1 not in unique_nums:  
                length = 1
                current = num
                while current + 1 in unique_nums:
                    current += 1
                    length += 1
                longest = max(longest, length)
        
        return longest
