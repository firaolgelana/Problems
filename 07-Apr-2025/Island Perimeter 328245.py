# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        def is_valid(x, y, n, m):
            return 0 <= x < n and 0 <= y < m
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = [[False] * m for _ in range(n)]
        def calculatePerimeter(x, y, n, m):
            ans = 0
            visited[x][y] = True
            for di, dj in directions:
                newX, newY = x + di, y + dj
                if not is_valid(newX, newY, n, m) or not grid[newX][newY]:
                    ans += 1
                elif is_valid(newX, newY, n, m) and not visited[newX][newY]:
                    ans += calculatePerimeter(newX, newY, n, m)
            return ans
            
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    return calculatePerimeter(i, j, n, m)
        
        return 0
