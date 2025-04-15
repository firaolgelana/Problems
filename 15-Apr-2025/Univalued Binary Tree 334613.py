# Problem: Univalued Binary Tree - https://leetcode.com/problems/univalued-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        val = root.val
        queue = deque([root])
        while queue:
            size = len(queue)
            for i in range(size):
                current = queue.popleft()
                if current.val != val:
                    return False
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
                    
        return True
        