# Problem: Symmetric tree - https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        while queue:
            size = len(queue)
            symmetric = []
            for _ in range(size):
                current = queue.popleft()
                if current.left:
                    queue.append(current.left)
                    symmetric.append(current.left.val)
                else:
                    symmetric.append(101)
                if current.right:
                    queue.append(current.right)
                    symmetric.append(current.right.val)
                else:
                    symmetric.append(101)
            if queue:
                for i in range((len(symmetric)) // 2):
                    if symmetric[i] != symmetric[-(i + 1)]:
                        return False
        
        return True

                
        