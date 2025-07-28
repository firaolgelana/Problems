# Problem: Count Number of Maximum Bitwise-OR Subsets - https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/description/

class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        for num in nums:
            max_or |= num
        
        total = 1 << len(nums)
        result = 0
        for i in range(total):
            count = 0
            for j in range(len(nums)):
                if (i >> j) & 1:
                    count |= nums[j]
            
            result += count == max_or

        return result
            

        
        