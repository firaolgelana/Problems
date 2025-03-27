# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def search(mid):
            count = 0
            for candy in candies:
                count += candy // mid
            return count >= k

        left, right = 1, max(candies)
        while left <= right:
            mid = left + (right - left) // 2
            if search(mid):
                left = mid + 1
            else:
                right = mid - 1

        return right
            
        