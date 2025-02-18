# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        modulo = 10 ** 9 + 7
        prefix_sum = [0] * (len(nums) + 1)
        for start, end in requests:
            prefix_sum[start] += 1
            prefix_sum[end + 1] -= 1
        
        for i in range(len(nums)):
            prefix_sum[i + 1] += prefix_sum[i]

        prefix_sum.sort(reverse=True)
        nums.sort(reverse=True)
        
        total_sum = 0
        for num, pre in zip(nums, prefix_sum):
            total_sum += (num * pre)

        return total_sum % modulo



        
        