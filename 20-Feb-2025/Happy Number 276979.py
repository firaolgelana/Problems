# Problem: Happy Number - https://leetcode.com/problems/happy-number/description/

class Solution:
    def isHappy(self, n: int) -> bool:
        def squares(num):
            squares = 0
            while num > 0:
                squares += (num % 10) ** 2
                num //= 10

            return squares
        
        seen = set()
        while n not in seen:
            seen.add(n)
            n = squares(n)
            if n == 1:
                return True

        return False
        