# Problem: Number of Subsequences That Satisfy the Given Sum Condition - https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        modulo = 10 ** 9 + 7
        nums.sort()
        subsequences = 0
        for i in range(len(nums)):
            idx = bisect_right(nums, target - nums[i])
            if idx > i:
                subsequences += 2 ** (idx - i - 1)
                subsequences %= modulo

        return subsequences
        