# Problem: Sum of Nodes with Even-Valued Grandparent - https://leetcode.com/problems/sum-of-nodes-with-even-valued-grandparent/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def cal_sum(self, node, depth):
        _sum = 0
        if not node:
            return 0
        if depth == 2:
            return node.val
        _sum += self.cal_sum(node.left, depth + 1)
        _sum += self.cal_sum(node.right, depth + 1)
        return _sum
        
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        _sum = 0
        def dfs(node, depth):
            nonlocal _sum
            if not node:
                return
            if node.val % 2 == 0:
                _sum += self.cal_sum(node, 0)

            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return _sum

        