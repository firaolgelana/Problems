# Problem: Maximize Happiness of Selected Children - https://leetcode.com/problems/maximize-happiness-of-selected-children/?envType=daily-question&envId=2024-05-09

class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        count = max_sum = 0
        happiness.sort()
        n = len(happiness)
        for _ in range(n - 1, n -  k - 1, -1):
            max_sum += happiness[_] - count if happiness[_] >= count else 0
            count += 1

        return max_sum


        