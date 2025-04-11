# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_count = [0] * n
        for a, b in trust:
            trust_count[b - 1] += 1
            trust_count[a - 1] -= 1
        
        for i in range(n):
            if trust_count[i] == n - 1:
                return i + 1

        return -1
        