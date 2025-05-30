# Problem: Find the Substring With Maximum Cost - https://leetcode.com/problems/find-the-substring-with-maximum-cost/

class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        dp = [inf] * 26
        for i in range(len(chars)):
            dp[ord(chars[i]) - ord('a')] = vals[i]
        max_cost = ans = 0
        for i in range(len(s)):
            idx = ord(s[i]) - ord('a')
            if dp[idx] == inf:
                max_cost = max_cost + idx + 1
            else:
                max_cost = max(max_cost + dp[idx], 0)
            ans = max(ans, max_cost)
        
        return ans


        