# Problem: Wiggle Subsequence  - https://leetcode.com/problems/wiggle-subsequence/

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        inc, dec = False, False
        count = 1
        for i in range(len(nums) - 1):
            if nums[i] < nums[i+1] and not inc:
               count += 1
               inc, dec = True, False
            elif nums[i] > nums[i+1] and not dec:
                count += 1
                dec, inc = True, False
        
        return count
            
                


        