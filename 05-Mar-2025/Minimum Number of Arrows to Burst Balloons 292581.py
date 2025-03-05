# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:(x[1], x[0]))
        coverage = points[0][1]
        count = 1
        for start, end in points:
            if start > coverage:
                count += 1
                coverage = end
        
        return count