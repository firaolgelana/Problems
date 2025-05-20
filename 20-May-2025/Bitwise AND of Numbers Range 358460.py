# Problem: Bitwise AND of Numbers Range - https://leetcode.com/problems/bitwise-and-of-numbers-range/

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        bits = [1] * right.bit_length()
        diff = right - left
        x = i = 0
        while x < diff:
            bits[i] = 0
            x += 2 ** i
            i += 1

        ans = 0
        for i in range(len(bits)):
            if bits[i]:
                ans |= 1 << i

        return ans & left & right




        