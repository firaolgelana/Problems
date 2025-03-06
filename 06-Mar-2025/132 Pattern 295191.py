# Problem: 132 Pattern - https://leetcode.com/problems/132-pattern/

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        last, stack = float('-inf'), []
        for num in reversed(nums):
            if last > num:
                return True
            while stack and stack[-1] < num:
                last = max(last, stack.pop())

            stack.append(num)

        return False