# Problem: Duplicate Zeros - https://leetcode.com/problems/duplicate-zeros/description/?envType=problem-list-v2&envId=two-pointers

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zeros = arr.count(0)
        for i in reversed(range(len(arr))):
            if i + zeros < len(arr):
                arr[i + zeros] = arr[i]
            if arr[i] == 0:
                zeros -= 1
                if i + zeros < len(arr):
                    arr[i + zeros] = 0
