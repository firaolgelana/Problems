# Problem: Grid Game - https://leetcode.com/problems/grid-game/

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n =len(grid[0])
        suffix = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix[i] = grid[0][i] + suffix[i+1]

        _sum = 0
        for i in range(n - 1):
            _sum += grid[1][i]
            if _sum < suffix[i+1]:
                continue
            else:
                return max(_sum - grid[1][i], suffix[i+1])

        return _sum
