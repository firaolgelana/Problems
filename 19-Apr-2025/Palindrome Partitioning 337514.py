# Problem: Palindrome Partitioning - https://leetcode.com/problems/palindrome-partitioning/

class Solution:
    def is_palindrome(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def backtrack(idx, current):
            if idx == len(s):
                if all(self.is_palindrome(string) for string in current):
                    ans.append(current[:])
                return

            for i in range(idx, len(s)):
                sub = s[idx:i + 1]
                current.append(sub)
                backtrack(i + 1, current)
                current.pop()

        backtrack(0, [])
        return ans