# Problem: Merge Two Binary Trees - https://leetcode.com/problems/merge-two-binary-trees/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        merge = TreeNode()
        def merged(node1, node2):
            if not node1 and not node2:
                return None
            val1 = node1.val if node1 else 0
            val2 = node2.val if node2 else 0
            merge = TreeNode(val1 + val2)
            merge.left = merged(node1.left if node1 else None, node2.left if node2 else None)
            merge.right = merged(node1.right if node1 else None, node2.right if node2 else None)
            return merge
        
        return merged(root1, root2)
        