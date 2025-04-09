# Problem: Construct Quad Tree - https://leetcode.com/problems/construct-quad-tree/description/

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
                                                                                                        
class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def is_all_same(x1, x2, y1, y2):
            val = grid[x1][y1]
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    if grid[i][j] != val:
                        return False, None
            return True, val

        def construct_tree(x1, x2, y1, y2):
            same, val = is_all_same(x1, x2, y1, y2)
            if same:
                return Node(val == 1, True)

            mid_x = (x1 + x2) // 2
            mid_y = (y1 + y2) // 2

            return Node(
                val = 1,
                isLeaf = False,
                topLeft = construct_tree(x1, mid_x, y1, mid_y),
                topRight = construct_tree(x1, mid_x, mid_y + 1, y2),
                bottomLeft = construct_tree(mid_x + 1, x2, y1, mid_y),
                bottomRight = construct_tree(mid_x + 1, x2, mid_y + 1, y2)
            )

        n = len(grid)
        return construct_tree(0, n - 1, 0, n - 1)
