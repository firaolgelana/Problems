# Problem: Reverse Odd Levels of Binary Tree - https://leetcode.com/problems/reverse-odd-levels-of-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        queue = deque([root])
        level = 0
        while queue:
            node = []
            size = len(queue)
            for _ in range(size):
                current = queue.popleft()
                node.append(current)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

            if level & 1:
                for i in range(len(node) // 2):
                    left, right = node[i], node[-(i + 1)]
                    left.val, right.val = right.val, left.val
                
            level += 1

        return root

