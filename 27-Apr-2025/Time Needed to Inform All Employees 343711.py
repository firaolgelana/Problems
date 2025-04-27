# Problem: Time Needed to Inform All Employees - https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = [[] for _ in range(n)]
        for i in range(n):
            if manager[i] != -1:
                graph[manager[i]].append(i)

        visited = [False] * n
        max_time = 0
        def dfs(node, time):
            nonlocal max_time
            visited[node] = True
            max_time = max(max_time, time)
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor, time + informTime[node])

        dfs(headID, 0)
        return max_time

            
