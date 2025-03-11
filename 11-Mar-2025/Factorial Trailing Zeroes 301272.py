# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        def factorial(n):
            if n <= 1:
                return 1
            return n * factorial(n - 1)
        
        count = 0
        fact = factorial(n)
        while fact % 10 == 0:
            count += 1
            fact //= 10

        return count