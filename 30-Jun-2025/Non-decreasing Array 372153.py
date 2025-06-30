# Problem: Non-decreasing Array - https://leetcode.com/problems/non-decreasing-array/

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        def check(idx):
            arr = nums[::]
            arr.pop(idx)
            for i in range(len(arr) - 1):
                if arr[i] > arr[i + 1]:
                    return False

            return True
        idx = 0
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:
                idx = i
                break
        return check(idx - 1) or check(idx)
        
        
        