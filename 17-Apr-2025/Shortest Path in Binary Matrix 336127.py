# Problem: Shortest Path in Binary Matrix - https://leetcode.com/problems/shortest-path-in-binary-matrix/description/

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]:
            return -1
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]
        n = len(grid)
        def inbound(row, col):
            return 0 <= row < n and 0 <= col < n
        visited = [[False] * n for _ in range(n)]
        queue = [(1, 0, 0)]
        visited[0][0] = True
        while queue:
            cost, row, col = heappop(queue)
            if row == n - 1 and col == n - 1:
                return cost
            for di, dj in directions:
                newx, newy = di + row, dj + col
                if inbound(newx, newy) and not visited[newx][newy] and not grid[newx][newy]:
                    visited[newx][newy] = True
                    heappush(queue, (cost + 1, newx, newy))

        return -1
                    