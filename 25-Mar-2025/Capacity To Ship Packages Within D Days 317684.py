# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def is_possible(mid):
            count_days, _sum = 0, 0
            for weight in weights:
                _sum += weight
                if _sum > mid:
                    _sum = weight
                    count_days += 1
            return count_days < days

        left, right = max(weights), sum(weights)
        while left <= right:
            mid = left + (right - left) // 2
            if is_possible(mid):
                right = mid - 1
            else:
                left = mid + 1
                
        return left
        