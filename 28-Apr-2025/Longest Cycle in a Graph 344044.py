# Problem: Longest Cycle in a Graph - https://leetcode.com/problems/longest-cycle-in-a-graph/

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        indegree = [0] * n
        graph = [[] for _ in range(n)]
        for i in range(n):
            if edges[i] != -1:
                graph[i].append(edges[i])
                indegree[edges[i]] += 1

        queue = deque([i for i in range(n) if indegree[i] == 0])
        visited = [False] * n
        while queue:
            current = queue.popleft()
            visited[current] = True
            for neighbor in graph[current]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        def dfs(node):
            ans = 1
            visited[node] = True
            for neighbor in graph[node]:
                if not visited[neighbor]:
                    ans += dfs(neighbor)
            return ans
            
        ans = -1
        for i in range(n):
            if not visited[i] and edges[i] != -1:
                ans = max(ans, dfs(i))
        
        return ans
        


            

        