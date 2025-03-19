# Problem: Letter Tile Possibilities - https://leetcode.com/problems/letter-tile-possibilities/description/

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        count = 0
        tiles = sorted(tiles)
        seen = [False] * len(tiles)
        def find(idx):
            nonlocal count
            if idx == len(tiles):
                return 
            for i in range(len(tiles)):
                if i > 0 and tiles[i] == tiles[i - 1] and not seen[i - 1]:
                    continue
                if not seen[i]:
                    count += 1
                    seen[i] = True
                    find(idx + 1)
                    seen[i] = False
            return count
        
        return find(0)