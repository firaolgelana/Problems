# Problem: Interval List Intersections - https://leetcode.com/problems/interval-list-intersections/

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        intervals = []
        first, second = 0, 0
        while first < len(firstList) and second < len(secondList):
            start = max(firstList[first][0], secondList[second][0])
            end = min(firstList[first][1], secondList[second][1])
            if start <= end:
                intervals.append([start, end])
            if firstList[first][1] < secondList[second][1]:
                first += 1
            else:
                second += 1

        return intervals

       