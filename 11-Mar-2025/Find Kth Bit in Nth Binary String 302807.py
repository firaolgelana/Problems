# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(s):
            list_s = list(s)
            i, j = 0, len(s) - 1
            while i <= j:
                if list_s[i] != list_s[j]:
                    pass
                else:
                    list_s[i] = list_s[j] =  str(1 - int(list_s[i]))
                i += 1
                j -= 1
            return "".join(list_s)
        def findBinary(n):
            if n == 1:
                return '0'
            s = findBinary(n - 1)
            return s + "1" + invert(s)

        return findBinary(n)[k - 1]

        
        