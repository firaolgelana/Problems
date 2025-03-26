# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def search(mid):
            count = 0
            for rank in ranks:
                count += floor(sqrt(mid//rank))
            return count >= cars
            
        left, right = 1, max(ranks) * cars * cars
        while left <= right:
            mid = left + (right - left) // 2
            if search(mid):
                right = mid - 1
            else:
                left = mid + 1
            
        return left
        