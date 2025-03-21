# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        seen = [False] * len(nums)
        def find_permutation(idx, arr):
            if idx == len(nums):
                ans.append(arr[:])
                return
            
            for i in range(len(nums)):
                if not seen[i]:
                    seen[i] = True
                    arr.append(nums[i])
                    find_permutation(idx + 1, arr)
                    arr.pop()
                    seen[i] = False

        find_permutation(0, [])
        return ans
        