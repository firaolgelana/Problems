# Problem: Same Tree - https://leetcode.com/problems/same-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        
        p_queue, q_queue = deque([p]), deque([q])
        while p_queue and q_queue:
            p_node, q_node = p_queue.popleft(), q_queue.popleft()
            if p_node.val != q_node.val:
                return False
            
            if (p_node.left and not q_node.left) or (not p_node.left and q_node.left):
                return False
            if (p_node.right and not q_node.right) or (not p_node.right and q_node.right):
                return False
            if p_node.left:
                p_queue.append(p_node.left)
                q_queue.append(q_node.left)
            if p_node.right:
                p_queue.append(p_node.right)
                q_queue.append(q_node.right)

        return not p_queue and not q_queue
            

        