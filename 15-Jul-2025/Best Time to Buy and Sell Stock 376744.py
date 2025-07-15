# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        pre = [inf] * (n + 1)
        suf = [-inf] * (n + 1)
        for i in range(n):
            pre[i + 1] = min(pre[i], prices[i])
        for i in reversed(range(n)):
            suf[i - 1] = max(suf[i], prices[i])
        ans = 0
        for i in range(n):
            ans = max(ans, suf[i] - pre[i + 1])

        return ans