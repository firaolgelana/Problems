# Problem: Balance a Binary Search Tree - https://leetcode.com/problems/balance-a-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        arr = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            arr.append(node.val)
            inorder(node.right)
        
        inorder(root)
        def construct(left, right):
            if left == right:
                return None
            
            mid = left + (right - left) // 2
            node = TreeNode(arr[mid])
            node.left = construct(left, mid)
            node.right = construct(mid + 1, right)
            return node
            
        return construct(0, len(arr))
        