# Problem: Maximum Sum BST in Binary Tree - https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def findMax(root):
            nonlocal ans
            if not root:
                return [0, float('inf'), float('-inf')]
            
            leftSum, leftMin, leftMax = findMax(root.left)
            rightSum, rightMin, rightMax = findMax(root.right)
            
            if leftMax < root.val < rightMin:
                currSum = leftSum + root.val + rightSum
                ans = max(ans, currSum)
                return currSum, min(root.val, leftMin), max(root.val, rightMax)
            else:
                return [0, float('-inf'), float('inf')]

        findMax(root)
        return ans
            
            
            

        