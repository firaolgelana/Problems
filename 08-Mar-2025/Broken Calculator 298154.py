# Problem: Broken Calculator - https://leetcode.com/problems/broken-calculator/description/

class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        count = 0
        while target > startValue:
            target = target // 2 if target % 2 == 0 else target + 1
            count += 1

        return count + startValue - target
        