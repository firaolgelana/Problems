# Problem: Find the Punishment Number of an Integer - https://leetcode.com/problems/find-the-punishment-number-of-an-integer/description/

class Solution:
    def punishmentNumber(self, n: int) -> int:
        N = 1
        def backtrack(idx, num, current):
            s = str(num * num)
            if idx == len(s):
                return current == num
            for i in range(idx, len(s)):
                val = int(s[idx:i+1])
                current += val
                if backtrack(i + 1, num, current):
                    return True
                current -= val            
            
        for num in range(2, n + 1):
            if backtrack(0, num, 0):
                N += num * num

        return N

        