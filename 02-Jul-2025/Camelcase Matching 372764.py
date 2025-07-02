# Problem: Camelcase Matching - https://leetcode.com/problems/camelcase-matching/

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        def check(q, p):
            i, j = 0, 0
            q_capital = sum(1 for i in q if i.isupper())
            p_capital = sum(1 for i in p if i.isupper())
            while i < len(p) and j < len(q):
                if p[i] == q[j]:
                    i += 1
                j += 1
            return i == len(p) and p_capital == q_capital

        ans = []
        for i in range(len(queries)):
            ans.append(check(queries[i], pattern))

        return ans
        