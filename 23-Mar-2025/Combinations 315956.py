# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def backtrack(idx, arr):
            if len(arr) == k:
                ans.append(arr[:])
                return
            for num in range(idx, n):
                arr.append(num + 1)
                backtrack(num + 1, arr)
                arr.pop()

        backtrack(0, [])
        return ans            