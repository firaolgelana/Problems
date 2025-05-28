# Problem: Sorting the Sentence - https://leetcode.com/problems/sorting-the-sentence/

class Solution:
    def sortSentence(self, s: str) -> str:
        lst = s.split()
        ans = [0] * len(lst)
        for word in lst:
            ans[int(word[-1]) - 1] = word[:-1]

        return " ".join(ans)
        