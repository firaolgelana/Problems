# Problem: Symmetric tree - https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        left_subtree = root.left
        right_subtree = root.right
        def dfs(left_subtree, right_subtree):
            if not left_subtree and not right_subtree:
                return True
            if not left_subtree or not right_subtree:
                return False
            
            return left_subtree.val == right_subtree.val and dfs(left_subtree.left, right_subtree.right) and dfs(left_subtree.right, right_subtree.left)

        return dfs(left_subtree, right_subtree)