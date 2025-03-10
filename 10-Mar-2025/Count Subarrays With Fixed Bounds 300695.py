# Problem: Count Subarrays With Fixed Bounds - https://leetcode.com/problems/count-subarrays-with-fixed-bounds/

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        left = right = -1
        min_left = -1
        count = 0
        for i in range(len(nums)):
            if nums[i] < minK or nums[i] > maxK:
                min_left = i
                left = right = -1
            else:
                if nums[i] == minK:
                    left = i
                if nums[i] == maxK:
                    right = i
                if left != -1 and right != -1:
                    count += min(left, right) - min_left
        
        return count
                


