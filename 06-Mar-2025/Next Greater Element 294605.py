# Problem: Next Greater Element - https://leetcode.com/problems/next-greater-element-i/

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack, next_large = [], []
        idx = {val:i for i, val in enumerate(nums2)}

        for num in reversed(nums2):
            while stack and stack[-1] < num:
                stack.pop()
            if not stack:
                next_large.append(-1)
            else:
                next_large.append(stack[-1])
            stack.append(num)

        next_large = next_large[::-1]
        result = [next_large[idx[num]] for num in nums1]
        return result