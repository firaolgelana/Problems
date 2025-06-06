# Problem: Repeated DNA Sequences - https://leetcode.com/problems/repeated-dna-sequences/

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        mapping = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        seen, ans = set(), set()
        hash_val = 0
        mask = (1 << 20) - 1
        for i in range(min(len(s), 10)):
            hash_val = (hash_val << 2) | mapping[s[i]]
        seen.add(hash_val)

        for i in range(10, len(s)):
            hash_val = ((hash_val << 2) | mapping[s[i]]) & mask
            if hash_val in seen:
                ans.add(s[i-9:i+1])
            else:
                seen.add(hash_val)

        return list(ans)



        

        