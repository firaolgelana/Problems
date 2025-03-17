# Problem: Path Sum III - https://leetcode.com/problems/path-sum-iii/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find(self, node, target, _sum):
        if not node:
            return 0 
        _sum += node.val
        count = 1 if _sum == target else 0
        count += self.find(node.left, target, _sum)
        count += self.find(node.right, target, _sum)
        return count
        
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = 0
        def dfs(node):
            nonlocal count
            if not node:
                return 
            count += self.find(node, targetSum, 0)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return count
        