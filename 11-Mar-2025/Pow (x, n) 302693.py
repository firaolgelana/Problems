# Problem: Pow (x, n) - https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x, y):
            if y == 1:
                return x
            if y <= 0:
                return 1
            if y & 1:
                return x * power(x, y - 1)
            else:
                p = power(x, y//2)
                return  p * p

        return power(1/x, abs(n)) if n < 0 else power(x, n)
