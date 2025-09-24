# Problem: Minimum Number of Days to Make m Bouquets - https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1
        def can(day):
            cnt = days = 0
            for i in range(len(bloomDay)):
                if bloomDay[i] > day:
                    cnt = 0
                else:
                    cnt += 1
                if cnt >= k:
                    days += 1
                    cnt = 0
            return days >= m

        left, right = min(bloomDay), max(bloomDay)
        while left <= right:
            mid = left + (right - left) // 2
            if can(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left