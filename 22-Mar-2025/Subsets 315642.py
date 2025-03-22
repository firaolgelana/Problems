# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        def backtrack(idx, arr):
            ans.append(arr[:])
            for i in range(idx, len(nums)):
                arr.append(nums[i])
                backtrack(i + 1, arr)
                arr.pop()

        backtrack(0, [])
        return ans