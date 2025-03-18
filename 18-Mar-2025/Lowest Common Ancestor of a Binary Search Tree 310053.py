# Problem: Lowest Common Ancestor of a Binary Search Tree - https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ancestors = defaultdict(list)
        def dfs(node, arr):
            if not node:
                return
            arr.append(node)
            ancestors[node].extend(arr[:])
            dfs(node.left, arr)
            dfs(node.right, arr)
            arr.pop()

        dfs(root, [])
        pq_ancestor = 0
        for p_ancestor, q_ancestor in zip(ancestors[p], ancestors[q]):
            if p_ancestor != q_ancestor:
                break
            pq_ancestor = p_ancestor
        
        return pq_ancestor
        
        