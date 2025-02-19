# Problem: Maximum Score After Splitting a String  - https://leetcode.com/problems/maximum-score-after-splitting-a-string/

class Solution:
    def maxScore(self, s: str) -> int:
        ones, zeros = s.count('1'), 0
        max_score = 0
        for i in range(len(s) - 1):
            if s[i] == '1':
                ones -= 1
            else:
                zeros += 1
            max_score = max(max_score, ones + zeros)

        return max_score        