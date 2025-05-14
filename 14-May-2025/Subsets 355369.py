# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        total_subsets = 1 << len(nums)
        for i in range(total_subsets):
            arr = []
            for j in range(i.bit_length()):
                if (i >> j) & 1:
                    arr.append(nums[j])
            res.append(arr)

        return res

