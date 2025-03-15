# Problem: Binary Tree Zigzag Level Order Traversal - https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        queue = deque([root])
        level = 0
        zigzag = []
        while queue:
            node = []
            size = len(queue)
            for _ in range(size):
                current = queue.popleft()
                node.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            
            if level & 1:
                zigzag.append(node[::-1])
            else:
                zigzag.append(node)
            level += 1

        return zigzag


        