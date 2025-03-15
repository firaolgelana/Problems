# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        def dfs(left_node, right_node, level):
            if not left_node:
                return
            if level & 1:
                left_node.val, right_node.val = right_node.val, left_node.val
            dfs(left_node.left, right_node.right, level + 1)
            dfs(left_node.right, right_node.left, level + 1)
        
        dfs(root.left, root.right, 1)
        return root