# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for i in range(n + 1):
            count = 0
            while i > 0:
                count += i & 1
                i >>= 1
            ans.append(count)
        
        return ans
        