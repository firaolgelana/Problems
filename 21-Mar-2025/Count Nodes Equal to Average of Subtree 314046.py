# Problem: Count Nodes Equal to Average of Subtree - https://leetcode.com/problems/count-nodes-equal-to-average-of-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:

        def find(node):
            if not node:
                return 0, 0
            left_count, left_sum = find(node.left)
            right_count, right_sum = find(node.right)
            total_sum = node.val + left_sum + right_sum
            total_count = 1 + left_count + right_count

            return total_count, total_sum
        if not root:
            return 0
        
        length, _sum = find(root)
        count = 1 if _sum // length == root.val else 0
        count += self.averageOfSubtree(root.left)
        count += self.averageOfSubtree(root.right)

        return count
        