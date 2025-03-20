# Problem: Combination Sum - https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        def backtrack(idx, arr):
            if sum(arr) > target:
                return 
            if sum(arr) == target:
                ans.append(arr[:])
                return
            if idx == len(candidates):
                return
            arr.append(candidates[idx])
            backtrack(idx, arr)
            arr.pop()
            backtrack(idx + 1, arr)

        backtrack(0, [])
        
        return ans
        