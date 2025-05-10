# Problem: Check if There is a Valid Path in a Grid - https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/

class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        n, m = len(grid), len(grid[0])
        directions = {
            1 : [(0, 1), (0, -1)], 
            2 : [(1, 0), (-1,  0)],
            3 : [(0, -1), (1, 0)],
            4 : [(1, 0), (0, 1)], 
            5 : [(0, -1), (-1, 0)],
            6 : [(-1, 0), (0, 1)]
        }
        visited = [[False] * m for _ in range(n)]
        queue = deque([(0, 0)])
        while queue:
            row, col = queue.popleft()
            if visited[row][col]:
                continue
            visited[row][col] = True
            if (row, col) == (n - 1, m - 1):
                return True
            for di, dj in directions[grid[row][col]]:
                nx, ny = di + row, dj + col
                if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                    if any((x + nx, y + ny) == (row, col) for x, y in directions[grid[nx][ny]]):
                        queue.append((nx, ny))
        
        return False
        