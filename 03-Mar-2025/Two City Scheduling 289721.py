# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        min_cost, n = 0, len(costs)
        diff = [(abs(a - b), a, b) for a, b in costs]
        diff.sort(reverse=True)
        count_a = count_b = 0
        for d, a, b in diff:
            if count_a == n // 2:
                min_cost += b
            elif count_b == n // 2:
                min_cost += a
            elif a < b:
                min_cost += a
                count_a += 1
            else:
                min_cost += b
                count_b += 1
        
        return min_cost


        