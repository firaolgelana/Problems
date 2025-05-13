# Problem: Missing Number - https://leetcode.com/problems/missing-number/description/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums) + 1):
            count ^= i
            
        for num in nums:
            count ^= num
        
        return count
            
        