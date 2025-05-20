# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        letter_idx = [i for i in range(len(s)) if s[i].isalpha()]
        total = 1 << len(letter_idx)
        res = []
        for i in range(total):
            arr = list(s)
            for bit in range(len(letter_idx)):
                j = letter_idx[bit]
                if (i >> bit) & 1:
                    arr[j] = s[j].swapcase()

            res.append("".join(arr))

        return res

