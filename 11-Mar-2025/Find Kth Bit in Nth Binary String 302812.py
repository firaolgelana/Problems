# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(s):
            return "".join('1' if char == '0' else '0' for char in s)
            
        def findBinary(n):
            if n == 1:
                return '0'
            s = findBinary(n - 1)
            return s + "1" + invert(s)[::-1]
        
        return findBinary(n)[k - 1]

        
        