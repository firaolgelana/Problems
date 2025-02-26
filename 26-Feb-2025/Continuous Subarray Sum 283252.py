# Problem: Continuous Subarray Sum - https://leetcode.com/problems/continuous-subarray-sum/

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        good_count = {0:-1}
        count = 0
        for i in range(len(nums)):
            count += nums[i]
            remainder = count % k
            if remainder in good_count and i - good_count[remainder] >= 2:
                return True
            if remainder not in good_count:
                good_count[remainder] = i
        
        return False
        