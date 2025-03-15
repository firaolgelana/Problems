# Problem: Count Good Numbers - https://leetcode.com/problems/count-good-numbers/

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        modulo = 10 ** 9 + 7
        def power(x, y):
            if y == 0:
                return 1 
            half = power(x, y // 2)
            half *= half
            if y % 2:
                half *= x
            return half % modulo

        even, odd = ceil(n / 2), n // 2
        good_numbers = power(5, even) * power(4, odd)
        return good_numbers % modulo


