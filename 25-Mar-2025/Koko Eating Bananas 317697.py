# Problem: Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat(k):
            count = 0
            for banana in piles:
                count += ceil(banana / k)
            return count <= h

        left, right = 1, max(piles)
        while left <= right:
            mid = left + (right - left) // 2
            if can_eat(mid):
                right = mid - 1
            else:
                left = mid + 1
        
        return left
        