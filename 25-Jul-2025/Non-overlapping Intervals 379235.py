# Problem: Non-overlapping Intervals - https://leetcode.com/problems/non-overlapping-intervals/description/

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        max_end = -inf
        cnt = 0
        for start, end in intervals:
            if max_end > start:
                continue
            cnt += 1
            max_end = end

        return len(intervals) - cnt