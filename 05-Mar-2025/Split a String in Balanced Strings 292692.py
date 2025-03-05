# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r = l = count = 0
        for bal in s:
            r += bal == 'R'
            l += bal == 'L'
            if r == l:
                count += 1
                
        return count
        