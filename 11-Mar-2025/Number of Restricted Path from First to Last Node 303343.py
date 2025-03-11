# Problem: Number of Restricted Path from First to Last Node - https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/

class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        modulo = 10 ** 9 + 7
        graph = defaultdict(list)
        for u, v, weight in edges:
            graph[u].append((v, weight))
            graph[v].append((u, weight))

        queue = [(0, n)]
        distance = {i + 1 : float('inf') for i in range(n)}
        distance[n] = 0
        while queue:
            cost, node = heappop(queue)
            for neighbor, weight in graph[node]:
                new_cost = cost + weight
                if new_cost < distance[neighbor]:
                    distance[neighbor] = new_cost
                    heappush(queue, (new_cost, neighbor))

        arr = [-1] * (n + 1)

        def dfs(node):
            if node == n:
                return 1
            if arr[node] != -1:
                return arr[node]
            arr[node] = 0
            for neighbor, weight in graph[node]:
                if distance[neighbor] < distance[node]:
                    arr[node] += dfs(neighbor) 

            return arr[node]

        return dfs(1) % modulo
        