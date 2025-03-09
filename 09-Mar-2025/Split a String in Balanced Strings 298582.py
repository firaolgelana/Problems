# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            r = s[:i+1].count('R')
            count += r == i - r + 1
                
        return count
        