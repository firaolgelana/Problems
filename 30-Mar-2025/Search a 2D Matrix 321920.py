# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) - 1
        while left <= right:
            mid = left + (right - left)//2
            if matrix[mid][0] > target:
                right = mid - 1
            else:
                left = mid + 1
        low, high = 0, len(matrix[0]) - 1
        while low <= high:
            mid = low + (high - low)//2
            if matrix[right][mid] == target:
                return True
            elif matrix[right][mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False
        