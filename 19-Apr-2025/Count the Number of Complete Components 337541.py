# Problem: Count the Number of Complete Components - https://leetcode.com/problems/count-the-number-of-complete-components/

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = [False] * n
        count = 0

        def bfs(start):
            queue = deque([start])
            nodes = set()
            edges_count = 0
            visited[start] = True
            nodes.add(start)
            
            while queue:
                node = queue.popleft()
                for neighbor in graph[node]:
                    edges_count += 1  
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        nodes.add(neighbor)
                        queue.append(neighbor)
            
            k = len(nodes)
            expected_edges = k * (k - 1)
            return edges_count == expected_edges

        for node in range(n):
            if not visited[node]:
                if bfs(node):
                    count += 1

        return count