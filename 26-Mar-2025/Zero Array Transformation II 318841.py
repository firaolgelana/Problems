# Problem: Zero Array Transformation II - https://leetcode.com/problems/zero-array-transformation-ii/

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def is_possible(mid):
            prefix = [0] * (len(nums) + 1)
            for i in range(mid):
                l, r, val = queries[i]
                prefix[l] += val
                prefix[r + 1] -= val
            prefix = list(accumulate(prefix))
            for x, y in zip(prefix, nums):
                if y > x:
                    return False
            return True

        low, high = 0, len(queries)
        while low <= high:
            mid = low + (high - low) // 2
            if is_possible(mid):
                high = mid - 1
            else:
                low = mid + 1
        
        return low if low <= len(queries) else -1
                