# Problem: Running Sum of 1d Array - https://leetcode.com/problems/running-sum-of-1d-array/

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefixSum = [0]
        for num in nums:
            prefixSum.append(prefixSum[-1] + num)
        
        return prefixSum[1:]
        