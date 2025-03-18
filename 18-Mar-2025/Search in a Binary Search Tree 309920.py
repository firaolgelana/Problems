# Problem: Search in a Binary Search Tree - https://leetcode.com/problems/search-in-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        queue = [root]
        while queue:
            node = queue.pop()
            if node.val == val:
                return node
            if node.val > val:
                if not node.left:
                    return None
                queue.append(node.left)
            else:
                if not node.right:
                    return None
                queue.append(node.right)
        