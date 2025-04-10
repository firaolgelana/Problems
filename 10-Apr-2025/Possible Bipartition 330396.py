# Problem: Possible Bipartition - https://leetcode.com/problems/possible-bipartition/

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]
        for u, v in dislikes:
            graph[u - 1].append(v - 1)
            graph[v - 1].append(u - 1)
        
        colors = [-1] * n 
        def dfs(node):
            for neighbor in graph[node]:
                if colors[neighbor] == -1:
                    colors[neighbor] = colors[node] ^ 1
                    if dfs(neighbor):
                        return True
                elif colors[neighbor] == colors[node]:
                    return True
            return False

        for i in range(n):
            if colors[i] == -1:
                colors[i] = 0
                if dfs(i):
                    return False
        return True