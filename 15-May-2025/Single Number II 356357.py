# Problem: Single Number II - https://leetcode.com/problems/single-number-ii/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        bits = [0] * 32
        for num in nums:
            for i in range(32):
                if (1 << i) & num:
                    bits[i] += 1

        ans = 0
        for i in range(32):
            if bits[i] % 3:
                ans += 2 ** i
                
        if ans >= 2 ** 31:
            ans -= 2 ** 32

        return ans
        