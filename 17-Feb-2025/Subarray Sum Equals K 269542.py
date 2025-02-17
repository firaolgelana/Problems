# Problem: Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        current_sum = nums_subarrays = 0
        count = defaultdict(int)
        count[0] += 1
        for num in nums:
            current_sum += num
            nums_subarrays += count[current_sum - k]
            count[current_sum] += 1
            
        return nums_subarrays

            