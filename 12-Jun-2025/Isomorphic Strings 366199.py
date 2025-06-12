# Problem: Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapS = {}
        mapT = {}
        for i, j in zip(s, t):
            if i in mapS and mapS[i] != j:
                return False
            else:
                mapS[i] = j
            if j in mapT and mapT[j] != i:
                return False
            else:
                mapT[j] = i


        return True
        