# Problem: Find Champion II - https://leetcode.com/problems/find-champion-ii/

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        for u, v in edges:
            graph[u].append(v)

        def dfs(node, seen):
            seen.add(node)
            for adj in graph[node]:
                if adj not in seen:
                    dfs(adj, seen)

        for i in range(n):
            seen = set()
            dfs(i, seen)
            if all(x in seen for x in range(n)):
                return i

        return -1
        