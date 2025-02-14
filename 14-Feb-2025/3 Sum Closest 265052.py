# Problem: 3 Sum Closest - https://leetcode.com/problems/3sum-closest/description/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        size = len(nums)
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]
        for i in range(size):
            left, right = i + 1, size - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right] 
                if abs(current_sum - target) < abs(closest - target):
                    closest = current_sum
                if current_sum < target:
                    left += 1
                else:
                    right -= 1
        
        return closest
        