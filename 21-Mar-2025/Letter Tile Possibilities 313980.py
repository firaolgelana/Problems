# Problem: Letter Tile Possibilities - https://leetcode.com/problems/letter-tile-possibilities/description/

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        tiles = sorted(tiles)
        self.count = 0
        seen = [False] * len(tiles)
        def backtrack(idx):
            if idx == len(tiles):
                return 
            for i in range(len(tiles)):
                if (i > 0 and (tiles[i] == tiles[i - 1] and not seen[i - 1]) or seen[i]):
                    continue
                self.count += 1
                seen[i] = True
                backtrack(idx + 1)
                seen[i] = False
            return self.count
        
        return backtrack(0)