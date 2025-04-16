# Problem: Shortest Path with Alternating Colors - https://leetcode.com/problems/shortest-path-with-alternating-colors/description/

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        redGraph = [[] for _ in range(n)]
        blueGraph = [[] for _ in range(n)]
        for u, v in redEdges:
            redGraph[u].append(v)
        for u, v in blueEdges:
            blueGraph[u].append(v)
        ans = [-1] * n
        queue = deque([(0, 1), (0, 2)])
        seen = set(queue)
        distance = 0
        while queue:
            size = len(queue)
            for _ in range(size):
                node, colors = queue.popleft()
                if colors == 1:
                    for child in redGraph[node]:
                        if not (child, 2) in seen:
                            queue.append((child, 2))
                            seen.add((child, 2))
                else:
                    for child in blueGraph[node]:
                        if not (child, 1) in seen:
                            queue.append((child, 1))
                            seen.add((child, 1))
                if ans[node] == -1:
                    ans[node] = distance
                else:
                    ans[node] = min(ans[node], distance)
            distance += 1
        
        return ans
