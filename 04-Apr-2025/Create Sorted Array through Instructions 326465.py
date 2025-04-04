# Problem: Create Sorted Array through Instructions - https://leetcode.com/problems/create-sorted-array-through-instructions/

class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        n, modulo = len(instructions), 10 ** 9 + 7
        nums = []
        cost = 0
        for i in range(n):
            num = instructions[i]
            left_pos = bisect_left(nums, num)
            right_pos = bisect_right(nums, num)
            cost += min(left_pos, len(nums) - right_pos)
            insort(nums, num)

        return cost % modulo


        