# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum, current_sum = float('-inf'), 0

        for num in nums:
            current_sum += num
            max_sum = max(current_sum, max_sum)
            if current_sum < 0:
                current_sum = 0

        return max_sum