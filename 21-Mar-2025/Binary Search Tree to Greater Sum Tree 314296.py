# Problem: Binary Search Tree to Greater Sum Tree - https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.total = 0
        def dfs(node):
            if not node:
                return 0
            
            right = dfs(node.right)
            self.total += node.val
            node.val = self.total
            left = dfs(node.left)

            return self.total

        dfs(root)
        return root
            
        