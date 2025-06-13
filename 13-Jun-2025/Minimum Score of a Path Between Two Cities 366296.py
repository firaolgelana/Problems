# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b, d in roads:
            graph[a].append((b, d))
            graph[b].append((a, d))
        
        visited = set()
        queue = deque([1])
        min_dist = float('inf')

        while queue:
            node = queue.popleft()
            visited.add(node)

            for neighbor, dist in graph[node]:
                min_dist = min(min_dist, dist)
                if neighbor not in visited:
                    queue.append(neighbor)

        return min_dist
