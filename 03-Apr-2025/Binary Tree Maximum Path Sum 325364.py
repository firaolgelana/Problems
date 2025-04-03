# Problem: Binary Tree Maximum Path Sum - https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = root.val
        def dfs(node):
            if not node:
                return 0
            
            left_sum = max(0, dfs(node.left))
            right_sum = max(0, dfs(node.right))
            self.ans = max(self.ans, left_sum + right_sum + node.val)

            return max(left_sum, right_sum) + node.val

        dfs(root)
        return self.ans