# Problem: Divide intervals into minimum number of groups - https://leetcode.com/problems/divide-intervals-into-minimum-number-of-groups/

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        pair_list = []
        count = 0
        max_count = 0
        for i in intervals:
            pair_list.append([i[0],1])
            pair_list.append([i[1]+1,-1])
        pair_list.sort()
        for i in pair_list:
            count += i[1]
            max_count = max(max_count,count)
        return max_count
        