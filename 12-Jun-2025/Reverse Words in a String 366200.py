# Problem: Reverse Words in a String - https://leetcode.com/problems/reverse-words-in-a-string/

class Solution:
    def reverseWords(self, s: str) -> str:
        ans = ""
        words = s.split()
        return " ".join(reversed(words))
        