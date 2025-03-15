# Problem: Maximum Difference Between Node and Ancestor - https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        diff = 0
        def dfs(node, max_num, min_num):
            nonlocal diff
            if not node:
                return 
            max_num = max(max_num, node.val)
            min_num = min(min_num, node.val)
            diff = max(diff, max_num - min_num)
            
            dfs(node.left, max_num, min_num)
            dfs(node.right, max_num, min_num)

        dfs(root, float('-inf'), float('inf'))
        return diff
        