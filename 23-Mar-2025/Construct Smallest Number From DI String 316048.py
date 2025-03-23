# Problem: Construct Smallest Number From DI String - https://leetcode.com/problems/construct-smallest-number-from-di-string/description/

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        visited = [False] * 10
        def backtrack(arr):
            if len(arr) == len(pattern) + 1:
                return "".join(str(num) for num in arr)

            for i in range(9):
                l = len(arr)
                if arr and ((pattern[l - 1] == "I" and arr[-1] > i + 1)
                 or (pattern[l - 1] == "D" and arr[-1] < i + 1)):
                    continue
                if not visited[i]:
                    arr.append(i + 1)
                    visited[i] = True
                    find = backtrack(arr)
                    if find:
                        return find
                    visited[i] = False
                    arr.pop()

        return backtrack([])

        