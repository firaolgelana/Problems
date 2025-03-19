# Problem: The k-th Lexicographical String of All Happy Strings of Length n - https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/description/

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        count = 0
        def backtrack(idx, arr):
            nonlocal count
            if idx == n:
                count += 1
                if count == k:
                    return "".join(arr)
                return None
            for char in "abc":
                if not arr or arr[-1] != char:
                    arr.append(char)
                    find = backtrack(idx + 1, arr)
                    if find:
                        return find
                    arr.pop()

        ans = backtrack(0, [])
        return ans if ans else ""