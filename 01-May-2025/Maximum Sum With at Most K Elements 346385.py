# Problem: Maximum Sum With at Most K Elements - https://leetcode.com/problems/maximum-sum-with-at-most-k-elements/description/

class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        n, m = len(grid), len(grid[0])
        nums = []
        for i in range(n):
            heap = []
            for j in range(m):
                heappush(heap, grid[i][j])
                if len(heap) > limits[i]:
                    heappop(heap)
                    
            nums.extend(heap)
        heapify(nums)
        return sum(nlargest(k, nums))

        
        