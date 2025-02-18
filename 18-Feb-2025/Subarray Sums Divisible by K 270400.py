# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = {0:1}
        nums_subarrays = current_sum = 0
        for num in nums:
            current_sum += num
            remainder = current_sum % k
            nums_subarrays += count.get(remainder, 0)
            count[remainder] = 1 + count.get(remainder, 0)
            
        return nums_subarrays