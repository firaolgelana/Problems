# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        white, swaps = 0, 0
        for char in reversed(s):
            if char == '0':
                white += 1
            else:
                swaps += white

        return swaps
            
