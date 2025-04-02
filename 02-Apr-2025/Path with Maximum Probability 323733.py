# Problem: Path with Maximum Probability - https://leetcode.com/problems/path-with-maximum-probability/

class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        graph = [[] for _ in range(n)]
        for i in range(len(edges)):
            u, v = edges[i]
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))

        queue = [(-1, start_node)]
        distance = [0] * n
        while queue:
            probability, current = heappop(queue)
            for neighbor, prob in graph[current]:
                new_prob = ((-probability) * prob)
                if new_prob > distance[neighbor]:
                    distance[neighbor] = new_prob
                    heappush(queue, (-new_prob, neighbor))

        return distance[end_node]

        