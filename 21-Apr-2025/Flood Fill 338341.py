# Problem: Flood Fill - https://leetcode.com/problems/flood-fill/

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n, m = len(image), len(image[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        def inbound(row, col):
            return 0 <= row < n and 0 <= col < m
        
        queue = [(sr, sc)]
        old_color = image[sr][sc]
        if color == old_color:
            return image
        image[sr][sc] = color
        while queue:
            row, col = queue.pop()
            for di, dj in directions:
                newx, newy = di + row, dj + col
                if inbound(newx, newy) and image[newx][newy] == old_color:
                    image[newx][newy] = color
                    queue.append((newx, newy))

        return image
        
