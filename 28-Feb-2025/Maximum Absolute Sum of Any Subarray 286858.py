# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_absSum = float('-inf')
        min_sum, max_sum = 0, 0

        for num in nums:
            max_sum = max(max_sum + num, num)
            min_sum = min(num + min_sum, num)
            max_absSum = max(max_absSum, abs(min_sum), max_sum)
        
        return max_absSum

        