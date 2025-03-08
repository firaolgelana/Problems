# Problem: Minimum Recolors to Get K Consecutive Black Blocks - https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white = blocks[:k].count('W')
        min_recolor = white
        for i in range(k, len(blocks)):
            if blocks[i - k]  == 'B' and blocks[i] == 'W':
                white += 1
            if blocks[i - k] == 'W' and blocks[i] == 'B':
                white -= 1
            min_recolor = min(min_recolor, white)

        return min_recolor


        