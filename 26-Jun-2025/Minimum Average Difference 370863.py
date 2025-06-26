# Problem: Minimum Average Difference - https://leetcode.com/problems/minimum-average-difference/

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)        
        prefix_sum = [0] * n
        prefix_sum[0] = nums[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i-1] + nums[i]
        
        total_sum = prefix_sum[-1]
        min_diff = float('inf')
        result_index = 0
        
        for i in range(n):
            left_sum = prefix_sum[i]
            left_avg = left_sum // (i + 1)
            
            if i == n - 1:
                right_avg = 0
            else:
                right_sum = total_sum - left_sum
                right_avg = right_sum // (n - i - 1)
            
            current_diff = abs(left_avg - right_avg)
            
            if current_diff < min_diff:
                min_diff = current_diff
                result_index = i
            elif current_diff == min_diff:
                if i < result_index:
                    result_index = i
        
        return result_index
            