# Problem: Longest Nice Substring - https://leetcode.com/problems/longest-nice-substring/

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def dfs(string):
            chars = set(string)
            if len(string) == 1:
                return ""
            for i in range(len(string)):
                if string[i].swapcase() not in chars:
                    left = dfs(string[:i])
                    right = dfs(string[i + 1:])

                    if len(left) >= len(right):
                        return left
                    else:
                        return right

            return string

        return dfs(s)
        