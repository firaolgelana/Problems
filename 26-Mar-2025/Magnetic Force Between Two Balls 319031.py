# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def is_possible(n):
            count = 1
            start = position[0]
            for num in position:
                if num - start >= n:
                    count += 1
                    start = num
            return count >= m

        low, high = 1, max(position) - min(position)
        while low <= high:
            mid = low + (high - low) // 2
            if is_possible(mid):
                low = mid + 1
            else:
                high = mid - 1
            
        return high
        