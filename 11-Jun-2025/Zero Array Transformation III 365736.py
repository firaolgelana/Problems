# Problem: Zero Array Transformation III - https://leetcode.com/problems/zero-array-transformation-iii/description/

class Solution:
    def maxRemoval(self, nums: List[int], queries: List[List[int]]) -> int:
        queries.sort()
        heap = []
        prefix = [0] * (len(nums) + 1)
        val = j = 0
        for i in range(len(nums)):
            val += prefix[i]
            while j < len(queries) and queries[j][0] <= i:
                l, r = queries[j]
                heappush(heap, (-r, l))
                j += 1
            while heap and val < nums[i]:
                r, l = heappop(heap)
                if -r >= i:
                    val += 1
                    prefix[-r + 1] -= 1
            if val < nums[i]:
                return -1

        return len(heap)