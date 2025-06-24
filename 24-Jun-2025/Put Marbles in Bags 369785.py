# Problem: Put Marbles in Bags - https://leetcode.com/problems/put-marbles-in-bags/

class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        split = []
        for i in range(n - 1):
            split.append(weights[i] + weights[i + 1])
        split.sort()
        return sum(split[n - k:]) - sum(split[:k - 1])