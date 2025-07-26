# Problem: 01 Matrix - https://leetcode.com/problems/01-matrix/

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        queue = deque([(row, col) for row in range(n) for col in range(m) if mat[row][col] == 0])
        distance = [[inf] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if not mat[i][j]:
                    distance[i][j] = 0
        directions = (0, 1, 0, -1, 0)
        def inbound(row, col):
            return 0 <= row < n and 0 <= col < m
        while queue:
            row, col = queue.popleft()
            for x, y in pairwise(directions):
                nx, ny = x + row, y + col
                if inbound(nx, ny) and mat[nx][ny]:
                    if distance[row][col] + 1 < distance[nx][ny]:
                        distance[nx][ny] = distance[row][col] + 1
                        queue.append((nx, ny))
        
        return distance

        