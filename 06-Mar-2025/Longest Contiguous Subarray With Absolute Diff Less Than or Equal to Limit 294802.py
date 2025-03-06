# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        inc, dec = deque(), deque()
        left, longest = 0, float('-inf')
        for i in range(len(nums)):
            while inc and nums[inc[-1]] > nums[i]:
                inc.pop()
            inc.append(i)
            while dec and nums[dec[-1]] < nums[i]:
                dec.pop()
            dec.append(i)
            while left < len(nums) and (nums[dec[0]] - nums[inc[0]] > limit):
                left += 1
                while inc and inc[0] < left:
                    inc.popleft()
                while dec and dec[0] < left:
                    dec.popleft()
                    
            longest = max(longest, i - left + 1)
        
        return longest
            
            

        