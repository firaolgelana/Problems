# Problem: Minimum Operations to Exceed Threshold Value II - https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapify(nums)
        operations = 0
        while len(nums) >= 2:
            first_min = heappop(nums)
            if first_min >= k:
                return operations
            second_min = heappop(nums)
            add_num = min(first_min, second_min) * 2 + max(first_min, second_min)
            heappush(nums, add_num)
            operations += 1
        return operations
        