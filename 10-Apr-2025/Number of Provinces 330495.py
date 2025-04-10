# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n
        graph = [[] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] and i != j:
                    graph[i].append(j)
        def dfs(node):
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
        count = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                count += 1

        return count

        