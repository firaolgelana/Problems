# Problem: Split Array Largest Sum - https://leetcode.com/problems/split-array-largest-sum/

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def is_possible_to_split(n):
            count, _sum = 1, 0
            for num in nums:
                _sum += num
                if _sum > n:
                    _sum = num
                    count += 1
            return count <= k

        left, right = max(nums), sum(nums)
        while left <= right:
            mid = left + (right - left) // 2
            if is_possible_to_split(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left