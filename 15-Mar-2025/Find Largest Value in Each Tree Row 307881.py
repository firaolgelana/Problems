# Problem: Find Largest Value in Each Tree Row - https://leetcode.com/problems/find-largest-value-in-each-tree-row/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        largest = []
        queue = deque([root])
        while queue:
            size = len(queue)
            min_num = float('-inf')
            for _ in range(size):
                node = queue.popleft()
                min_num = max(min_num, node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            largest.append(min_num)

        return largest
                
        