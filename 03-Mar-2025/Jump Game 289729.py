# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_jump = 0
        for i in range(len(nums) - 1):
            max_jump = max(max_jump, nums[i] + i)
            if max_jump <= i:
                return False
            
        return True
        