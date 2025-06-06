# Problem: Subarray Product Less Than K - https://leetcode.com/problems/subarray-product-less-than-k/

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        count, left = 0, 0
        product = 1
        for right in range(len(nums)):
            product *= nums[right]
            while product >= k and left <= right:
                product //= nums[left]
                left += 1

            count += right - left + 1

        return count