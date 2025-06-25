# Problem: Smallest Range Covering Elements from K Lists - https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        arr = [(val, i) for i, row in enumerate(nums) for val in row]
        arr.sort()
        count_row = defaultdict(int)
        intervals, left = [], 0

        for val, idx in arr:
            count_row[idx] += 1
            while len(count_row) >= len(nums):
                if not intervals or (val - arr[left][0] < intervals[1] - intervals[0]):
                    intervals = [arr[left][0], val]
                count_row[arr[left][1]] -= 1
                if count_row[arr[left][1]] == 0:
                    del count_row[arr[left][1]]
                left += 1

        return intervals



        