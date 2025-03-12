# Problem: All Ancestors of a Node in a Directed Acyclic Graph - https://leetcode.com/problems/all-ancestors-of-a-node-in-a-directed-acyclic-graph/

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        in_degree = [0] * n
        for u, v in edges:
            graph[u].append(v)
            in_degree[v] += 1
        
        ancestors = [set() for i in range(n)]
        queue = deque([i for i in range(n) if in_degree[i] == 0])

        while queue:
            node = queue.popleft()
            for neighbor in graph[node]:
                if ancestors[node]:
                    ancestors[neighbor].update(ancestors[node])
                ancestors[neighbor].add(node)
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)

        ancestors = [sorted(ancestors[i]) for i in range(n)]
        return ancestors
            

        