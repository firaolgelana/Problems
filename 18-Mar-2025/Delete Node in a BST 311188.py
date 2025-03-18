# Problem: Delete Node in a BST - https://leetcode.com/problems/delete-node-in-a-bst/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def dfs(node, key):
            if not node:
                return None
            if node.val > key:
                node.left = dfs(node.left, key)
            elif node.val < key:
                node.right = dfs(node.right, key)
            else:
                if not node.left:
                    return node.right
                elif not node.right:
                    return node.left
                current = node.right
                while current.left:
                    current = current.left
                node.val, current.val = current.val, current.val + 0.5
                return dfs(node, current.val)

            return node

        return dfs(root, key)

                

                